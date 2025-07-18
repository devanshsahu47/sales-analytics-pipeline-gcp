# 📈 Automated Sales Data Pipeline & International Growth Dashboard (GCP)

This project showcases a fully automated, end-to-end data pipeline deployed on **Google Cloud Platform (GCP)**. It ingests raw e-commerce sales data, processes it, stores it in a cloud data warehouse, and visualizes key business insights through an interactive **Looker Studio** dashboard focused on identifying international growth opportunities.

---

## 📌 Objective

Build a **scalable, serverless data analytics system** that provides real-time insights into international sales performance.

Key goals:

- **Automated Data Ingestion**: Seamlessly load new sales data into the data warehouse.
- **Exploratory Data Analysis (EDA)**: Uncover trends and patterns in global sales.
- **Interactive Visualization**: Highlight international market performance through a dynamic dashboard.

---

## ⚙️ Architecture Overview

The pipeline follows an **event-driven, serverless** architecture using GCP components:

| Stage          | Tool                    | Purpose                                                 |
|----------------|-------------------------|---------------------------------------------------------|
| Ingestion      | Google Cloud Storage    | Upload `.csv` files to trigger the pipeline             |
| Processing     | Cloud Run               | Serverless Python function processes & loads the data   |
| Storage        | BigQuery                | Scalable data warehouse for real-time SQL querying      |
| Visualization  | Looker Studio           | Dashboard connects to BigQuery for up-to-date insights  |

---

## 📦 Dataset: E-Commerce Sales Data

**Filename**: `data.csv`  
A transactional dataset representing sales from an online retail company.

**Key Features**:

- `InvoiceNo`: Unique ID for each transaction
- `StockCode`, `Description`: Product identifiers and names
- `Quantity`: Number of units sold
- `InvoiceDate`: Timestamp of purchase
- `UnitPrice`: Price per item
- `CustomerID`: Unique customer identifier
- `Country`: Location of purchase

---

## 🔍 Key Insights from EDA

- **Market Dominance**: The UK contributes ~85% of all sales, indicating high domestic reliance.
- **Order Cancellations**: Negative quantities signal frequent cancellations needing further attention.
- **Peak Sales Window**: 12 PM to 2 PM emerges as the busiest time for transactions.
- **Guest Checkouts**: ~25% of sales lack `CustomerID`, complicating customer retention analysis.

---

## 📊 Dashboard Highlights: International Growth

The Looker Studio dashboard was developed to turn data into strategic direction for global expansion.

**Key Metrics & Findings**:

- **International Revenue Share**: 15.65% – a measurable baseline for non-UK growth
- **Top Non-UK Markets**: Netherlands, Ireland (EIRE), Germany, France
- **Higher AOV Internationally**: 
  - Intl AOV: €521  
  - UK AOV: €426
- **Top Intl Products Differ**: Best-selling international products differ from domestic bestsellers, influencing region-specific campaigns.

---

## 🧠 Tools & Technologies Used

| Tool / Tech         | Purpose                                      |
|---------------------|----------------------------------------------|
| Google Cloud Storage| Raw data lake for .csv ingestion             |
| Cloud Run           | Serverless Python-based data processing      |
| BigQuery            | Cloud data warehouse for analytical querying |
| Looker Studio       | Real-time, interactive dashboarding          |
| Python + pandas     | Data cleaning and transformation             |
| GitHub              | Version control and project tracking         |

---

## 🧩 Business Implications

- International markets, particularly **Germany** and **France**, present strong growth potential.
- Higher AOV internationally justifies investment in:
  - Region-specific marketing
  - Localized websites
  - International shipping capabilities
- Product marketing should be localized; bestsellers vary by region.

---

## 🔗 Live Dashboard

👉 [**View the Live International Growth Dashboard**] https://lookerstudio.google.com/reporting/27adc2e9-bde6-4e1a-9f30-da73dc777749

---

## 📝 License

This project is licensed under the **MIT License**. Feel free to use, share, and adapt with attribution.
