"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 7: Chi-square Test — NPS Category vs Repurchase Intent (Section 10).
Requires df1_with_nps.pkl produced by 06_nps_dashboard.py
"""

import pandas as pd
from scipy import stats

df1 = pd.read_pickle("df1_with_nps.pkl")

ct_nps_repurchase = pd.crosstab(df1["nps_band"], df1["repurchase_intent"])
chi2, p, dof, expected = stats.chi2_contingency(ct_nps_repurchase)

print("NPS x Repurchase crosstab:\n", ct_nps_repurchase)
print(f"Chi-square={chi2:.3f}, df={dof}, p={p:.3f}")
