# Student Marks Analysis System 

A simple data analysis project built with Python to analyze student academic performance using NumPy and Pandas.

## 📌 Project Summary

This project demonstrates basic data manipulation and analysis techniques on student performance data. It processes raw numerical data into a structured format and calculates key performance metrices for each student.

## 🎯 What I Learned & Researched

Through this project, I explored and applied several core Data Science concepts:

- **2D Array Manipulation:** Creating and structuring multi-dimensional numerical arrays using `numpy.array()`.
- **Pandas DataFrames:** Converting raw NumPy arrays into labeled DataFrames using custom indices (Student IDs) and column headers (Subjects).
- **Understanding Axis Differences:** Learning the distinction between `axis=0` (column-wise operations across all students) and `axis=1` (row-wise operations per student).
- **Aggregations in Data Analysis:** Utilizing native Pandas functions like `.sum()`, `.mean()`, and `.max()` to extract statistical summary metrics.
- **Index Identification:** Using `.idxmax()` to dynamically find the column name (subject) corresponding to the highest score in a row.

## 🔑 Key Features

- **Structured Data Representation:** Converts a 2D matrix into a clean Pandas DataFrame with custom student IDs and subject names.
- **Performance Metrics:** Automatically calculates the total score and average mark for each student.
- **Top Subject Identification:** Identifies the specific subject in which a student scored the highest.
- **Highest Mark Extraction:** Determines each student's peak score across all subjects.

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical operations
