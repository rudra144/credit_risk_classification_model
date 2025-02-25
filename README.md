Here’s your **complete** `README.md`, which includes **your original content** plus the **API section** I wrote for you. This file is **fully structured, professional, and ready to be added to your repository.** 🚀

```markdown
# **Credit Risk Prediction - README**

## **Project Overview**
This project focuses on **predicting credit risk** by identifying **loan defaulters** using **historical financial data**. Leveraging **machine learning models**, the system helps financial institutions make **data-driven lending decisions**.

---

## **Features**
- **End-to-End Machine Learning Pipeline**
- **Handles Class Imbalance (SMOTE-Tomek, Undersampling)**
- **Hyperparameter Tuning with Optuna**
- **Risk Segmentation via Rank Ordering & Deciles**
- **Feature Importance Analysis for Risk Mitigation**
- **FastAPI-powered API for Real-Time Predictions**
- **Dockerized for Scalable Deployment**

---

## **API Documentation (Swagger UI)**
FastAPI provides an **interactive API documentation** at `/docs`.  
![Swagger UI](img/FastAPI - Swagger UI.png)

---

## **Project Structure**
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
│── server.py                     # FastAPI server
│── Dockerfile                    # Docker setup for deployment
```

---

# **API Endpoints**
## **Base URL**
```
http://localhost:8000
```

### **1️⃣ Health Check**
- **Endpoint**: `/`
- **Method**: `GET`
- **Purpose**: Check if the API is running.

- **Response:**
  ```json
  {
    "message": "Credit Risk API is running"
  }
  ```

---

### **2️⃣ Predict Credit Risk**
- **Endpoint**: `/predict`
- **Method**: `POST`
- **Request Format**: JSON
- **Response Format**: JSON
- **Content-Type**: `application/json`

#### **Sample JSON Request from UI**
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
  "loan_purpose": "Home Renovation",
  "loan_type": "Personal Loan"
}
```

#### **Sample JSON Response**
```json
{
  "default_probability": 0.0614273543330177,
  "credit_score": 809,
  "rating": "Excellent"
}
```

---

## **3️⃣ UI to API Flow**
1. **User Inputs Data** → UI collects borrower details.
2. **UI Sends JSON Request** → The UI formats input data as JSON and sends a `POST` request to `/predict`.
3. **API Processes Data** → The API applies a **machine learning model** to predict risk.
4. **API Returns JSON Response** → The UI receives the risk assessment and displays the result.

---

## **4️⃣ Example UI Request Using Fetch API**
If your UI is built with JavaScript, you can **send data to the API using Fetch**:
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

## **5️⃣ cURL Request for Testing**
If you want to **test the API from the terminal**, run:
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
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

## **6️⃣ API Validation**
- **If the JSON request is missing fields**, the API should return a `422 Unprocessable Entity` error.
- **If data types are incorrect**, the API should return a `400 Bad Request` response.

---

## **Key Performance Metrics (KPIs)**
| Metric | Value |
|--------|------|
| **F1-Score** | 0.976 |
| **Accuracy** | 96% |
| **AUC-ROC** | 0.984 |
| **Gini Coefficient** | 0.967 |
| **KS-Statistic** | 85.98% |
| **Recall (Defaulters)** | 86% |

---

## **Data Pipeline**
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

## **Future Improvements**
- **Deploy model using AWS SageMaker for real-time predictions.**
- **Automate data ingestion & risk scoring dashboard.**
- **Enhance model with real-time streaming fraud detection.**

---

## **Contributors**
- **Rudhresh Madhusudhanan** *(Lead Data Scientist)*
- Open to collaborations! Feel free to reach out on **[LinkedIn](www.linkedin.com/in/rudhresh-madhusudhanan)**.

---

## **License**
This project is **open-source** under the **MIT License**.

---

