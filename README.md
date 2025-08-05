**Digital Commerce Readiness Dashboard**
This project visualizes the multidimensional readiness of Indian states to participate in the digital commerce ecosystem. Using publicly available government data, the dashboard provides a comparative view of financial inclusion, digital infrastructure, education, and entrepreneurship across states.

**Live Dashboard**
Access the dashboard here: 

**Project Structure**
📁 dashboard_project/
   ├── app.py                      # Streamlit app script
├── data/
   └── digital_readiness_master.csv  # Normalized dataset used in dashboard
│
├── requirements.txt               # Required Python libraries
📊 Features in the Dashboard
📈 DCRI Score vs. Key Indicators
Analyze how broadband, financial access, education, and urbanization correlate with the Digital Commerce Readiness Index (DCRI).

🧮 Principal Component Contributions
Understand how the PCA dimensions (PC1–PC4) contribute to digital readiness.

🧪 Cluster Analysis
States are grouped into 3 clusters based on common readiness profiles (low, medium, high).

🧭 Compare States on Key Indicators
Choose any two states to compare their performance on normalized metrics like MSME density, startup count, literacy rate, etc.

📌 Identify Gaps & Outliers
Highlight high-potential but underutilized regions and those with structural bottlenecks.

🧪 Tech Stack
Python 3.9+

Streamlit

Plotly

Pandas, Seaborn, Matplotlib, Statsmodels

🚀 How to Run Locally
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/digital-commerce-readiness.git
cd digital-commerce-readiness/dashboard_project
2. Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
bash
Copy
Edit
pip install -r ../requirements.txt
4. Run the dashboard:
bash
Copy
Edit
streamlit run app.py
📈 Data Sources
MSME & Startup data from government portals

UPI/IMPS & PMJDY data (RBI, NPCI, Ministry of Finance)

Broadband & Literacy: Census 2011 and TRAI

Higher Education: AISHE data

Population normalization from latest available estimates

📬 Feedback & Contributions
We welcome feedback, suggestions, and PRs! Feel free to fork the repo or raise issues.

