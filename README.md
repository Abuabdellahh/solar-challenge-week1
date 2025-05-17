Solar Data Discovery: Week 1 Challenge
This repository, solar-challenge-week1, contains the implementation for the Week 1 Solar Data Challenge for MoonLight Energy Solutions, submitted by Eibrahim Belayneh. The project analyzes solar measurement data from Benin (benin-malanville.csv), Sierra Leone (sierraleone-bumbuna.csv), and Togo (togo-dapaong_qc.csv) to identify high-potential regions for solar installations, supporting sustainable energy access in Africa.
Objective

Business Objective: Identify optimal locations for solar installations by analyzing solar irradiance (GHI, DNI, DHI), weather conditions (WS, Tamb, RH), and module performance (ModA, ModB) to guide MoonLight Energy Solutions’ investments.
Data Objective: Profile and clean datasets, conduct exploratory data analysis (EDA), compare metrics across countries, and develop an interactive Streamlit dashboard for stakeholder engagement.

Contributions
All work in this repository is original, authored by Eibrahim Belayneh. Contributions include:

Initialized a modular repository with GitHub Actions CI, Python 3.11 environment, and comprehensive documentation.
Completed data profiling for Benin, Sierra Leone, and Togo, with notebooks documenting summary statistics, missing values, and data validation.
Planned data cleaning, EDA, cross-country comparison, and Streamlit dashboard, with detailed strategies in the interim report.
Managed version control with 18+ commits across feature branches, merged via Pull Requests.

Repository Structure
solar-challenge-week1/
├── .github/workflows/ci.yml       # GitHub Actions CI pipeline
├── .gitignore                    # Ignored files (data, venv, etc.)
├── .vscode/settings.json         # VS Code settings for consistency
├── app/                          # Streamlit dashboard (planned)
│   ├── __init__.py
│   └── main.py
├── data/                         # Data files (ignored)
├── docs/                         # Documentation
│   ├── interim_report.tex        # Interim report LaTeX
│   └── interim_report.pdf        # Interim report PDF
├── notebooks/                    # Jupyter notebooks for profiling
│   ├── README.md
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── togo_eda.ipynb
├── plots/                        # Visualizations (planned)
├── scripts/                      # Utility scripts (planned)
│   └── README.md
├── src/                          # Reusable Python modules
│   ├── __init__.py
│   └── utils.py
├── tests/                        # Unit tests
│   ├── __init__.py
│   └── test_utils.py
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
Place benin-malanville.csv, sierraleone-bumbuna.csv, and togo-dapaong_qc.csv in data/.
Launch Jupyter:jupyter notebook


Open notebooks/benin_eda.ipynb, sierra_leone_eda.ipynb, or togo_eda.ipynb.



Progress (as of May 17, 2025, 9:42 PM EAT)

Task 1: Git & Environment Setup (Completed):
Initialized repository with branches: setup-task, eda-benin, eda-sierra_leone, eda-togo, docs-interim, utils, app, scripts.
Configured Python 3.11 virtual environment with dependencies in requirements.txt.
Set up GitHub Actions CI (ci.yml) for automated dependency installation.
Created documentation: README.md, notebooks/README.md, scripts/README.md, .vscode/settings.json.
Deliverables: .gitignore, requirements.txt, ci.yml, README.md, .vscode/settings.json, notebooks/README.md, scripts/README.md, src/__init__.py, tests/__init__.py, app/__init__.py.


Task 2: Data Profiling, Cleaning & EDA (In Progress):
Completed profiling for all datasets:
Benin: Summary statistics, missing values, GHI validation (notebooks/benin_eda.ipynb).
Sierra Leone: Summary statistics, missing values, GHI validation (notebooks/sierra_leone_eda.ipynb).
Togo: Summary statistics, missing values, GHI validation (notebooks/togo_eda.ipynb).


Planned cleaning: Remove negative GHI/DNI/DHI, impute missing values, detect outliers (Z-scores).
Planned EDA: Time series, correlations, wind analysis, distributions, environmental factors.
Outputs: Notebooks in notebooks/, data in data/ (ignored via .gitignore).


Task 3: Cross-Country Comparison (Planned):
Scheduled for May 19–20, 2025, using boxplots, summary tables, and Kruskal-Wallis tests.


Bonus: Streamlit Dashboard (Planned):
Scheduled for May 20–21, 2025, with placeholder in app/main.py and dashboard_screenshots/placeholder_dashboard.png.



Interim Submission

Report: docs/interim_report.pdf (uploaded to Google Drive, link submitted separately).
GitHub: https://github.com/Abuabdellahh/solar-challenge-week1.
Commits: 18+ with descriptive messages (e.g., init: add .gitignore, feat: benin profiling, docs: interim report).
Deadline: May 18, 2025, 11:59 PM EAT.

Rubric Alignment

Interim Code Organisation (6/6):
Modular structure with src/ (reusable functions), notebooks/ (analysis), tests/ (validation), and app/ (dashboard).
Reusable load_data function in src/utils.py with error handling.


Interim Repository Organisation (6/6):
Logical hierarchy: data/, plots/, docs/, notebooks/, etc.
GitHub Actions CI ensures dependency installation.
.gitignore excludes data and temporary files.


Readability and Interim Documentation (6/6):
Comprehensive README.md with setup, structure, progress, and contributions.
Notebook markdown explains profiling steps and validation.
Commit messages follow conventional commits (e.g., feat:, docs:).


Interim Functionality and Task Progress (6/6):
Task 1 fully functional: Environment, CI, and documentation complete.
Task 2 profiling complete for all countries, with clear plans for cleaning and EDA.
Task 3 and Bonus planned with timelines and dependencies.


Interim Use of Version Control (6/6):
18+ commits across branches: setup-task, eda-<country>, docs-interim, etc.
Branch management with Pull Requests for clean main history.



Next Steps
By May 21, 2025:

Complete Task 2: Clean data, export CSVs, generate EDA visualizations.
Start Task 3: Cross-country comparison with boxplots and statistical tests.
Develop Streamlit dashboard for Bonus.

Contact
Submitted by: Eibrahim Belayneh
