"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 2: Descriptive profile (Section 5, Figures 1-5).
Requires df2_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd

df2 = pd.read_pickle("df2_clean.pkl")

# Brand awareness split (Figure 1)
awareness_split = df2["outlook_awareness"].value_counts(normalize=True) * 100
print("Brand awareness split (%):\n", awareness_split.round(1))

# Category profiles (Figures 2-4)
cat_vars = ["brand_awareness_influencer", "brand_discovery_method",
            "digital_ad_platform", "campaign_frequency",
            "digital_buy_frequency", "digital_monthly_spend"]
for c in cat_vars:
    print(f"\n{c}:\n", df2[c].value_counts(normalize=True).mul(100).round(1))

# Familiarity score distribution (Figure 5)
familiarity_desc = df2["outlook_familiarity_score"].agg(["mean", "std"])
print("\nFamiliarity score mean/std:\n", familiarity_desc.round(2))
