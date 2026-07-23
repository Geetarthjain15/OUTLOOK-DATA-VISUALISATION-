"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 6: Net Promoter Score (NPS) Dashboard (Section 9, Figures 5-6).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd

df1 = pd.read_pickle("df1_clean.pkl")


def nps_band(score):
    if score <= 2:
        return "Detractor"
    elif score == 3:
        return "Passive"
    else:
        return "Promoter"


df1["nps_band"] = df1["recommend_likelihood"].apply(nps_band)

nps_counts = df1["nps_band"].value_counts(normalize=True) * 100
promoters_pct = nps_counts.get("Promoter", 0)
detractors_pct = nps_counts.get("Detractor", 0)
nps_score = promoters_pct - detractors_pct

print(f"NPS composition:\n{nps_counts.round(1)}")
print(f"Net Promoter Score = {nps_score:.1f}")

repurchase_dist = df1["repurchase_intent"].value_counts(normalize=True) * 100
print("Repurchase intent distribution:\n", repurchase_dist.round(1))

# Save for downstream chi-square script
df1.to_pickle("df1_with_nps.pkl")
