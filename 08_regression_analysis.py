"""
Case Study 1 — Customer Loyalty & Response Analysis
Step 8: Multiple Linear Regression (Section 11).
Requires df1_clean.pkl produced by 01_data_cleaning.py
"""

import pandas as pd
import statsmodels.api as sm

df1 = pd.read_pickle("df1_clean.pkl")

X = df1[["service_rating", "content_rating", "price_rating",
         "delivery_rating", "experience_rating", "customer_support_rating"]]
X = sm.add_constant(X)
y = df1["recommend_likelihood"]

ols_model = sm.OLS(y, X).fit()
print(ols_model.summary())

# Key stats used in report:
# ols_model.rsquared, ols_model.rsquared_adj,
# ols_model.fvalue, ols_model.f_pvalue,
# ols_model.params, ols_model.pvalues
