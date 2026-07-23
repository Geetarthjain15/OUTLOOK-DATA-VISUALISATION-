"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 5: One-way ANOVA by Repurchase Intent (Section 8, Table 3, Figures 3-4).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df1 = pd.read_pickle("df1_clean.pkl")

numeric_cols = ["service_rating", "content_rating", "price_rating",
                "delivery_rating", "experience_rating",
                "customer_support_rating", "recommend_likelihood"]

groups_labels = ["No", "Will think of it", "Yes"]
anova_results = []
for var in numeric_cols:
    groups = [df1[df1["repurchase_intent"] == g][var] for g in groups_labels]
    f_stat, p_val = stats.f_oneway(*groups)
    means = {g: df1[df1["repurchase_intent"] == g][var].mean() for g in groups_labels}
    anova_results.append({
        "Variable": var,
        "Mean: No": means["No"],
        "Mean: Will Think": means["Will think of it"],
        "Mean: Yes": means["Yes"],
        "F-statistic": f_stat,
        "p-value": p_val,
        "Significant": "Yes" if p_val < 0.05 else "No"
    })

anova_df = pd.DataFrame(anova_results)
print(anova_df.round(3))

# Figure 4: boxplot of recommend_likelihood by repurchase intent
fig, ax = plt.subplots(figsize=(6, 5))
df1.boxplot(column="recommend_likelihood", by="repurchase_intent", ax=ax)
plt.title("Recommendation Score by Repurchase Intent Segment")
plt.suptitle("")
plt.ylabel("Recommend Likelihood (1-5)")
plt.tight_layout()
plt.savefig("fig4_boxplot_recommend.png", dpi=150)
plt.close()
