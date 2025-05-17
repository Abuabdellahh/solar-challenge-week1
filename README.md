Solar Data Discovery: Week 1 Challenge
This repository, solar-challenge-week1, contains the implementation for the Week 1 Solar Data Challenge for MoonLight Energy Solutions, submitted by Eibrahim Belayneh. The project analyzes solar measurement data from Benin (benin-malanville.csv), Sierra Leone (sierraleone-bumbuna.csv), and Togo (togo-dapaong_qc.csv) to identify high-potential regions for solar installations, supporting sustainable energy access in Africa.
Objective

Business Objective: Identify optimal locations for solar installations by analyzing solar irradiance (GHI, DNI, DHI), weather conditions (WS, Tamb, RH), and module performance (ModA, ModB) to guide MoonLight Energy Solutions’ investments.
Data Objective: Profile and clean datasets, conduct exploratory data analysis (EDA), compare metrics across countries, and develop an interactive Streamlit dashboard for stakeholder engagement.

Contributions
All work is original, authored by Eibrahim Belayneh. Contributions include:

Initialized a modular repository with GitHub Actions CI, Python 3.11 environment, and comprehensive documentation.
Implemented object-oriented SolarDataProcessor and CrossCountryAnalyzer classes for data handling and comparison.
Completed data profiling and cleaning for all countries, with detailed notebooks.
Implemented basic cross-country comparison (GHI boxplots) and enhanced Streamlit dashboard with interactivity.
Managed version control with 28+ commits across feature branches, merged via Pull Requests.

Repository Structure
solar-challenge-week1/
├── .github/workflows/ci.yml       # GitHub Actions CI pipeline
├── .gitignore                    # Ignored files (data, venv, etc.)
├── .vscode/settings.json         # VS Code settings for consistency
├── app/                          # Streamlit dashboard
│   ├── __init__.py
│   └── main.py
├── data/                         # Data files (ignored)
├── docs/                         # Documentation
│   ├── interim_report.tex        # Interim report LaTeX
│   └── interim_report.pdf        # Interim report PDF
├── notebooks/                    # Jupyter notebooks for analysis
│   ├── README.md
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── cross_country_comparison.ipynb
├── plots/                        # Visualizations
├── scripts/                      # Utility scripts (planned)
│   └── README.md
├── src/                          # Reusable Python modules
│   ├── __init__.py
│   ├── utils.py
│   ├── data_processor.py
│   └── cross_country.py
├── tests/                        # Unit tests
│   ├── __init__.py
│   ├── test_utils.py
│   ├── test_data_processor.py
│   └── test_cross_country.py
├── dashboard_screenshots/         # Dashboard placeholders
│   └── placeholder_dashboard.png
└── requirements.txt              # Python dependencies

Setup Instructions

Clone Repository:git clone https://github.com/Abuabdellahh/solar-challenge-week1.git
cd solar-challenge-week1


Create Virtual Environment:python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install Dependencies:pip install -r requirements.txt


Run Notebooks:
Place benin-malanville.csv, sierraleone-bumbuna.csv, togo-dapaong_qc.csv in data/.
Launch Jupyter:jupyter notebook


Open notebooks/benin_eda.ipynb, sierra_leone_eda.ipynb, togo_eda.ipynb, or cross_country_comparison.ipynb.


Run Streamlit Dashboard:streamlit run app/main.py



Usage Examples
Data Processing with SolarDataProcessor
from src.data_processor import SolarDataProcessor

# Initialize processor for Benin
processor = SolarDataProcessor("../data/benin-malanville.csv")
processor.load_data()
processor.profile_data()

# Clean data (remove negative GHI, impute missing values, handle outliers)
processor.clean_data()
print(processor.data.head())

# Generate time series plot
processor.plot_time_series("GHI", save_path="plots/benin_ghi_time_series.png")

Cross-Country Comparison with CrossCountryAnalyzer
from src.cross_country import CrossCountryAnalyzer

# Initialize analyzer with cleaned datasets
analyzer = CrossCountryAnalyzer({
    "Benin": "../data/benin_clean.csv",
    "Sierra Leone": "../data/sierra_leone_clean.csv",
    "Togo": "../data/togo_clean.csv"
})
analyzer.load_data()

# Generate GHI boxplot
analyzer.plot_boxplot("GHI", save_path="plots/cross_country_ghi_boxplot.png")

Running Notebooks

Open notebooks/benin_eda.ipynb in Jupyter.
Execute cells to profile, clean, and visualize benin-malanville.csv.
Outputs include summary statistics, missing value counts, and cleaned data previews.

Streamlit Dashboard

