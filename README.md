# Case Studies — Python Computation Code

Submission by Geetarth (2023UEA6641)
Netaji Subhash University of Technology

This folder contains the Python code used for the statistical computations
in both case studies. Excel pivot tables and Power BI were used to build and
share the original pivot views and dashboards; these scripts reproduce and
statistically validate that same analysis in Python.

## Setup

```
pip install -r requirements.txt
```

Place `Outlook_Consumer_Survey.xlsx` (Sheet1, 92 columns x 11,109 rows) in
this folder before running any scripts.

## Folder structure

```
case_studies_code/
├── requirements.txt
├── README.md
├── case_study_1/   Customer Loyalty & Response Analysis
│   ├── 01_data_cleaning.py
│   ├── 02_descriptive_statistics.py
│   ├── 03_reliability_cronbach_alpha.py
│   ├── 04_correlation_analysis.py
│   ├── 05_anova_repurchase_intent.py
│   ├── 06_nps_dashboard.py
│   ├── 07_chisquare_nps_vs_repurchase.py
│   ├── 08_regression_analysis.py
│   └── 09_pivot_crosstabs.py
└── case_study_2/   Brand Awareness & Digital Marketing Effectiveness
    ├── 01_data_cleaning.py
    ├── 02_descriptive_profile.py
    ├── 03_reliability_test_retest.py
    ├── 04_chisquare_awareness_vs_marketing.py
    ├── 05_ttest_familiarity_by_awareness.py
    ├── 06_logistic_regression.py
    └── 07_pivot_crosstabs.py
```

## Run order

Each numbered script depends on the pickle file(s) saved by the earlier
script(s) in the same case study folder, so run them in numeric order from
inside each case_study folder, e.g.:

```
cd case_study_1
python 01_data_cleaning.py
python 02_descriptive_statistics.py
python 03_reliability_cronbach_alpha.py
python 04_correlation_analysis.py
python 05_anova_repurchase_intent.py
python 06_nps_dashboard.py
python 07_chisquare_nps_vs_repurchase.py
python 08_regression_analysis.py
python 09_pivot_crosstabs.py
```

```
cd ../case_study_2
python 01_data_cleaning.py
python 02_descriptive_profile.py
python 03_reliability_test_retest.py
python 04_chisquare_awareness_vs_marketing.py
python 05_ttest_familiarity_by_awareness.py
python 06_logistic_regression.py
python 07_pivot_crosstabs.py
```

Note: `01_data_cleaning.py` in each folder expects
`Outlook_Consumer_Survey.xlsx` to be in that same working directory (or
update the path in the script).
