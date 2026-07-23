"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 7: Pivot-table cross-tabulations PT1-PT3 (Section 10).
Requires df2_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
from scipy import stats

df2 = pd.read_pickle("df2_clean.pkl")

# -------------------------------------------------------------------------
# PT1 — Brand Awareness x Digital Buy Frequency
# -------------------------------------------------------------------------
ct_pt1 = pd.crosstab(df2["outlook_awareness"], df2["digital_buy_frequency"])
chi2_a, p_a, dof_a, _ = stats.chi2_contingency(ct_pt1)
print("PT1 crosstab:\n", ct_pt1)
print(f"PT1 chi2={chi2_a:.3f}, df={dof_a}, p={p_a:.3f}")

# -------------------------------------------------------------------------
# PT2 — Digital Monthly Spend x Campaign Frequency
# -------------------------------------------------------------------------
ct_pt2 = pd.crosstab(df2["digital_monthly_spend"], df2["campaign_frequency"])
chi2_b, p_b, dof_b, _ = stats.chi2_contingency(ct_pt2)
print("\nPT2 crosstab:\n", ct_pt2)
print(f"PT2 chi2={chi2_b:.3f}, df={dof_b}, p={p_b:.3f}")

# -------------------------------------------------------------------------
# PT3 — Brand Discovery Method x Awareness
# -------------------------------------------------------------------------
ct_pt3 = pd.crosstab(df2["brand_discovery_method"], df2["outlook_awareness"])
chi2_c, p_c, dof_c, _ = stats.chi2_contingency(ct_pt3)
print("\nPT3 crosstab:\n", ct_pt3)
print(f"PT3 chi2={chi2_c:.3f}, df={dof_c}, p={p_c:.3f}")
