# 🏠 House Price Prediction

An End-to-End Machine Learning project that predicts house prices using **Linear Regression**.

## 🎯 Project Overview

This project covers the main steps of a Machine Learning application:

* Data exploration and preparation
* Feature selection
* Linear Regression
* Model evaluation
* Model saving
* FastAPI API
* Docker
* Basic monitoring
* Simple web interface
* Temporary deployment with Cloudflare Tunnel

## 📊 Dataset

The project uses the **California Housing dataset**.

### Features

* `MedInc` — Median income
* `HouseAge` — House age
* `AveRooms` — Average rooms
* `AveBedrms` — Average bedrooms
* `Population` — Population
* `AveOccup` — Average occupancy
* `Latitude` — Latitude
* `Longitude` — Longitude

### Target

`MedHouseVal` — Median house value.

## 🤖 Machine Learning

**Model:** Linear Regression

### Evaluation

| Metric |   Score |
| ------ | ------: |
| MAE    |  0.2701 |
| MSE    |  0.1188 |
| RMSE   |  0.3446 |
| R²     | ≈ 0.803 |

The trained model is saved with **Joblib** and used by the API for predictions.

## ⚡ FastAPI

The model is exposed through a REST API.

### Endpoints

```text
GET  /health
POST /predict
```

Example prediction:

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984,
  "AveBedrms": 1.024,
  "Population": 322,
  "AveOccup": 2.556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

Response:

```json
{
  "predicted_price": 3.458570838417759
}
```

API documentation is available through:

```text
/docs
```

## 🌐 Frontend

A simple frontend was developed using:

* HTML
* CSS
* JavaScript

It allows users to enter the house features and receive a prediction directly from the FastAPI API.

## 🐳 Docker

The application is containerized using Docker.

```bash
docker build -t house-price-api .
docker run -p 10000:10000 house-price-api
```

Application:

```text
http://127.0.0.1:10000
```

## 🚀 Deployment

For temporary public access, the application was exposed using **Cloudflare Quick Tunnel**.

```text
Cloudflare Tunnel
        ↓
Docker
        ↓
FastAPI
        ↓
ML Model
```

## 🔍 Monitoring

A basic health-check endpoint was implemented:

```text
GET /health
```

Response:

```json
{
  "status": "ok",
  "model": "loaded"
}
```

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* FastAPI
* Docker
* HTML / CSS / JavaScript
* Git & GitHub
* Cloudflare Tunnel

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app/
│   └── main.py
├── model/
│   └── house_price_model.pkl
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── data/
├── house_price_projet.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 👨‍💻 Author

**Ayoub Namri**

Artificial Intelligence & Software Engineering Student

GitHub:
https://github.com/namriayoub-io
