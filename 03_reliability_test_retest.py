"""
Case Study 2 — Brand Awareness & Digital Marketing Effectiveness
Step 3: Reliability Check — Test-Retest on Awareness (Section 6, Figure 6).
Requires df2_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd

df2 = pd.read_pickle("df2_clean.pkl")

df2["consistent"] = (df2["outlook_awareness"] == df2["outlook_awareness_repeat"])
agreement_rate = df2["consistent"].mean() * 100

print(f"Test-retest agreement rate: {agreement_rate:.2f}%")
print("Expected if random (2 binary options): 50.00%")

# Save for downstream scripts
df2.to_pickle("df2_with_reliability.pkl")
