# India Census Data Visualization and Analysis

## Project Overview

This project analyzes and visualizes Census of India 2011 data
using Python, Pandas, Matplotlib, Seaborn and Plotly.

## Objectives

- Analyze population distribution across Indian states
- Analyze literacy rates
- Study male and female population distribution
- Analyze sex ratio
- Study population-related patterns
- Create interactive visualizations
- Develop an interactive Plotly Dash dashboard

## Dataset

Source: Census of India 2011

Dataset: Primary Census Abstract (PCA)

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Dash
- Jupyter Notebook
- GitHub
- AI tools
## Features

- **Data Cleaning:** Loads and prepares Census 2011 data for analysis.
- **Exploratory Data Analysis:** Examines population, literacy, and sex ratio patterns across 35 states and union territories.
- **Population Analysis:** Identifies regions with the highest populations.
- **Literacy Analysis:** Compares calculated literacy rates across regions.
- **Sex Ratio Analysis:** Examines the female-to-male population ratio per 1,000 males.
- **Population Density Analysis:** Compares population density using population and reference area data.
- **Interactive Dashboard:** Displays key population statistics using Plotly Dash.
- **KPI Cards:** Shows total population, male population, female population, average calculated literacy rate, and average sex ratio.
- **Interactive Region Selection:** Allows users to select a state or union territory and view its statistics.
- **Interactive Charts:** Includes charts for population, calculated literacy rate, sex ratio, and population density.

## features
## Project Structure

```text
India-Census-Data_Visualization/
│
├── data/
│   ├── raw/
│   │   └── census_2011_raw.xlsx
│   └── cleaned/
│       ├── census_2011_cleaned.csv
│       └── census_dashboard_data.csv
│
├── notebooks/
│   └── census_analysis.ipynb
│
├── reports/
│   ├── charts/
│   ├── descriptive_statistics.csv
│   ├── population_analysis.csv
│   ├── child_population_analysis.csv
│   ├── population_ranking.csv
│   └── population_density_analysis.csv
|   |__ rural_urban_analysis.csv
|   |__ worker_population_analysis.csv
│
├── app.py
├── README.md
└── requirements.txt
```

### Folder Description

- **data/raw/** — Contains the original Census 2011 Excel dataset.
- **data/cleaned/** — Stores cleaned data and the dataset used by the dashboard.
- **notebooks/** — Contains the Jupyter Notebook used for data analysis.
- **reports/** — Stores analysis results and exported CSV files.
- **reports/charts/** — Contains charts generated during the analysis.
- **app.py** — Runs the interactive Plotly Dash dashboard.
- **requirements.txt** — Lists the Python packages required by the project.
- **README.md** — Documents the project and explains how to run it.

## Installation and Setup
## Analysis Results

The project analyzes Census of India 2011 data across 35 states and union territories.

Key findings from the cleaned dataset include:

- **Total population:** 1,210,854,977
- **Male population:** 623,270,258
- **Female population:** 587,584,719
- **Average calculated literacy rate across 35 regions:** 67.76%
- **Average sex ratio across 35 regions:** 931.06 females per 1,000 males

Additional observations:

- Uttar Pradesh has the largest population among the regions in the dataset.
- Kerala has the highest calculated literacy rate in the analysis.
- Kerala has the highest sex ratio in the analysis.
- The National Capital Territory of Delhi has the highest calculated population density.
- Arunachal Pradesh has the lowest calculated population density.

## Limitations

- The analysis uses Census of India 2011 data and does not represent current population figures.
- The calculated literacy rate is derived from the literacy and illiteracy columns in the dataset. It should not automatically be treated as the official published literacy rate.
- The average literacy rate and average sex ratio reported above are simple averages across 35 regions, not population-weighted national statistics.
- Population density depends on the reference area values used. Historical boundary changes may affect comparisons between regions.
- The results depend on the quality and consistency of the source dataset and the data-cleaning process.


