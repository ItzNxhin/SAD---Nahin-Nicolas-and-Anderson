## Kaggle Systems Design

https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop_2_Design/Workshop_2.pdf

## Kaggle Competetion 

https://www.kaggle.com/competitions/nfl-player-contact-detection

## Aditional Sources

- Workshop 1: https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/tree/main/Workshop1%20-%20Kaggle
- Diagram with draw.io: https://app.diagrams.net/
- Additional context: https://www.nfl.com/playerhealthandsafety/
- Competion Winner repository: https://github.com/nvnnghia/1st_place_kaggle_player_contact_detection

## Workshop development

- [PDF Report](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop_2_Design/Workshop_2_report.pdf)
- [Workshop - 2 - Diagram](https://github.com/ItzNxhin/SAD---Nahin-Nicolas-and-Anderson/blob/main/Workshop_2_Design/Workshop2_diagram.png)

## Summary

Our analysis began with a detailed review of the main problem: tracking player contacts using sensor and video data. We started by identifying key system behaviors and terms, which allowed us to construct an initial diagram as a visual foundation for our work. This helped clarify the project’s scope and allowed the team to stay focused on what was most relevant.

We studied how the system would operate under real conditions, and through team discussions, we refined the system by removing redundant or unnecessary components. We prioritized elements that contributed directly to contact detection and real-time processing.

A major reference point for us was the winning solution of the Kaggle competition. We analyzed their approach carefully and selected technologies that would work within our constraints—especially hardware limitations. This meant using lightweight, CPU-friendly tools like MobileNet SSD for object detection, OpenCV for video tracking, and RandomForest from Scikit-learn for contact classification. We also relied on Jupyter notebooks for step-by-step execution, which made collaboration and testing easier.

The analysis also included identifying system vulnerabilities—such as data imbalance, video occlusions, and synchronization issues between sensor and video data. These were flagged as critical areas for attention. To address them, we integrated basic monitoring routines, ensured modularity through design patterns like Factory and Observer, and emphasized interpretability and maintainability.

Throughout, we divided responsibilities among team members, leveraging individual strengths. Final review sessions helped us align terminology, validate our design choices, and ensure that the documentation reflected both the functional system and the reasoning behind our decisions.
