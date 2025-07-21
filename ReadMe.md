# 📊 Influencer Campaign ROI Dashboard

A **Streamlit-based interactive dashboard** to analyze and track the performance, ROAS, and incremental ROI of influencer campaigns across platforms like **Instagram** and **YouTube**.

🔗 **Live App**: [Click to Open](https://healthkartinfluencerdashboard-aeura3bu7pdk5xss7bi8u2.streamlit.app/)

---

## 🚀 Features

* 📄 Upload simulated influencer, post, tracking, and payout data
* 📈 Automatic ROAS & Incremental ROAS calculation
* 💡 Summary metrics: Total Revenue, Spend, Avg ROAS, Incremental ROAS
* 🎛️ Interactive filters: Platform, Product, Gender
* 📊 Visual insights: Bar and Scatter charts
* 🧐 Ranking of top influencers by ROAS and Incremental ROAS

---

## 📁 Folder Structure

```
influencer-campaign-dashboard/
├── influencers.csv
├── posts.csv
├── tracking_data.csv
├── payouts.csv
├── app.py              ← (Main Streamlit App)
└── README.md
```

---

## 📦 Requirements

Make sure you have **Python 3.8+** installed, then install the dependencies:

```bash
pip install streamlit pandas altair
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📊 Sample Data Schema

### influencers.csv

| ID | name | category | gender | follower\_count | platform |
| -- | ---- | -------- | ------ | --------------- | -------- |

### posts.csv

\| influencer\_id | platform | date | URL | caption | reach | likes | comments |

### tracking\_data.csv

\| source | campaign | influencer\_id | user\_id | product | date | orders | revenue |

### payouts.csv

\| influencer\_id | basis | rate | orders | total\_payout |

---

## ⚙️ Assumptions

* Baseline revenue is simulated at **₹1000 per influencer** to compute Incremental ROAS.
* Data is assumed clean and consistent (e.g., valid `influencer_id` references).
* Designed for **exploratory and reporting** use-cases; can be extended with real data pipelines.

---

## ✨ Future Improvements

* 📄 Export reports to PDF/CSV
* 🔐 Add authentication for multiple campaign users
* 💾 Store data in a persistent backend (SQLite, Supabase, etc.)
* 🧹 Add brand/campaign-specific insights

---

## 👨‍💼 Built With

* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Altair](https://altair-viz.github.io/)

---

## 📝 License

[MIT License](https://choosealicense.com/licenses/mit/)

---

## 💡 Contact

For queries, reach out via [GitHub](https://github.com) or email.