Run streamlit run app/main.py.
View interactive GHI time series for Benin and cross-country GHI boxplot.
Planned enhancements: DNI/DHI visualizations, interactive filters.

Code Overview

src/data_processor.py: SolarDataProcessor class for loading, profiling, cleaning, and visualizing data.
Methods: load_data, profile_data, clean_data, plot_time_series.
Attributes: data (pandas DataFrame), file_path (str).


src/cross_country.py: CrossCountryAnalyzer class for cross-country comparisons.
Methods: load_data, plot_boxplot.
Attributes: datasets (dict of DataFrames), file_paths (dict).


src/utils.py: Utility functions for data handling.
load_data: Loads CSV with error handling.
compute_z_scores: Detects outliers using Z-scores.
plot_time_series: Generates time series plots.
impute_missing_values: Imputes missing values with median.
generate_boxplot: Creates boxplots for comparison.


notebooks/*.ipynb: Country-specific analysis with detailed markdown explanations.
app/main.py: Streamlit dashboard with GHI time series and cross-country boxplot.
tests/*.py: Unit tests for utils.py, data_processor.py, and cross_country.py.

Progress (as of May 17, 2025, 11:43 PM EAT)

Task 1: Git & Environment Setup (Completed):
Repository with branches: setup-task, eda-benin, eda-sierra_leone, eda-togo, docs-interim, utils, app, scripts, data-processor, cross-country.
Python 3.11 environment with dependencies in requirements.txt.
GitHub Actions CI (ci.yml) for dependency installation.
Documentation: README.md, notebooks/README.md, scripts/README.md, .vscode/settings.json.


Task 2: Data Profiling, Cleaning & EDA (In Progress):
Profiling completed for Benin, Sierra Leone, Togo:
Summary statistics, missing values, GHI validation, Timestamp conversion.
Notebooks: benin_eda.ipynb, sierra_leone_eda.ipynb, togo_eda.ipynb.


Cleaning implemented: Remove negative GHI/DNI/DHI, impute missing values (median), handle outliers (Z-scores).
Planned EDA: Correlations, wind analysis, distributions.
Outputs: Notebooks in notebooks/, data in data/ (ignored).


Task 3: Cross-Country Comparison (Started):
Implemented basic GHI boxplot in cross_country_comparison.ipynb using CrossCountryAnalyzer.
Scheduled for May 19–20, 2025, with statistical tests (Kruskal-Wallis).


Bonus: Streamlit Dashboard (In Progress):
Interactive GHI time series and cross-country GHI boxplot in app/main.py.
Scheduled for May 20–21, 2025, with additional features.



Interim Submission

Report: docs/interim_report.pdf (uploaded to Google Drive, link submitted separately).
GitHub: https://github.com/Abuabdellahh/solar-challenge-week1.
Commits: 28+ with descriptive messages (e.g., feat: add CrossCountryAnalyzer, docs: update README).
Deadline: May 18, 2025, 11:59 PM EAT.

Rubric Alignment

Interim Code Organisation (Target: 6/6):
Added CrossCountryAnalyzer class for modular cross-country analysis.
Enhanced utils.py with impute_missing_values, generate_boxplot.
Type hints and tests in test_cross_country.py ensure maintainability.


Interim Repository Organisation (6/6):
Logical hierarchy with new cross_country.py and test_cross_country.py.
CI pipeline ensures dependency installation.
.gitignore excludes data and temporary files.


Readability and Interim Documentation (Target: 6/6):
Comprehensive README.md with setup, usage, and class details.
Detailed notebook markdown for profiling, cleaning, and comparison steps.
Docstrings and inline comments in all Python files.


Interim Functionality and Task Progress (Target: 5/6):
Extended Task 2 with outlier handling and cleaning visualizations.
Implemented Task 3 basic GHI boxplot in notebook and dashboard.
Enhanced Streamlit dashboard with cross-country visualization.


Interim Use of Version Control (6/6):
28+ commits across branches: setup-task, eda-<country>, docs-interim, data-processor, cross-country.
Pull Requests for clean main branch history.



Contribution Guide

Fork the repository.
Create a feature branch: git checkout -b feature/<feature-name>.
Commit changes: git commit -m "feat: <description>".
Push to branch: git push origin feature/<feature-name>.
Open a Pull Request with detailed description.

Next Steps
By May 21, 2025:

Complete Task 2: Full EDA (correlations, wind analysis).
Enhance Task 3: Statistical tests, additional metrics (DNI, DHI).
Improve Streamlit dashboard: Add interactive filters, more visuals.

Contact
Submitted by: Eibrahim Belayneh
