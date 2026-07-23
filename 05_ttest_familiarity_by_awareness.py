"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 5: Independent-Samples t-Test — Familiarity Score by Awareness (Section 8).
Requires df2_with_reliability.pkl produced by 03_reliability_test_retest.py
"""

import pandas as pd
from scipy import stats

df2 = pd.read_pickle("df2_with_reliability.pkl")

aware_yes = df2[df2["outlook_awareness"] == "Yes"]["outlook_familiarity_score"]
aware_no = df2[df2["outlook_awareness"] == "No"]["outlook_familiarity_score"]

t_stat, p_val = stats.ttest_ind(aware_yes, aware_no, equal_var=True)

print(f"Aware mean={aware_yes.mean():.3f} (n={len(aware_yes)})")
print(f"Not aware mean={aware_no.mean():.3f} (n={len(aware_no)})")
print(f"t-statistic={t_stat:.3f}, p-value={p_val:.3f}")
