# Model Registry API

This is a minimal REST API built with **FastAPI** to manage machine learning models in a registry.

## Features

- Register a new model
- List all registered models
- Retrieve model details by ID
- Auto-generated Swagger docs at `/docs`

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/cberkbiryol/Learning_model_management_API.git
cd Learning_model_management_API
```

### 2. (Optional) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

### 5. Open in browser

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 Endpoints

| Method | Endpoint        | Description                 |
|--------|------------------|-----------------------------|
| POST   | `/models`        | Register a new model        |
| GET    | `/models`        | List all models             |
| GET    | `/models/{id}`   | Get model details by UUID   |

---

## 📄 Notes

- No database is used — the app stores models in memory.
- Designed for simplicity and clarity, per guidelines.
- Built using Python 3.11 and FastAPI.

---

## Author

Cemal Berk Biryol  
[GitHub Profile](https://github.com/cberkbiryol)  
cberkbiryol@gmail.com
