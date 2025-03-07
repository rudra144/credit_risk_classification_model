
---

# **Credit Risk Prediction - README** 

## ** Project Overview**
This project focuses on **predicting credit risk** by identifying **loan defaulters** using **historical financial data**. Leveraging **machine learning models**, the system helps financial institutions make **data-driven lending decisions**.

---

## Features
- **End-to-End Machine Learning Pipeline**
- **Handles Class Imbalance (SMOTE-Tomek, Undersampling)**
- **Hyperparameter Tuning with Optuna**
- **Risk Segmentation via Rank Ordering & Deciles**
- **Feature Importance Analysis for Risk Mitigation**
- **FastAPI-powered API for Real-Time Predictions**
- **Dockerized for Scalable Deployment**

---
## Streamlit UI Preview
This project includes a **Streamlit-based web interface** for easy interaction.

![Streamlit UI - Input](img/credit_risk_modelling_input.png)
![Streamlit UI - Prediction](img/Credit_Risk Modelling_output.png)

- Upload loan details and get an **instant credit risk score**.
- Powered by **FastAPI backend + ML model**.

## API Documentation (Swagger UI)
FastAPI provides an **interactive API documentation** at `/docs`.

![Swagger UI](img/fastapi_swagger_ui.png)


---

## ** Project Structure**
```
📁 credit_risk_prediction/
│── 📁 .devcontainer/             # Development container settings
│── 📁 .idea/                     # IDE project settings
│── 📁 .ipynb_checkpoints/        # Jupyter Notebook checkpoints
│── 📁 __pycache__/               # Compiled Python files
│── 📁 app/                       # API for model inference (FastAPI)
│── 📁 artifacts/                 # Trained models and logs
│── 📁 dataset/                   # Data Files (customers, loans, bureau data)
│── credit_risk_model.ipynb       # Jupyter Notebook for model training & evaluation
│── requirements.txt              # Required dependencies
```
Your README formatting seems cluttered and difficult to read due to:

1. **Lack of proper sectioning** – Headers should be clear and consistently formatted.
2. **Improper JSON and code block formatting** – Code should be inside proper fenced code blocks (` ```json `, ` ```bash `, etc.).
3. **Markdown syntax issues** – Numbers (`2`, `3`, `4`, etc.) appearing unintentionally.
4. **Overloaded inline text** – Long lines of text make it difficult to follow.

---

### **🚀 Cleaned-Up README Structure**

Here's an improved version of your **API Documentation** section:

```markdown
## API Documentation

### **1️⃣ Predict Credit Risk Endpoint**
**Endpoint:** `/predict`  
**Method:** `POST`  
**Request Format:** `JSON`  
**Response Format:** `JSON`  
**Content-Type:** `application/json`  

#### **📌 Example JSON Request (From UI)**
```json
{
  "age": 35,
  "income": 55000,
  "loan_amount": 20000,
  "loan_tenure_months": 60,
  "avg_dpd_per_delinquency": 2.5,
  "delinquency_ratio": 0.12,
  "credit_utilization_ratio": 0.45,
  "num_open_accounts": 5,
  "residence_type": "Owned",
  "loan_type": "Personal Loan",
  "loan_purpose": "Home Renovation"
}
```

#### **📌 Example JSON Response**
```json
{
  "default_probability": 0.0614273543330177,
  "credit_score": 809,
  "rating": "Excellent"
}
```

---

### **2️⃣ UI to API Flow**
1. **User Inputs Data** → UI collects borrower details.
2. **UI Formats JSON Request** → UI sends a `POST` request to `/predict`.
3. **API Processes Data** → The API applies a machine learning model to assess risk.
4. **API Returns JSON Response** → UI receives the risk assessment and displays the result.

---

### **3️⃣ Example Request Using Fetch API**
If your UI is built with JavaScript, you can send data to the API using `fetch`:

```javascript
fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    age: 35,
    income: 55000,
    loan_amount: 20000,
    loan_tenure_months: 60,
    avg_dpd_per_delinquency: 2.5,
    delinquency_ratio: 0.12,
    credit_utilization_ratio: 0.45,
    num_open_accounts: 5,
    residence_type: "Owned",
    loan_purpose: "Home Renovation",
    loan_type: "Personal Loan"
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

