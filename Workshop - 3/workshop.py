import pandas as pd
import numpy as np
import time
import psutil
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

# --- Microservice: Data Ingestion ---
def ingest_data(labels_path, tracking_path, helmets_path, game_plays):
    try:
        labels = pd.read_csv(labels_path)
        tracking = pd.read_csv(tracking_path)
        helmets = pd.read_csv(helmets_path)
        # Only keep a small sample for testing
    except Exception as e:
        print(f"Data ingestion error: {e}")
        return None, None, None
    # Filter for relevant plays
    labels = labels[labels['game_play'].isin(game_plays)]
    tracking = tracking[tracking['game_play'].isin(game_plays)]
    helmets = helmets[helmets['game_play'].isin(game_plays)]
    return labels, tracking, helmets

# --- Microservice: Preprocessing ---
def preprocess_data(labels, tracking, helmets):
    # Convert object columns to appropriate types
    tracking = tracking.infer_objects()
    
    # Interpolate only numeric columns
    numeric_cols = tracking.select_dtypes(include=[np.number]).columns
    tracking[numeric_cols] = tracking[numeric_cols].interpolate(method='linear')
    
    # Ensure required columns exist
    for df in [labels, tracking, helmets]:
        for col in ['game_play', 'step', 'player_id']:
            if col not in df.columns:
                df[col] = np.nan  # Add placeholder if missing
    
    # Merge dataframes
    merged = pd.merge(labels, tracking, on=['game_play', 'step', 'player_id'], how='left')
    merged = pd.merge(merged, helmets, on=['game_play', 'step', 'player_id'], how='left')
    merged.fillna(0, inplace=True)  # Handle remaining NaNs
    return merged

# --- Microservice: Feature Extraction ---
def extract_features(data):
    features = []
    labels = []
    for _, group in data.groupby(['game_play', 'step']):
        # Check if required columns exist
        if 'contact' not in group.columns or 'x_position' not in group.columns:
            continue
        
        players = group[['x_position', 'y_position', 'speed']].values
        contact_labels = group['contact'].values
        
        if len(players) >= 2 and len(contact_labels) > 0:
            dist = np.linalg.norm(players[0, :2] - players[1, :2])
            rel_speed = abs(players[0, 2] - players[1, 2])
            features.append([dist, rel_speed])
            labels.append(contact_labels[0])  # Use first contact label
    
    X = np.array(features)
    y = np.array(labels)
    
    if X.size == 0 or y.size == 0:
        print("Warning: No features or labels extracted. Check game_plays for contact events.")
        return X, y  # Return empty arrays to handle gracefully
    
    return X, y

# --- Microservice: Model Training ---
def train_model(X, y):
    if len(X) < 2 or len(y) < 2:
        print("Warning: Insufficient data for training.")
        return 0.0, None  # Return default F1-score and no model
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, class_weight='balanced', random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    
    # Calculate F1-score with zero_division to avoid warnings
    f1 = f1_score(y_test, preds, zero_division=0)
    return f1, clf

# --- Simulation Controller ---
def run_simulation(labels_path, tracking_path, helmets_path, game_plays, noise_level=0.0, drop_rate=0.0, max_memory_gb=2):
    start_time = time.time()
    labels, tracking, helmets = ingest_data(labels_path, tracking_path, helmets_path, game_plays)
    if labels is None:
        print("Simulation aborted: Data ingestion failed.")
        return 0, 0, 0, 0

    # Simulate chaos: Drop rows, add noise
    if drop_rate > 0:
        tracking = tracking.sample(frac=1 - drop_rate, random_state=42)
    if 'x_position' in tracking.columns and 'y_position' in tracking.columns:
        tracking[['x_position', 'y_position']] += np.random.normal(0, noise_level, tracking[['x_position', 'y_position']].shape)

    data = preprocess_data(labels, tracking, helmets)
    X, y = extract_features(data)
    f1, clf = train_model(X, y)

    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().used / 1024**3
    if memory_usage > max_memory_gb:
        print("Simulation aborted: Memory limit exceeded.")
        return 0, time.time() - start_time, cpu_usage, memory_usage

    return f1, time.time() - start_time, cpu_usage, memory_usage

# --- Example Run ---
game_plays = ['58168_003392', '58172_003247']
f1, runtime, cpu, mem = run_simulation(
    'nfl-player-contact-detection/train_labels.csv',
    'nfl-player-contact-detection/train_player_tracking.csv',
    'nfl-player-contact-detection/train_baseline_helmets.csv',
    game_plays,
    noise_level=0.1,
    drop_rate=0.1,
    max_memory_gb=8  # or higher, depending on your system
)
print(f"F1-Score: {f1}, Runtime: {runtime:.2f}s, CPU: {cpu}%, Memory: {mem:.2f}GB")

# --- Example Run: Multiple Simulations ---
game_plays = ['58168_003392', '58172_003247']

for i in range(10):  # Run the simulation 10 times
    print(f"\n--- Simulation Run {i+1} ---")
    try:
        f1, runtime, cpu, mem = run_simulation(
            'nfl-player-contact-detection/train_labels.csv',
            'nfl-player-contact-detection/train_player_tracking.csv',
            'nfl-player-contact-detection/train_baseline_helmets.csv',
            game_plays,
            noise_level=0.1,
            drop_rate=0.1,
            max_memory_gb=8
        )
        print(f"F1-Score: {f1}, Runtime: {runtime:.2f}s, CPU: {cpu}%, Memory: {mem:.2f}GB")
    except Exception as e:
        print(f"Simulation failed with error: {e}")