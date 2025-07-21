# 📊 Influencer Campaign ROI Dashboard

A Streamlit-based interactive dashboard to analyze and track the performance, ROAS, and incremental ROI of influencer campaigns across platforms like Instagram and YouTube.

---

## 🚀 Features

- Upload simulated influencer, post, tracking, and payout data
- Automatic ROAS & Incremental ROAS calculation
- Summary metrics: Total Revenue, Spend, Avg ROAS, Incremental ROAS
- Interactive filters: Platform, Product, Gender
- Visual insights: Bar and Scatter charts
- Ranking of top influencers by ROAS and Incremental ROAS

---

## 📁 Folder Structure

```
📂 influencer-campaign-dashboard/
├── influencers.csv
├── posts.csv
├── tracking_data.csv
├── payouts.csv
├── app.py  ← (Main Streamlit file)
└── README.md
```

---

## 📦 Requirements

Make sure you have Python 3.8+ and install dependencies:

```bash
pip install streamlit pandas altair
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open the app in your browser (usually http://localhost:8501)

---

## 📊 Sample Data Schema

### influencers.csv
| ID | name | category | gender | follower_count | platform |
|----|------|----------|--------|----------------|----------|

### posts.csv
| influencer_id | platform | date | URL | caption | reach | likes | comments |

### tracking_data.csv
| source | campaign | influencer_id | user_id | product | date | orders | revenue |

### payouts.csv
| influencer_id | basis | rate | orders | total_payout |

---

## ⚙️ Assumptions

- Baseline revenue is simulated at ₹1000 per influencer to compute Incremental ROAS
- Data is assumed clean and consistent (e.g., all influencer_id references are valid)
- Works best for exploratory and reporting use-cases; can be extended with real data pipelines

---

## ✨ Future Improvements (Optional)

- Export reports to PDF/CSV
- Add authentication for multiple campaign users
- Store data in a persistent backend like SQLite or Supabase
- Add campaign-specific insights (per brand)

---

## 👨‍💻 Built With
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Altair](https://altair-viz.github.io/)

---

## 📝 License
MIT License

---

## 💡 Contact
For queries, reach out via GitHub or email.
