# ⚽ AI Football Predictor

An AI-powered football match prediction system built with **Python** and **Streamlit**.

This project combines **Artificial Intelligence**, **Statistics**, and **Data Science** to simulate football matches and generate realistic predictions using Expected Goals (xG), Poisson Distribution, Bayesian ratings, and Monte Carlo Simulation.

---

## 🚀 Features

* ⚽ Expected Goals (xG)
* 🏆 Win / Draw / Loss probabilities
* 🥇 Qualification probability
* 🎯 Most likely exact score
* 📊 Interactive dashboard with Plotly visualizations
* 🔄 What-if scenarios (player availability, tactical adjustments, team ratings)
* ⚡ Monte Carlo Simulation (up to **250,000** simulated matches)

---

## 🧠 Prediction Engine

The prediction model combines multiple statistical approaches:

* Bayesian Attack & Defence Strength
* Expected Goals (xG)
* Poisson Goal Distribution
* Monte Carlo Simulation

Together, these models estimate realistic football match outcomes based on team strength, attacking and defensive performance, and probabilistic simulations.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

---

## 📂 Project Structure

```text
AI-Football-Predictor/
│
├── app.py                 
├── predict.py             
├── requirements.txt
├── README.md
│
├── assets/
│   ├── fifa_world_cup.png
│   ├── france.png
│   ├── spain.png
│   └── players/
│       ├── mbappe.png
│       └── yamal.png
│
├── data/
│   ├── matches.csv
│   └── team_inputs.csv
│
├── src/
│   ├── models.py
│   ├── loader.py
│   ├── predictor.py
│   ├── expected_goals.py
│   ├── poisson.py
│   ├── monte_carlo.py
│   ├── charts.py
│   └── utils.py
│
└── tests/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yousraerraki/AI-Football-Predictor.git
```

Navigate to the project folder:

```bash
cd AI-Football-Predictor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Example Prediction

Example match:

**🇫🇷 France vs 🇪🇸 Spain**

The application predicts:

* Expected Goals (xG)
* Win / Draw / Loss probabilities
* Qualification probability
* Most likely exact score
* Interactive visualizations
* What-if scenario analysis

---

## 📸 Screenshots

You can add screenshots such as:

* 🏠 Home Dashboard
* 📊 Prediction Results
* 📈 Probability Charts
* 🔥 Score Heatmap

---

## 🎥 Demo

A video demonstration of the application is available on my LinkedIn profile.

---

## 🚀 Future Improvements

* Live football data integration
* FIFA/ELO rating updates
* Team statistics API
* Player performance analysis
* Injury impact model
* Machine Learning models
* Tournament prediction mode
* Multi-language support

---

## 👩‍💻 Author

**Yousra Erraki**

Computer Engineering Student | AI & Data Enthusiast

🔗 LinkedIn
[www.linkedin.com/in/yousra-erraki-885b20221](http://www.linkedin.com/in/yousra-erraki-885b20221)

💻 GitHub
https://github.com/yousraerraki

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

Feedback and suggestions are always welcome!
