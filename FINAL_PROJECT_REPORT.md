# India Census Data Visualization and Analysis Using Python

## 1. Introduction

This project focuses on analyzing and visualizing Census of India 2011 data using Python. The project applies data cleaning, exploratory data analysis, statistical summaries, and data visualization to understand population and demographic patterns across Indian states and union territories.

An interactive dashboard was developed using Plotly Dash to make the results easier to explore.

## 2. Objectives

- Analyze population distribution across states and union territories.
- Compare male and female population figures.
- Examine literacy rates and sex ratios.
- Analyze population density across regions.
- Perform data cleaning and exploratory data analysis.
- Create visualizations and an interactive dashboard.

## 3. Dataset Description

The project uses the Primary Census Abstract (PCA) dataset from the Census of India 2011.

The original Excel dataset contains 2,028 rows and 94 columns. The cleaned regional dataset contains 35 records and 96 columns. A separate dashboard dataset contains 35 records and 98 columns.

The data includes population, male and female population, child population, literacy, worker population, and related demographic indicators.

## 4. Tools and Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Plotly and Dash
- Jupyter Notebook
- VS Code
- Git and GitHub

## 5. Methodology

### Data Loading and Cleaning

The original Excel dataset was loaded and examined. Relevant state and union territory total records were selected and prepared for analysis.

### Exploratory Data Analysis

The cleaned data was examined for missing values, duplicate records, and demographic patterns.

### Feature Calculation

Additional indicators, including calculated literacy rate, sex ratio, and population density, were prepared for analysis.

### Data Visualization

Charts were created to compare population, literacy rate, sex ratio, child population, worker population, and population density.

### Dashboard Development

A Plotly Dash application was developed with KPI cards, interactive charts, and a state/UT dropdown that displays selected-region statistics.

## 6. Key Results

The cleaned dataset produced the following results:

- Total population across the 35 regional records: 1,210,854,977
- Male population: 623,270,258
- Female population: 587,584,719
- Simple average of calculated literacy rates across regions: 67.76%
- Simple average sex ratio across regions: 931.06 females per 1,000 males

Uttar Pradesh had the largest population in the analyzed dataset. Kerala had the highest calculated literacy rate and sex ratio in the analysis. The National Capital Territory of Delhi had the highest calculated population density, while Arunachal Pradesh had the lowest.

## 7. Dashboard Features

- KPI cards for population and demographic indicators.
- Population comparison chart.
- Calculated literacy-rate comparison chart.
- Sex-ratio comparison chart.
- Population-density comparison chart.
- Interactive state/UT selection.
- Selected-region demographic statistics.

## 8. Testing and Validation

The dashboard was tested by selecting different regions, checking the displayed population figures, verifying chart rankings, and refreshing the browser.

The final validation reported 35 regional records, no missing values in the checked key columns, and no duplicate region names. The dashboard was tested without errors during the reported functional checks.

## 9. Limitations

- The project uses Census 2011 data and does not represent current population figures.
- Calculated literacy rates should not automatically be treated as official published literacy rates.
- Regional averages are simple unweighted averages, not population-weighted national statistics.
- Population-density comparisons depend on the reference area values and may be affected by historical boundary changes.

## 10. Conclusion

This project demonstrates how Python libraries can be used to clean, analyze, and visualize demographic data. The interactive dashboard makes it easier to compare regional population patterns and explore demographic indicators.

The project provided practical experience in data preprocessing, exploratory data analysis, visualization, dashboard development, and project documentation.

## 11. Screenshots

Dashboard screenshots are stored in the `screenshots/` directory.

## 12. Data Source

Census of India 2011 — Primary Census Abstract (PCA).
