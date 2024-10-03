# DataFrame Class: Analyzing and Visualing Student Scores
Overview

This Python project is designed to manage and analyze student score data using pandas. The class DataFrame reads student data from a CSV file, processes the data, and provides methods to analyze it. Key functionalities include finding students who failed in any subject, calculating the average scores per semester, determining the student with the highest average score, identifying the hardest subject, and creating new reports in Excel format. The Visualization class provides simple yet effective ways to visualize student score data using matplotlib.


## Features

- Simulates a many-to-many relationship between authors and books.
- Generates random data for 500 authors and 1000 books using the Faker library.
- Ensures that some authors have no books.



## Dataset
The dataset should be a CSV file named student_scores_random_names.csv. The file is expected to contain:

- A Semester column that identifies the semester of the student's performance.
- A Student column with student names.
- Columns for subjects such as "Math", "Physics", "Chemistry", "Biology", and "English", containing the scores for each subject.


## Requirements 
To run the project, you need to have the following libraries installed:

 - pandas: For data manipulation and analysis
- openpyxl: For writing Excel files (optional, used for saving data to Excel)
- matplotlib: For creating plots