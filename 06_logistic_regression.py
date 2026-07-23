"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 6: Logistic Regression — Predicting Brand Awareness (Section 9).
Requires df2_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
import statsmodels.api as sm

df2 = pd.read_pickle("df2_clean.pkl")

df2_model = df2.copy()
df2_model["awareness_bin"] = (df2_model["outlook_awareness"] == "Yes").astype(int)

logit_df = pd.get_dummies(
    df2_model[["awareness_bin", "brand_awareness_influencer",
               "digital_monthly_spend", "campaign_frequency",
               "outlook_familiarity_score"]],
    columns=["brand_awareness_influencer", "digital_monthly_spend", "campaign_frequency"],
    drop_first=True
)
logit_df = logit_df.astype({c: "int" for c in logit_df.columns if logit_df[c].dtype == bool})

X_logit = sm.add_constant(logit_df.drop(columns=["awareness_bin"]))
y_logit = logit_df["awareness_bin"]

logit_model = sm.Logit(y_logit, X_logit.astype(float)).fit()
print(logit_model.summary())

# Key stats used in report:
# logit_model.prsquared (Pseudo R-squared)
# logit_model.llr_pvalue (Log-Likelihood Ratio p-value)
