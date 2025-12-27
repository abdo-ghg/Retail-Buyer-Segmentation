"""
Dashboard for Retail Buyer Segmentation Analysis

This script creates an interactive dashboard using Streamlit to visualize key insights from the customer segmentation analysis. The dashboard includes:
- Total spending by product category
- Relationship between annual income and total spending
- Purchase channel preferences
- Key findings summary

To run:
1. Install requirements: pip install streamlit pandas matplotlib seaborn
2. Run: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data
data = pd.read_csv("Data/data.csv")

# Calculate total spending per category (fix column names)
spend_cols = ['spend_wine', 'spend_fruits', 'spend_meat', 'spend_fish', 'spend_sweets', 'spend_gold']
data['TotalSpend'] = data[spend_cols].sum(axis=1)

# Sidebar
st.sidebar.title("Retail Buyer Segmentation Dashboard")
st.sidebar.markdown("Analyze customer spending and behavior.")

st.title("Retail Buyer Segmentation Dashboard")


# 1. Total spending by product category
st.header("1. Total Spending by Product Category")
category_totals = data[spend_cols].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots()
sns.barplot(x=category_totals.values, y=category_totals.index.str.replace('spend_', '').str.title(), ax=ax1, palette="viridis")
ax1.set_xlabel("Total Spend")
ax1.set_ylabel("Product Category")
st.pyplot(fig1)

st.markdown("""
- **Wine** and **Meat** are the main drivers of customer spending.
- Wine spending is the highest, followed by Meat. Other categories contribute less.
- There is a large variation in total spending among customers.
""")

# 2. Relationship between annual income and total spending
st.header("2. Annual Income vs. Total Spending")
fig2, ax2 = plt.subplots()
sns.scatterplot(x=data['annual_income'], y=data['TotalSpend'], ax=ax2, alpha=0.6)
ax2.set_xlabel("Annual Income")
ax2.set_ylabel("Total Spending")
st.pyplot(fig2)

correlation = data['annual_income'].corr(data['TotalSpend'])
st.markdown(f"**Correlation between annual income and total spending:** {correlation:.2f}")
st.markdown("""
- There is a strong positive relationship between annual income and total spending.
- Most high spenders (Total Spend > 1500) have incomes between 50,000 and 100,000.
""")


# 3. Purchase channel preferences
st.header("3. Purchase Channel Preferences")
channels = {
	'num_store_purchases': 'Store',
	'num_web_purchases': 'Web',
	'num_catalog_purchases': 'Catalog',
	'num_discount_purchases': 'Deals'
}
channel_totals = {v: data[k].sum() for k, v in channels.items() if k in data.columns}
channel_df = pd.DataFrame(list(channel_totals.items()), columns=['Channel', 'Total Purchases'])
fig3, ax3 = plt.subplots()
sns.barplot(x='Total Purchases', y='Channel', data=channel_df, ax=ax3, palette="mako")
ax3.set_xlabel("Total Purchases")
ax3.set_ylabel("Channel")
st.pyplot(fig3)

st.markdown("""
- **Store** is the preferred purchase channel, followed by **Web**.
- Catalog and Deals channels are used less frequently.
""")


# 4. More Insights & Graphs
st.header("4. More Insights & Graphs")

# Spending by Education Level
st.subheader("Spending by Education Level")
edu_spend = data.groupby('education_level')['TotalSpend'].mean().sort_values(ascending=False)
fig4, ax4 = plt.subplots()
edu_spend.plot(kind='bar', ax=ax4, color='skyblue')
ax4.set_ylabel('Average Total Spend')
ax4.set_xlabel('Education Level')
st.pyplot(fig4)
st.markdown("- Customers with higher education levels tend to spend more on average.")

# Spending by Age Group
st.subheader("Spending by Age Group")
import numpy as np
data['age'] = 2025 - data['birth_year']
bins = [18, 30, 40, 50, 60, 70, 100]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70+']
data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)
age_spend = data.groupby('age_group')['TotalSpend'].mean()
fig5, ax5 = plt.subplots()
age_spend.plot(kind='bar', ax=ax5, color='coral')
ax5.set_ylabel('Average Total Spend')
ax5.set_xlabel('Age Group')
st.pyplot(fig5)
st.markdown("- Spending varies by age group, with certain age ranges spending more on average.")

# Spending by Marital Status
st.subheader("Spending by Marital Status")
marital_spend = data.groupby('marital_status')['TotalSpend'].mean().sort_values(ascending=False)
fig6, ax6 = plt.subplots()
marital_spend.plot(kind='bar', ax=ax6, color='mediumseagreen')
ax6.set_ylabel('Average Total Spend')
ax6.set_xlabel('Marital Status')
st.pyplot(fig6)
st.markdown("- Marital status influences spending patterns.")

# Campaign Acceptance Rate
st.subheader("Campaign Acceptance Rate")
campaign_cols = [col for col in data.columns if col.startswith('accepted_campaign_')]
campaign_acceptance = data[campaign_cols].sum()
fig7, ax7 = plt.subplots()
campaign_acceptance.plot(kind='bar', ax=ax7, color='slateblue')
ax7.set_ylabel('Number of Acceptances')
ax7.set_xlabel('Campaign')
st.pyplot(fig7)
st.markdown("- Shows which campaigns were most successful.")

# Web Visits vs. Total Spend
st.subheader("Web Visits vs. Total Spend")
fig8, ax8 = plt.subplots()
sns.boxplot(x=data['web_visits_last_month'], y=data['TotalSpend'], ax=ax8)
ax8.set_xlabel('Web Visits Last Month')
ax8.set_ylabel('Total Spend')
st.pyplot(fig8)
st.markdown("- Analyzes if frequent web visits are associated with higher spending.")

# 5. Key Findings
st.header("Key Findings Summary")
st.markdown("""
1. **Wine dominates spending**: Wine and Meat are the top categories, with significant variation in total spending among customers.
2. **Income drives spending**: There is a strong positive correlation between annual income and total spending.
3. **Store is preferred**: Most purchases are made in-store, but web purchases are also significant.
4. **Education, age, and marital status** all influence spending patterns.
5. **Campaign effectiveness** varies, with some campaigns being more successful than others.
6. **Web activity** may be linked to spending, but the relationship is nuanced.
""")
