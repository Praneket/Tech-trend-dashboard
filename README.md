Tech Stack Evolution in Kaggle Notebooks

This project was developed as part of the **Meta Kaggle Hackathon 2025**. It explores how various data science stacks such as Deep Learning, Machine Learning, R-based analytics, and EDA have evolved over time on Kaggle, using the Meta Kaggle dataset.

---
📌 Project Overview

We analyzed notebook metadata from 2015 to 2024 and categorized each into stack types using associated tags. Key deliverables include:

- 📘 Dataset Merging & Preprocessing (Day 1)
- 📈 Stack Trend Analysis Over Time (Day 2)
- 📊 Stack Categorization & Author Contributions (Day 3)
- 💻 Final Streamlit Dashboard Deployment (Day 4)

---

🚀 Live Dashboard

👉 [Click to view the live Streamlit dashboard](https://tech-trend-dashboard.streamlit.app/)

---

📁 Files

| File | Description |
|------|-------------|
| `tech_stack_evolution_dashboard_final.py` | Streamlit dashboard app (Days 1–4 combined) |
| `day3_notebooks_with_stack.csv` | Preprocessed dataset with notebook-stack mapping |
| `day3_stack_trends.csv` | Year-wise stack usage counts |
| `requirements.txt` | Required Python packages |
| `README.md` | Project overview and documentation |

---

📊 Sample Visuals

- 📈 Line chart of stack usage trends over years  
- 📊 Bar chart of notebook counts by tech stack  
- 🏆 Top 5 contributors per stack category

---

🧠 Key Insights

- 📈 **Deep Learning** surged post-2020, dominating notebook submissions.
- 📊 **EDA tools** remain essential across all stacks.
- 📉 **R-based notebooks** have declined in popularity.
- 🏆 Each tech stack has specialized top authors in the community.

---

🛠️ Tech Stack

- `Python`, `pandas`, `plotly`, `streamlit`
- `Meta Kaggle Datasets` (Kernels, KernelVersions, Tags, KernelTags)

---

🙌 Authors

Team: Submission by **[Praneket]**

Mentor: Meta Kaggle Hackathon Community & OpenAI

---

🏁 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run tech_stack_evolution_dashboard_final.py
