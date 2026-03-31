# 🦠 COVID-19 Trend Tracker (Python + Dash)

An interactive dashboard to visualize real-time COVID-19 data across the globe.  
Built using Python and Dash, this project allows users to explore trends, compare countries, and analyze key metrics like cases, recoveries, deaths, and testing rates.

---

## 🚀 Features

- 📊 Global trend analysis (daily cases & 7-day moving average)
- 🌍 Interactive world map visualization
- 🔄 Auto-refresh every 5 minutes (live data)
- 📈 Multi-country comparison (bar chart)
- 📋 Country-wise statistics (cases, deaths, recoveries, tests)
- 🌙 Light / Dark mode toggle
- 🎯 Clean and responsive UI

---

## 🛠 Tech Stack

- Python  
- Dash (by Plotly)  
- Pandas  
- Plotly Express  
- Requests  

---

## 📡 Data Source

Live COVID-19 data fetched from:

- disease.sh API  
  https://disease.sh/

---

## 📁 Project Structure
covid-tracker/
│── app.py
│── data.py
│── requirements.txt
│── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/anandpatel9044/covid-tracker.git
cd covid-tracker
pip install -r requirements.txt
python app.py
http://127.0.0.1:8050/
