"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 9: Pivot-table cross-tabulations (PT1-PT3), re-verified with chi-square
(Section 12). These pivots were originally built in Excel; this script
reproduces and statistically validates them in Python.
"""

import pandas as pd
from scipy import stats

df_raw = pd.read_excel("Outlook_Consumer_Survey.xlsx", sheet_name="Sheet1")
df1 = pd.read_pickle("df1_clean.pkl")

# -------------------------------------------------------------------------
# PT1 — Repurchase Intent x Pricing Satisfaction
# -------------------------------------------------------------------------
ct_pt1 = pd.crosstab(df1["repurchase_intent"], df_raw["pricing_satisfaction"])
chi2_pt1, p_pt1, dof_pt1, _ = stats.chi2_contingency(ct_pt1)
print("PT1 crosstab:\n", ct_pt1)
print(f"PT1 chi2={chi2_pt1:.3f}, df={dof_pt1}, p={p_pt1:.3f}")

# -------------------------------------------------------------------------
# PT2 — Repurchase Intent x Recommend Likelihood
# (correcting mixed text/numeric "5" data artifact)
# -------------------------------------------------------------------------
recommend_fixed = pd.to_numeric(
    df_raw["recommend_likelihood"].astype(str).str.strip(), errors="coerce"
).round().astype("Int64")
ct_pt2 = pd.crosstab(df1["repurchase_intent"], recommend_fixed)
chi2_pt2, p_pt2, dof_pt2, _ = stats.chi2_contingency(ct_pt2)
print("\nPT2 crosstab:\n", ct_pt2)
print(f"PT2 chi2={chi2_pt2:.3f}, df={dof_pt2}, p={p_pt2:.3f}")

# -------------------------------------------------------------------------
# PT3 — Most Valued Outlook Quality
# -------------------------------------------------------------------------
pt3_counts = df_raw["top_qualities_outlook"].value_counts()
pt3_share = df_raw["top_qualities_outlook"].value_counts(normalize=True) * 100
print("\nPT3 counts:\n", pt3_counts)
print("PT3 share (%):\n", pt3_share.round(1))
