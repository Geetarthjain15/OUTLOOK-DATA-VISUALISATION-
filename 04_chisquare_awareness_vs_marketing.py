"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 4: Chi-square Tests — Awareness vs Marketing Variables (Section 7, Figure 7).
Requires df2_with_reliability.pkl produced by 03_reliability_test_retest.py
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df2 = pd.read_pickle("df2_with_reliability.pkl")

cat_vars = ["brand_awareness_influencer", "brand_discovery_method",
            "digital_ad_platform", "campaign_frequency",
            "digital_buy_frequency", "digital_monthly_spend"]

chi_results = []
for var in cat_vars:
    ct = pd.crosstab(df2["outlook_awareness"], df2[var])
    chi2, p, dof, _ = stats.chi2_contingency(ct)
    chi_results.append({"Variable": var, "Chi-square": chi2, "df": dof, "p-value": p})

chi_df = pd.DataFrame(chi_results)
print(chi_df.round(3))

# Figure 7: bar chart of p-values with alpha = 0.05 threshold line
plt.figure(figsize=(8, 5))
plt.bar(chi_df["Variable"], chi_df["p-value"], color="gray")
plt.axhline(0.05, linestyle="--", color="red", label="alpha = 0.05")
plt.xticks(rotation=30, ha="right")
plt.ylabel("p-value")
plt.title("Chi-square Test Results vs Brand Awareness")
plt.legend()
plt.tight_layout()
plt.savefig("fig7_chisq_pvalues.png", dpi=150)
plt.close()
