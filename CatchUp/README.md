# Kaggle Player Contact Detection - Catch-Up Summary

## Project Overview

This repository documents the progress and analysis of our system designed for detecting player contacts in NFL games. The work integrates data from the Kaggle competition on player contact detection, employing video and sensor data to improve accuracy and reliability in contact identification.

Our primary focus was on developing a CPU-efficient, modular system leveraging state-of-the-art machine learning and computer vision techniques. The solution prioritizes scalability and adaptability to real-game conditions while addressing hardware constraints and data challenges.

---

## Catch-Up Contents

### Workshop Development

1. **Report**  
   A comprehensive report detailing the analysis and design approach.  
   [View Report](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/CatchUp/Detection%20of%20Player%20Report.pdf)

2. **Paper**  
   A formal paper summarizing the research and findings.  
   [View Paper](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/CatchUp/Paper.pdf)

3. **Poster**  
   A visual presentation of the system’s analysis and design.  
   [View Poster](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/CatchUp/Poster%20Analisis%20de%20sistemas.pdf)

4. **Workshop 2 Diagram**  
   A visual representation of the system architecture.  
   [View Diagram](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/CatchUp/Workshop2_diagram.png)

---

## Reference Materials

- **Workshop 1:** [Initial analysis and context](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/tree/main/Workshop1%20-%20Kaggle)  
- **Workshop 2 Design:** [PDF Report](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop_2_Design/Workshop_2_report.pdf) | [Diagram](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop_2_Design/Workshop2_diagram.png)  
- **Kaggle Competition:** [NFL Player Contact Detection](https://www.kaggle.com/competitions/nfl-player-contact-detection)  
- **Competition Winner Repository:** [1st Place Solution](https://github.com/nvnnghia/1st_place_kaggle_player_contact_detection)  
- **Additional Context:** [NFL Player Health & Safety](https://www.nfl.com/playerhealthandsafety/)  
- **System Design Tool:** [Diagrams.net](https://app.diagrams.net/)  

---

## Key Insights from Workshops

1. **System Design:**  
   Initial diagrams clarified system behavior and scope, focusing on modularity and removing redundant components for efficiency.

2. **Technological Stack:**  
   Selected lightweight tools such as MobileNet SSD (object detection), OpenCV (video tracking), and RandomForest (contact classification) to meet hardware constraints.

3. **Challenges Identified:**  
   - Data imbalance and synchronization issues between video and sensor data.  
   - Video occlusions and real-game variability.  
   - Hardware limitations (e.g., GPU, RAM).  

4. **Mitigation Strategies:**  
   - Modular architecture using patterns like Factory and Observer.  
   - Emphasized system maintainability and interpretability.  
   - Basic monitoring routines to track and mitigate vulnerabilities.  

5. **Collaboration:**  
   Division of responsibilities enhanced productivity, with regular review sessions aligning the team on terminology and design choices.

---

## Summary

This repository serves as a central resource for understanding the development and progress of our system for NFL player contact detection. By analyzing existing solutions and refining our approach, we aim to build a scalable, efficient, and practical system tailored to sports analytics.
