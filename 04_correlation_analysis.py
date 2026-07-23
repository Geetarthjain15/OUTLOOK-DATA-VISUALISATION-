"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 4: Pearson correlation analysis (Section 7 / Figure 2).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_pickle("df1_clean.pkl")

corr_cols = ["service_rating", "content_rating", "price_rating",
             "delivery_rating", "experience_rating",
             "customer_support_rating", "recommend_likelihood"]

corr_matrix = df1[corr_cols].corr(method="pearson")
print(corr_matrix.round(2))

plt.figure(figsize=(7, 6))
plt.imshow(corr_matrix, cmap="RdBu_r", vmin=-1, vmax=1)
plt.colorbar(label="Correlation")
plt.xticks(range(len(corr_cols)), corr_cols, rotation=45, ha="right")
plt.yticks(range(len(corr_cols)), corr_cols)
for i in range(len(corr_cols)):
    for j in range(len(corr_cols)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8)
plt.title("Correlation Matrix — Service Dimensions & Recommendation Intent")
plt.tight_layout()
plt.savefig("fig2_correlation_matrix.png", dpi=150)
plt.close()
