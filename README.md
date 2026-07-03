# 🥇 Gold Price Prediction using Machine Learning

A Machine Learning project that predicts gold prices using historical financial market data and economic indicators. This project demonstrates a complete end-to-end machine learning workflow including data preprocessing, exploratory data analysis, feature correlation analysis, model training, evaluation, and prediction.

---

## 📌 Project Overview

Gold is one of the most valuable and widely traded assets in the world. Its price is influenced by multiple economic and financial factors including stock market performance, oil prices, currency exchange rates, and silver prices.

Predicting gold prices accurately can help investors, analysts, and financial institutions make better decisions.

This project uses historical data and Machine Learning algorithms to predict gold prices based on various market indicators.

---

## 🎯 Objectives

The main goals of this project are:

- Analyze historical gold market data
- Identify important features affecting gold prices
- Perform preprocessing and exploratory analysis
- Train Machine Learning models
- Evaluate model performance
- Visualize prediction results

---

## 📊 Dataset Information

The dataset contains financial indicators such as:

| Feature | Description |
|-----------|-------------|
| Date | Date of observation |
| SPX | S&P 500 Index |
| GLD | Gold price |
| USO | United States Oil Fund price |
| SLV | Silver price |
| EUR/USD | Euro to USD exchange rate |

Dataset Shape:

```text
2290 Rows × 6 Columns
```

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-Learn

### Development Tools

- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
Gold_Price_Prediction/
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── gold_price_data.csv
├── README.md
├── requirements.txt
├── .gitignore
│
└── images/
```

---

## ⚙️ Project Workflow

### Step 1: Data Collection

The historical gold dataset was loaded using Pandas:

```python
gold_data = pd.read_csv("gold_price_data.csv")
```

---

### Step 2: Data Preprocessing

Preprocessing included:

✅ Dataset inspection  
✅ Missing value detection  
✅ Data type analysis  
✅ Statistical summary  
✅ Correlation analysis

Example:

```python
correlation = gold_data.drop(['Date'],axis=1).corr()
```

---

### Step 3: Exploratory Data Analysis

A correlation heatmap was created to understand relationships among variables.

```python
plt.figure(figsize=(8,8))

sns.heatmap(
    correlation,
    cbar=True,
    square=True,
    annot=True,
    cmap='Blues'
)
```

Visualization helps identify:

- Positive correlation
- Negative correlation
- Strong influencing factors

---

### Step 4: Feature Selection

Input features:

```text
SPX
USO
SLV
EUR/USD
```

Target variable:

```text
GLD
```

---

### Step 5: Train-Test Split

Dataset split into training and testing datasets.

```python
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=2
)
```

---

### Step 6: Model Training

Random Forest Regressor was used:

```python
model = RandomForestRegressor()

model.fit(X_train,Y_train)
```

---

## 📈 Model Evaluation

Performance was evaluated using:

### R² Score

```python
error_score = metrics.r2_score(
    Y_test,
    prediction
)
```

The R² score measures how well the model predicts gold prices.

Higher score → Better prediction accuracy.

---

## 📊 Prediction Visualization

Actual Gold Prices vs Predicted Gold Prices visualization:

```python
plt.plot(Y_test.values,label='Actual Value')
plt.plot(prediction,label='Predicted Value')

plt.xlabel("Number of Values")
plt.ylabel("Gold Price")
plt.legend()

plt.show()
```

---

## 🚀 Installation and Setup

Clone repository:

```bash
git clone https://github.com/Hellboy28D/Gold_Price_Prediction.git
```

Move into project:

```bash
cd Gold_Price_Prediction
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python src/predict.py
```

---

## 📌 Future Improvements

Potential enhancements:

- Hyperparameter tuning
- XGBoost implementation
- Deep Learning approach
- Live gold price API integration
- Streamlit web application
- Deployment on cloud platforms

---

## 💡 Key Learning Outcomes

This project helped strengthen my understanding of:

- Data preprocessing
- Feature engineering
- Correlation analysis
- Machine Learning workflow
- Random Forest Regression
- Model evaluation
- Data visualization
- Git and GitHub workflow

---

## 👨‍💻 Author

**Divakr Dayas**

GitHub:

https://github.com/Hellboy28D

LinkedIn:

(Add your LinkedIn profile here)

---

## ⭐ Support

If you found this project useful, consider giving it a star.

Feedback and suggestions are always welcome.

Happy Coding 🚀
