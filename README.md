# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendations in E-Commerce

Welcome to **Shopper Spectrum**, a data analytics project focused on extracting actionable insights from e-commerce transactional data to boost customer engagement and drive sales through targeted segmentation and personalized recommendations.

---

## 📋 Project Overview

The e-commerce sector generates massive data on customer transactions daily. This project analyzes such data to:

- Segment customers based on their buying behavior using **RFM analysis**  
- Recommend products using **collaborative filtering**  
- Build an interactive **Streamlit** app for real-time segmentation and recommendation  

This helps businesses identify valuable customers, detect at-risk users, and suggest relevant products dynamically.

---

## 🧰 Key Features

- **Data Cleaning & Preprocessing**  
- **RFM Feature Engineering** for Recency, Frequency, and Monetary value  
- **Customer Segmentation** using clustering algorithms (KMeans & Hierarchical)  
- **Collaborative Filtering-based Product Recommendations** leveraging cosine similarity  
- **Interactive Streamlit Web Application** with:  
  - Customer Segmentation input and live predictions  
  - Product Recommendation by product name input

---

## 🚀 How to Use

1. Clone the repository
   
    `https://github.com/gvdharun/Shopper-Spectrum.git`

2. Install dependencies: `pip install -r requirements.txt`
3. Prepare your dataset or use the provided cleaned data
4. Run the Streamlit app:

    `streamlit run Shopper_Spectrum_app.py`

5. Explore customer segments and get product recommendations interactively

---

📁 Repository Structure
```
├── 📂 data/
│   ├── 📄 online_retail.csv           # Raw or processed transaction dataset
│   ├── 📄 product_mapping.pkl        # StockCode <-> Product Description mapping
│   ├── 📄 product_similarity.pkl     # Product similarity matrix (pickle file)
│   └── 📄 rfm_segmented.csv          # Customer RFM and segment labels
│
├── 📂 models/
│   ├── 📦 rfm_scaled.pkl             # Scaler for RFM features (pickle file)
│   └── 📦 rfm_kmeans.pkl             # KMeans clustering model (pickle file)
│
├── 📝 Shopper_Spectrum_app.py        # Streamlit app combining segmentation and recommendations
├── 📊 Shopper_Spectrum.ipynb         # Jupyter notebook (Data preprocessing, EDA, Feature Engg, Clustering)
└── 📚 README.md                      # Project documentation
```

---

## 📈 Insights & Business Use Cases

- **Targeted Marketing:** Focus campaigns on high-value customers  
- **Customer Retention:** Identify and nurture at-risk customers  
- **Upsell & Cross-sell:** Recommend products customers are most likely to buy  
- **Inventory Optimization:** Stock products according to customer demand patterns  

---

## 🛠️ Technologies & Libraries

- Python: `pandas`, `numpy`, `scikit-learn`  
- Visualization: `matplotlib`, `seaborn`  
- Machine Learning: `KMeans`, `DBSCAN`, `Hierarchical`, `cosine similarity`  
- Web App: `Streamlit`  
- Saving Files: `joblib`  

---

## 🙌 Conclusion

Thank you for exploring the **🛒 Shopper Spectrum** project!

This repository demonstrates a complete end-to-end approach to enhancing e-commerce performance through:

- **Robust customer segmentation** leveraging RFM analytics and clustering techniques  
- **Personalized product recommendations** powered by collaborative filtering and similarity matrices  
- **Interactive Streamlit application** for real-time insights and business decision support  

By harnessing transactional data effectively, businesses can create more targeted marketing strategies, improve customer loyalty, and boost sales with data-driven product suggestions.

Feel free to explore, contribute, and adapt this project to unlock the full potential of your e-commerce data!

🚀 **Empower your business with shopper intelligence and actionable analytics!**

---


