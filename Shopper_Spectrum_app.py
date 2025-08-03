import streamlit as st
import pandas as pd
import joblib

# Load models and data
scaler = joblib.load('rfm_scaled.pkl')
kmeans = joblib.load('rfm_kmeans.pkl')
rfm_df = pd.read_csv('rfm_segmented.csv')
product_sim_df = pd.read_pickle('product_similarity.pkl')
product_mapping = pd.read_pickle('product_mapping.pkl')

st.title("🛒 Shopper Spectrum: E-Commerce Analytics")

# Tabs for Segmentation and Recommendation
tab1, tab2 = st.tabs(['Customer Segmentation', 'Product Recommendation'])

# --------- Customer Segmentation Module ---------
with tab1:
    st.header("Customer Segmentation")

    # Input fields for RFM values
    recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)
    frequency = st.number_input("Frequency (number of purchases)", min_value=0, max_value=1000, value=5)
    monetary = st.number_input("Monetary (total spend)", min_value=0.0, max_value=1_000_000.0, value=100.0, format="%.2f")

    if st.button("Predict Customer Segment"):
        # Scale inputs
        input_scaled = scaler.transform([[recency, frequency, monetary]])
        # Predict cluster
        cluster_label = kmeans.predict(input_scaled)[0]

        # Map predicted cluster to segment label using rfm_segmented.csv mapping
        # (Assuming cluster labels in 'Cluster' and segment names in 'Segment')
        segment_map = dict(zip(rfm_df['Cluster'], rfm_df['Segment']))
        # To avoid random assignment (since cluster labels can be non-sequential),
        # we'll pick the most frequent label for the predicted cluster from the dataset
        predicted_segment = rfm_df[rfm_df['Cluster'] == cluster_label]['Segment'].mode()
        segment = predicted_segment.values[0] if not predicted_segment.empty else 'Unknown'
        st.success(f"Predicted Cluster: **{cluster_label}**")
        st.success(f"Predicted Customer Segment: **{segment}**")

# --------- Product Recommendation Module ---------
with tab2:
    st.header("Product Recommendation")

    product_input = st.text_input("Enter product name:").strip().lower()
    n_recom = st.slider("Number of Recommendations", 1, 10, 5)

    # Create lookup dictionaries
    # Map Description (product name) to StockCode
    desc_to_code = dict(zip(product_mapping['Description'].str.lower(), product_mapping['StockCode']))
    # Map StockCode to Description (for displaying recommendations)
    code_to_desc = dict(zip(product_mapping['StockCode'], product_mapping['Description']))

    if st.button("Get Recommendations"):
        if not product_input:
            st.warning("Please enter a product name.")
        elif product_input in desc_to_code:
            stock_code = desc_to_code[product_input]

            if stock_code in product_sim_df.columns:
                # Get top N similar products excluding the input itself
                sim_scores = product_sim_df[stock_code].sort_values(ascending=False)[1:n_recom+1]
                recommended_codes = sim_scores.index.tolist()

                # Get product descriptions for recommended codes
                recommended_names = [code_to_desc.get(code, code) for code in recommended_codes]

                st.markdown(f"### Top {n_recom} products similar to **{product_input.title()}**:")
                for i, prod_name in enumerate(recommended_names, start=1):
                    st.write(f"{i}. {prod_name}")
            else:
                st.warning(f"Similarity data for product code '{stock_code}' not found.")
        else:
            st.warning(f"Product name '{product_input}' not found in the system. Please check spelling or try another.")
