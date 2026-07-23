"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 3: Reliability analysis — Cronbach's Alpha (Section 6).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd

df1 = pd.read_pickle("df1_clean.pkl")


def cronbach_alpha(data: pd.DataFrame) -> float:
    """Cronbach's alpha for a set of Likert items."""
    item_vars = data.var(axis=0, ddof=1)
    total_var = data.sum(axis=1).var(ddof=1)
    n_items = data.shape[1]
    alpha = (n_items / (n_items - 1)) * (1 - item_vars.sum() / total_var)
    return alpha


service_items = df1[["service_rating", "content_rating", "price_rating",
                      "delivery_rating", "experience_rating",
                      "customer_support_rating"]]

alpha = cronbach_alpha(service_items)
print(f"Cronbach's Alpha (6 items): {alpha:.3f}")
