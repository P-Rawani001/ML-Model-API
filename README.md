# 🚀 ML Model API (FastAPI + Docker)

## 📌 Overview

This project is a **Machine Learning-powered REST API** built using **FastAPI** and fully **containerized with Docker**.
It predicts outcomes (e.g., heart disease risk) based on user input features using a trained ML model.

The project follows a **modular backend architecture** and is designed to be **scalable, production-ready, and easy to deploy**.

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn
* **Language:** Python 3.10
* **Containerization:** Docker
* **API Testing:** Swagger UI / Postman

---

## 📂 Project Structure

```
ML-Model-API/
│
├── app/
│   ├── api/            # API routes
│   ├── ml/             # ML model (model.pkl)
│   ├── models/         # Pydantic schemas
│   ├── services/       # Business logic & prediction
│   ├── utils/          # Utility functions
│   └── main.py         # FastAPI entry point
│
├── Dockerfile          # Docker configuration
├── requirements.txt    # Dependencies
├── frontend.py         # Optional frontend script
└── .gitignore
```

---

## ⚙️ Features

* ✅ RESTful API using FastAPI
* ✅ Machine Learning model integration
* ✅ Clean modular architecture
* ✅ Dockerized for easy deployment
* ✅ Interactive API documentation (Swagger UI)

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ml-model-api.git
cd ml-model-api
```

---

### 2️⃣ Create virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

### 5️⃣ Open API docs

👉 http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker (Recommended)

### 1️⃣ Build Docker image

```bash
docker build -t ml-api .
```

---

### 2️⃣ Run container

```bash
docker run -p 8000:8000 ml-api
```

---

### 3️⃣ Access API

👉 http://localhost:8000/docs

---

## 📡 API Endpoints

| Method | Endpoint | Description             |
| ------ | -------- | ----------------------- |
| POST   | /predict | Get ML model prediction |

---

## 🧠 Model Details

* Trained using **Scikit-learn**
* Saved as `model.pkl`
* Loaded at runtime for predictions

---

## 📈 Future Improvements

* 🔹 Add frontend (React / Streamlit)
* 🔹 Deploy on cloud (Render / AWS / Railway)
* 🔹 Add authentication & logging
* 🔹 Use cloud storage for model
* 🔹 Add CI/CD pipeline

---

## 👨‍💻 Author

**Pankaj Kumar Rawani**

* GitHub: https://github.com/P-Rawani001

---

## ⭐ Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.
