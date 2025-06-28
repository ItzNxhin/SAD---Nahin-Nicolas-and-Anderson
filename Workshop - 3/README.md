# NFL Player Contact Detection Simulation (Workshop 3)

This folder contains the code and report for the NFL Player Contact Detection simulation, developed as part of Workshop 3 for the course "Análisis y Diseño de Sistemas".

## Summary

This simulation demonstrates a modular, lightweight approach to NFL player contact detection using Python (Pandas, NumPy, Scikit-learn). The pipeline includes data ingestion, preprocessing, feature extraction, model training, and chaos engineering (random noise, data loss, etc.) to test robustness under uncertain inputs. The approach is designed to run efficiently on hardware with limited resources (e.g., 8GB RAM, no GPU).

## Simulation Approach

- **Data Preparation:**  
  Loads and filters the official NFL competition CSVs (`train_labels.csv`, `train_player_tracking.csv`, `train_baseline_helmets.csv`) for a subset of game plays.
- **Preprocessing:**  
  Cleans and synchronizes data, interpolates missing values, and merges relevant features.
- **Feature Extraction:**  
  Computes features such as player distances and relative speeds for each play and step.
- **Model Training:**  
  Trains a RandomForest classifier to predict player contact events, using class weights to address data imbalance.
- **Chaos Engineering:**  
  Introduces random events (noise, data loss, memory spikes, etc.) to simulate real-world uncertainty and test system resilience.
- **Evaluation:**  
  Reports F1-score, runtime, CPU, and memory usage for each simulation run.

## How to Run

1. Clone the repository and navigate to the `Workshop 3` folder.
2. Ensure you have the required Python packages:  
   `pandas`, `numpy`, `scikit-learn`, `psutil`
3. Place the required CSV files in the appropriate directory.
4. Run the main simulation script (`workshop.py`).  
   You can run multiple simulations to observe the effects of chaos events.

## Results

- The simulation achieves a baseline F1-score (e.g., ~0.15 with minimal features and imbalanced data).
- Chaos events can trigger errors or degrade performance, demonstrating the importance of robust system design.
- The pipeline is efficient and modular, suitable for further extension or deployment.

## Report

- **Full Simulation Report (PDF):**  
  [NFL Contact Detection Simulation Report.pdf](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop%20-%203/Simulation%20Report.pdf)
- **Markdown Source:**  
  [NFL Contact Detection Simulation Report.markdown](./NFL%20Contact%20Detection%20Simulation%20Report.markdown)

