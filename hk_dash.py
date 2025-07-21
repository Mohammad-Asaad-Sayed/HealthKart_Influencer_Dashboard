# 💪 HealthKart | Influencer Campaign Performance Dashboard
# NOTE: To run this Streamlit app, install required libraries:
# pip install streamlit altair pandas

import streamlit as st
import pandas as pd
import altair as alt

# App Setup
st.set_page_config(page_title="HealthKart Influencer ROI Dashboard", layout="wide")
st.title("💪 HealthKart | Influencer Campaign Performance Dashboard")

# Sidebar Upload + Filters in Expanders
with st.sidebar:
    with st.expander("📤 Upload CSV Files", expanded=True):
        influencers_file = st.file_uploader("Influencers", type="csv")
        posts_file = st.file_uploader("Posts", type="csv")
        tracking_file = st.file_uploader("Tracking Data", type="csv")
        payouts_file = st.file_uploader("Payouts", type="csv")



# Main Logic
if influencers_file and posts_file and tracking_file and payouts_file:
    influencers = pd.read_csv(influencers_file)
    posts = pd.read_csv(posts_file)
    tracking = pd.read_csv(tracking_file)
    payouts = pd.read_csv(payouts_file)

    # Simulate baseline revenue
    baseline_revenue = tracking.groupby('influencer_id')['revenue'].sum().reset_index()
    baseline_revenue['baseline'] = 1000

    # Merge all data
    merged = pd.merge(tracking, payouts, on="influencer_id")
    merged = pd.merge(merged, baseline_revenue[['influencer_id', 'baseline']], on="influencer_id")
    merged = pd.merge(merged, influencers, left_on='influencer_id', right_on='ID')
    merged = pd.merge(merged, posts[['influencer_id', 'reach', 'likes', 'comments']], on='influencer_id', how='left')

    # Derived metrics
    merged['engagement_rate'] = (merged['likes'] + merged['comments']) / merged['reach']
    merged['ROAS'] = merged['revenue'] / merged['total_payout']
    merged['Incremental Revenue'] = merged['revenue'] - merged['baseline']
    merged['Incremental ROAS'] = merged['Incremental Revenue'] / merged['total_payout']

    def classify_roi(roas):
        if roas >= 3:
            return 'High'
        elif roas >= 1.5:
            return 'Medium'
        else:
            return 'Low'

    merged['ROI Segment'] = merged['ROAS'].apply(classify_roi)

    # Update filter values
    with st.sidebar:
        with st.expander("🎛 Filter Options", expanded=True):
            platform_filter = st.multiselect("Platform", merged['platform'].unique(), default=list(merged['platform'].unique()))
            product_filter = st.multiselect("Product", merged['product'].unique(), default=list(merged['product'].unique()))
            gender_filter = st.multiselect("Gender", merged['gender'].unique(), default=list(merged['gender'].unique()))

    filtered = merged[
        merged['platform'].isin(platform_filter) &
        merged['product'].isin(product_filter) &
        merged['gender'].isin(gender_filter)
    ]

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Metrics", "🧠 Insights", "📊 Charts", "🗃 Raw Data"])

    # Metrics Tab
    with tab1:
        st.subheader("📈 Key Campaign Metrics")
        total_revenue = filtered['revenue'].sum()
        total_spend = filtered['total_payout'].sum()
        avg_roas = total_revenue / total_spend if total_spend != 0 else 0
        incremental_roas = filtered['Incremental Revenue'].sum() / total_spend if total_spend != 0 else 0
        avg_engagement = filtered['engagement_rate'].mean()

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
        col2.metric("📤 Total Payout", f"₹{total_spend:,.0f}")
        col3.metric("📊 Avg ROAS", f"{avg_roas:.2f}")
        col4.metric("📈 Incremental ROAS", f"{incremental_roas:.2f}")
        col5.metric("❤️ Engagement Rate", f"{avg_engagement:.2%}")

    # Insights Tab
    with tab2:
        st.subheader("🧠 Top Influencers by Incremental ROAS")
        top_influencers = filtered.groupby('influencer_id').agg({
            'revenue': 'sum',
            'baseline': 'mean',
            'Incremental Revenue': 'sum',
            'total_payout': 'sum',
            'engagement_rate': 'mean'
        })
        top_influencers['ROAS'] = top_influencers['revenue'] / top_influencers['total_payout']
        top_influencers['Incremental ROAS'] = top_influencers['Incremental Revenue'] / top_influencers['total_payout']
        top_influencers = top_influencers.sort_values(by='Incremental ROAS', ascending=False).reset_index()
        top_influencers = pd.merge(top_influencers, influencers, left_on='influencer_id', right_on='ID')

        st.dataframe(top_influencers[['name', 'platform', 'gender', 'follower_count', 'ROAS', 'Incremental ROAS', 'engagement_rate']].round(2))

    # Charts Tab
    with tab3:
        st.subheader("📊 Visual Insights")
        top5 = top_influencers.sort_values("ROAS", ascending=False).head(5)

        bar = alt.Chart(top5).mark_bar().encode(
            x=alt.X('name:N', title='Influencer'),
            y=alt.Y('ROAS:Q', title='ROAS'),
            color='platform:N',
            tooltip=['name', 'ROAS', 'platform']
        ).properties(title='Top 5 Influencers by ROAS')

        st.altair_chart(bar, use_container_width=True)

        scatter = alt.Chart(top_influencers).mark_circle(size=100).encode(
            x=alt.X('total_payout:Q', title='Payout (₹)'),
            y=alt.Y('revenue:Q', title='Revenue (₹)'),
            color='platform:N',
            tooltip=['name', 'total_payout', 'revenue']
        ).properties(title='Revenue vs Payout by Influencer')

        st.altair_chart(scatter, use_container_width=True)

    # Raw Data Tab
    with tab4:
        st.subheader("🗃 Raw Merged Data (Filtered)")
        st.dataframe(filtered)

else:
    st.info("📥 Please upload all four CSV files to begin analysis.")
