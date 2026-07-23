"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 1: Load data and clean it (Section 4).
"""

import pandas as pd

df_raw = pd.read_excel("Outlook_Consumer_Survey.xlsx", sheet_name="Sheet1")

cs2_cols = [
    "outlook_awareness", "outlook_awareness_repeat", "brand_awareness_influencer",
    "brand_discovery_method", "digital_ad_platform", "campaign_frequency",
    "digital_buy_frequency", "digital_monthly_spend", "outlook_familiarity_score"
]
df2 = df_raw[cs2_cols].copy()

# -------------------------------------------------------------------------
# Missing values
# -------------------------------------------------------------------------
print("Missing values:\n", df2.isnull().sum())

# -------------------------------------------------------------------------
# Category label standardisation — fix spelling inconsistency
# -------------------------------------------------------------------------
df2["digital_ad_platform"] = df2["digital_ad_platform"].replace(
    {"Linkedln": "LinkedIn"}
)

# -------------------------------------------------------------------------
# Range validation for familiarity score (1-5)
# -------------------------------------------------------------------------
oor = df2[(df2["outlook_familiarity_score"] < 1) | (df2["outlook_familiarity_score"] > 5)]
print("Out-of-range familiarity scores:", len(oor))

# -------------------------------------------------------------------------
# Full-record duplicate check
# -------------------------------------------------------------------------
dup2 = df2.duplicated().sum()
print(f"Duplicates: {dup2} ({dup2/len(df2)*100:.1f}%)")

# Save cleaned data for downstream scripts
df2.to_pickle("df2_clean.pkl")