---

### **4️⃣ Example Request Using cURL**
If you want to test the API from the terminal, run:

```bash
curl -X 'POST' 'http://localhost:8000/predict' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "age": 35,
  "income": 55000,
  "loan_amount": 20000,
  "loan_tenure_months": 60,
  "avg_dpd_per_delinquency": 2.5,
  "delinquency_ratio": 0.12,
  "credit_utilization_ratio": 0.45,
  "num_open_accounts": 5,
  "residence_type": "Owned",
  "loan_purpose": "Home Renovation",
  "loan_type": "Personal Loan"
}'
```

---


```

---

### **🚀 Key Fixes & Improvements:**
✅ **Properly structured** API documentation  
✅ **Clearly formatted code blocks** for JSON, JavaScript, and cURL  
✅ **Better readability with sectioning**  
✅ **Images properly referenced**  
✅ **Easier to follow UI-API interaction**

Now, **your README will look professional and well-structured**. Let me know if you need any further refinements! 🚀
---

## ** Features**
✅ **End-to-End Machine Learning Pipeline**  
✅ **Handles Class Imbalance (SMOTE-Tomek, Undersampling)**  
✅ **Hyperparameter Tuning with Optuna**  
✅ **Risk Segmentation via Rank Ordering & Deciles**  
✅ **Feature Importance Analysis for Risk Mitigation**  
✅ **Automated Deployment with FastAPI (Planned)**  

---

## ** Key Performance Metrics (KPIs)**
| Metric | Value |
|--------|------|
| **F1-Score** | 0.976 |
| **Accuracy** | 96% |
| **AUC-ROC** | 0.984 |
| **Gini Coefficient** | 0.967 |
| **KS-Statistic** | 85.98% |
| **Recall (Defaulters)** | 86% |

---

## ** Data Pipeline**
1. **Data Collection & Preprocessing**
   - Merged **Customer, Loan, and Bureau Data** (~50,000 records).
   - Handled **missing values** & **categorical encoding**.

2. **Exploratory Data Analysis (EDA)**
   - Identified **key risk factors** (Loan-to-Income, Credit Utilization).
   - **Class imbalance observed** → Addressed using **SMOTE-Tomek**.

3. **Model Training & Optimization**
   - Tested **Logistic Regression, Random Forest, and XGBoost**.
   - **XGBoost (Optuna-tuned) achieved the best performance**.

4. **Evaluation & Risk Segmentation**
   - **AUC-ROC = 0.984** → Excellent discrimination between risky & non-risky loans.
   - **Rank Ordering with Deciles** → Identified **top-risk customers**.

---

Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/credit-risk-model.git
cd credit-risk-model
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Start the FastAPI Server
bash
Copy
Edit
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
The FastAPI server will start at http://localhost:8000
Open http://localhost:8000/docs to access the Swagger UI.
4️⃣ Launch the Streamlit UI
bash
Copy
Edit
streamlit run app/main.py
The Streamlit UI will open in your browser.
You can upload loan applicant details and get real-time credit risk assessment.

---

## ** Model Insights**
- **Top 10% customers (Decile 9 & 8) account for 98.6% of defaults.**
- **Loan-to-Income & Credit Utilization** are the most influential features.
- **AUC-ROC = 0.98** confirms the model's effectiveness in distinguishing risky borrowers.

---

## ** Future Improvements**
-  **Deploy model using AWS SageMaker for real-time predictions.**
-  **Automate data ingestion & risk scoring dashboard.**
-  **Enhance model with real-time streaming fraud detection.**

---

## ** Contributors**
- **Rudhresh Madhusudhanan** *(Lead Data Scientist)*
- Open to collaborations! Feel free to reach out on **[LinkedIn](www.linkedin.com/in/rudhresh-madhusudhanan)**.

---

## ** License**
This project is **open-source** under the **MIT License**.

---

This **README.md** is structured to match your project directory while ensuring clarity and completeness. 🚀 Let me know if you need modifications!
