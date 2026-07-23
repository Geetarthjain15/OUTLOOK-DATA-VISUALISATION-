"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 2: Descriptive statistics (Table 2 / Figure 1).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_pickle("df1_clean.pkl")

numeric_cols = ["service_rating", "content_rating", "price_rating",
                "delivery_rating", "experience_rating",
                "customer_support_rating", "recommend_likelihood"]

desc = df1[numeric_cols].agg(["mean", "std", "median"]).T
desc["skew"] = df1[numeric_cols].skew()
desc.columns = ["Mean", "Std Dev", "Median", "Skewness"]
print(desc.round(2))

# Figure 1: Average customer rating by touchpoint
means_sorted = df1[numeric_cols].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
colors = ["#1f3864"] * (len(means_sorted) - 1) + ["#c9a227"]
plt.bar(means_sorted.index, means_sorted.values, color=colors)
plt.ylim(0, 5)
plt.ylabel("Mean Score (1-5)")
plt.title("Average Customer Ratings Across Touchpoints")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("fig1_avg_ratings.png", dpi=150)
plt.close()
