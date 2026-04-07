# Menstrual Cycle Dataset

## Description
This dataset contains synthetic menstrual cycle data for 100 users. It includes features such as age, BMI, stress levels, exercise frequency, sleep patterns, dietary habits, and menstrual cycle details. The dataset is designed for analyzing factors affecting menstrual health and building predictive models for the next menstrual cycle.

## Dataset Overview
- **Number of Users**: 100
- **Number of Records**: Varies per user (6-12 cycles per user)
- **File Format**: CSV
- **File Name**: `menstrual_cycle_data.csv`

## Columns
| Column Name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `User ID`             | Unique identifier for each user.                                            |
| `Age`                 | Age of the user (in years).                                                 |
| `BMI`                 | Body Mass Index of the user.                                                |
| `Stress Level`        | Self-reported stress level (scale: 1-5, where 1 = low, 5 = high).          |
| `Exercise Frequency`  | Frequency of exercise (options: Low, Moderate, High).                      |
| `Sleep Hours`         | Average hours of sleep per night.                                           |
| `Diet`                | Dietary habits (options: Balanced, Vegetarian, High Sugar, Low Carb).       |
| `Cycle Start Date`    | Start date of the menstrual cycle.                                          |
| `Cycle Length`        | Length of the menstrual cycle (in days).                                    |
| `Period Length`       | Duration of the period (in days).                                           |
| `Next Cycle Start Date` | Start date of the next menstrual cycle (target variable for prediction).  |
| `Symptoms`            | Common menstrual symptoms (options: Cramps, Mood Swings, Fatigue, Headache, Bloating). |

## Example Data
Here’s an example of what the dataset looks like:

| User ID | Age | BMI  | Stress Level | Exercise Frequency | Sleep Hours | Diet       | Cycle Start Date | Cycle Length | Period Length | Next Cycle Start Date | Symptoms     |
|---------|-----|------|--------------|--------------------|-------------|------------|------------------|--------------|---------------|-----------------------|--------------|
| 1       | 28  | 24.3 | 3            | Moderate           | 7.2         | Balanced   | 2023-01-15      | 28           | 5             | 2023-02-12           | Cramps       |
| 1       | 28  | 24.3 | 3            | Moderate           | 7.2         | Balanced   | 2023-