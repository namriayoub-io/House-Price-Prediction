# 🏠 House Price Prediction

An end-to-end Machine Learning project for predicting house prices using **Linear Regression**.

This project covers the complete workflow of a Machine Learning application, from data preparation and model training to model evaluation, API development, Docker containerization, deployment, monitoring, and a web interface.

---

## 📌 Project Overview

The goal of this project is to build a complete Machine Learning application capable of predicting house prices based on several house characteristics and geographic information.

Unlike a project that only focuses on training a Machine Learning model, this project follows an **End-to-End Machine Learning workflow**:

```text
Dataset
   ↓
Data Exploration & Preparation
   ↓
Machine Learning Model
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
FastAPI
   ↓
Docker
   ↓
Deployment
   ↓
Monitoring
   ↓
Frontend
```

---

## 🎯 Objectives

The main objectives of this project are:

* Explore and prepare the dataset
* Select the relevant features
* Train a Linear Regression model
* Evaluate the model using regression metrics
* Save the trained Machine Learning model
* Build a REST API using FastAPI
* Containerize the application using Docker
* Deploy the application using Cloudflare Tunnel
* Implement a basic health-check system
* Create a simple web interface
* Connect the frontend to the Machine Learning API

---

# 📊 Dataset

The project uses the **California Housing dataset**.

The dataset contains information about houses and their geographic location.

## Features

| Feature      | Description                |
| ------------ | -------------------------- |
| `MedInc`     | Median income              |
| `HouseAge`   | Median house age           |
| `AveRooms`   | Average number of rooms    |
| `AveBedrms`  | Average number of bedrooms |
| `Population` | Population                 |
| `AveOccup`   | Average house occupancy    |
| `Latitude`   | Geographic latitude        |
| `Longitude`  | Geographic longitude       |

### Target

The target variable represents the **median house value**.

The model uses the eight features above to predict the target value.

---

# 🔎 Machine Learning Workflow

The Machine Learning workflow follows several steps.

## 1. Data Loading

The dataset is loaded and prepared for analysis.

```python
import pandas as pd
import numpy as np
```

---

## 2. Data Exploration

The dataset is explored to understand:

* Number of observations
* Features
* Data types
* Statistical information
* Missing values
* Dataset structure

Typical operations include:

```python
df.head()
df.info()
df.describe()
df.isnull().sum()
```

---

## 3. Feature Selection

The following features are used by the model:

```text
MedInc
HouseAge
AveRooms
AveBedrms
Population
AveOccup
Latitude
Longitude
```

The target variable is the house value.

---

## 4. Train/Test Split

The dataset is divided into:

* Training data
* Testing data

The training set is used to train the model, while the testing set is used to evaluate its performance on unseen data.

---

## 5. Model Training

The Machine Learning algorithm used in this project is:

**Linear Regression**

The model is implemented using Scikit-learn.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

---

# 🤖 Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this project, the model learns the relationship between house characteristics and house prices.

The general idea is:

```text
Input Features
      ↓
Linear Regression Model
      ↓
Predicted House Price
```

---

# 📈 Model Evaluation

The model was evaluated using several regression metrics:

* MAE
* MSE
* RMSE
* R² Score

## Results

| Metric   |  Result |
| -------- | ------: |
| MAE      |  0.2701 |
| MSE      |  0.1188 |
| RMSE     |  0.3446 |
| R² Score | ≈ 0.803 |

### MAE — Mean Absolute Error

MAE measures the average absolute difference between the real values and the predicted values.

```text
MAE = 0.2701
```

### MSE — Mean Squared Error

MSE calculates the average squared error between predictions and actual values.

```text
MSE = 0.1188
```

### RMSE — Root Mean Squared Error

RMSE is the square root of MSE and represents the prediction error in the same scale as the target.

```text
RMSE = 0.3446
```

### R² Score

R² indicates how much of the variation in the target variable is explained by the model.

```text
R² ≈ 0.803
```

---

# 💾 Model Saving

After training, the model is saved using `joblib`.

```python
import joblib

joblib.dump(model, "model/house_price_model.pkl")
```

The trained model is stored in:

```text
model/
└── house_price_model.pkl
```

This allows the API to load the already-trained model without training it again every time the application starts.

---

# ⚡ FastAPI

After building the Machine Learning model, a REST API was created using **FastAPI**.

The API loads the saved model and provides an endpoint for making predictions.

## API Architecture

```text
Client
  ↓
FastAPI
  ↓
Load Trained Model
  ↓
Prediction
  ↓
JSON Response
```

---

# 🔗 API Endpoints

## 1. Home

```http
GET /
```

The root endpoint serves the web frontend.

---

## 2. Health Check

```http
GET /health
```

This endpoint checks whether the API and Machine Learning model are running correctly.

### Example response

```json
{
  "status": "ok",
  "model": "loaded"
}
```

---

## 3. Prediction

```http
POST /predict
```

This endpoint receives the house features and returns the predicted price.

### Example request

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

### Example response

```json
{
  "predicted_price": 3.458570838417759
}
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, Swagger UI is available at:

```text
http://127.0.0.1:10000/docs
```

The Swagger interface can be used to:

* View the API endpoints
* Send prediction requests
* Test the `/predict` endpoint
* Check API responses

---

# 🌐 Frontend

A simple frontend was created to make the Machine Learning application easier to use.

The frontend was developed using:

* HTML
* CSS
* JavaScript

The user can enter the required house information and request a prediction directly from the web interface.

## Frontend workflow

```text
User
 ↓
HTML Form
 ↓
JavaScript
 ↓
POST /predict
 ↓
FastAPI
 ↓
Linear Regression Model
 ↓
Prediction
 ↓
Frontend
```

---

# 📁 Frontend Structure

```text
frontend/
│
├── index.html
├── style.css
└── script.js
```

### `index.html`

Contains the structure of the prediction interface.

### `style.css`

Contains the visual design of the application.

### `script.js`

Collects the user inputs and sends them to the FastAPI `/predict` endpoint.

---

# 🐳 Docker

The complete application was containerized using Docker.

Docker allows the application and its dependencies to run in an isolated environment.

## Docker workflow

```text
Project Files
     ↓
Dockerfile
     ↓
Docker Image
     ↓
Docker Container
     ↓
FastAPI Application
```

---

## Build the Docker Image

```bash
docker build -t house-price-api .
```

---

## Run the Docker Container

```bash
docker run -p 10000:10000 house-price-api
```

The application will be available at:

```text
http://127.0.0.1:10000
```

---

# 🚀 Deployment

For temporary public access, the application was exposed to the internet using **Cloudflare Quick Tunnel**.

The Docker container runs the FastAPI application locally, and Cloudflare Tunnel creates a temporary public URL.

## Deployment architecture

```text
Internet
   ↓
Cloudflare Quick Tunnel
   ↓
Local Machine
   ↓
Docker Container
   ↓
FastAPI
   ↓
Machine Learning Model
```

The tunnel was started using:

```bash
cloudflared tunnel --url http://localhost:10000
```

This provides a temporary public URL that can be used to access the application from outside the local machine.

---

# 🔍 Monitoring

Basic monitoring was implemented through a health-check endpoint and Docker logs.

## Health Check

```http
GET /health
```

Example:

```json
{
  "status": "ok",
  "model": "loaded"
}
```

This allows us to verify that:

* The API is running
* The Machine Learning model has been loaded

---

## Docker Logs

Docker logs can also be used to monitor API requests.

Example:

```text
"GET /health HTTP/1.1" 200 OK
"POST /predict HTTP/1.1" 200 OK
```

This provides basic visibility into the application's activity.

---

# 🧱 Project Architecture

The complete project can be represented as follows:

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │ HTML / CSS / JS     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │   REST API          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Trained Model      │
                    │ Linear Regression   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Predicted House     │
                    │       Price         │
                    └─────────────────────┘
```

---

# 🛠️ Technologies Used

## Programming Languages

* Python
* JavaScript
* HTML
* CSS

## Data Science & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib

## API Development

* FastAPI
* Uvicorn
* Pydantic

## Deployment & DevOps

* Docker
* Cloudflare Tunnel
* Git
* GitHub

---

# 📦 Project Structure

```text
House-Price-Prediction/
│
├── app/
│   └── main.py
│
├── model/
│   └── house_price_model.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── ...
│
├── house_price_projet.py
│
├── Dockerfile
│
├── requirements.txt
│
└── README.md
```

---

# 💻 Installation

## 1. Clone the repository

```bash
git clone https://github.com/namriayoub-io/House-Price-Prediction.git
```

## 2. Navigate to the project

```bash
cd House-Price-Prediction
```

## 3. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI application:

```bash
uvicorn app.main:app --reload --port 10000
```

Then open:

```text
http://127.0.0.1:10000
```

API documentation:

```text
http://127.0.0.1:10000/docs
```

Health check:

```text
http://127.0.0.1:10000/health
```

---

# 🐳 Run with Docker

Instead of installing the Python dependencies manually, the application can also be run using Docker.

### Build

```bash
docker build -t house-price-api .
```

### Run

```bash
docker run -p 10000:10000 house-price-api
```

Then open:

```text
http://127.0.0.1:10000
```

---

# 🧪 Example Prediction

Example input:

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

Example output:

```json
{
  "predicted_price": 3.458570838417759
}
```

---

# 🔄 Complete End-to-End Workflow

The final workflow of the project is:

```text
1. Dataset
      ↓
2. Data Exploration
      ↓
3. Data Preparation
      ↓
4. Feature Selection
      ↓
5. Train/Test Split
      ↓
6. Linear Regression
      ↓
7. Model Evaluation
      ↓
8. Model Saving with Joblib
      ↓
9. FastAPI
      ↓
10. Docker
      ↓
11. Cloudflare Tunnel
      ↓
12. Monitoring
      ↓
13. Frontend
      ↓
14. Complete End-to-End Application
```

---

# 📌 What I Learned

Through this project, I practiced several important concepts:

### Machine Learning

* Dataset exploration
* Feature selection
* Train/Test Split
* Linear Regression
* Model training
* Model evaluation
* Regression metrics
* Model persistence

### Backend Development

* FastAPI
* REST APIs
* POST requests
* JSON data
* Pydantic models
* API documentation with Swagger

### Deployment & DevOps

* Docker
* Docker images
* Docker containers
* Environment configuration
* Cloudflare Tunnel
* Basic monitoring

### Frontend

* HTML forms
* CSS styling
* JavaScript
* Fetch API
* Frontend/API integration

---

# 🔮 Future Improvements

Possible improvements for future versions include:

* Compare Linear Regression with other Machine Learning algorithms
* Add more data preprocessing techniques
* Improve model performance
* Add automated tests
* Add API validation improvements
* Add CI/CD using GitHub Actions
* Add advanced monitoring
* Add model versioning
* Improve the frontend design
* Deploy the application on permanent cloud infrastructure
* Add authentication and API security

---

# 👨‍💻 Author

**Ayoub Namri**

Artificial Intelligence & Software Engineering Student

### GitHub

https://github.com/namriayoub-io

### Project Repository

https://github.com/namriayoub-io/House-Price-Prediction

---

# ⭐ Project

This project was developed as a practical **End-to-End Machine Learning project**, combining Machine Learning, API development, Docker, deployment, monitoring, and frontend integration.
