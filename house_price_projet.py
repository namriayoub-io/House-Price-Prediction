import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Phase 1 — Data Understanding
df = pd.read_csv('house_price_prediction_practice.csv')

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows',None) #afficher tous les lignes
pd.set_option('display.max_columns',None) #afficher tous les colonnes
pd.set_option('display.width',None) #afficher tous les colonnes dans meme lignes
print(df)

print(f"le nombre de lignes et colonnes :{df.shape}")
print('-'*50)
print(df.dtypes)
print('-'*50)
print(df.describe())
print('-'*50)
print(df.isna().sum())
print('-'*50)
print(f"les doublans : {df.duplicated().sum()}")
print('-'*50)

# Phase 2 — Data Preparation

x= df.drop('MedHouseVal',axis=1)
y= df['MedHouseVal']

# Phase 3 — Séparation des données

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Phase 4 — Construction du modèle

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Phase 5 — Évaluation
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
R2 = r2_score(y_test, y_pred)

print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)
print("R2:", R2)

print('-'*50)

# Phase 6 — Visualisation
# Visualization 1:
plt.figure(figsize=(8, 5))
plt.scatter(df['HouseAge'], df['MedHouseVal'], color='red')
plt.title('HouseAge vs MedHouseVal')
plt.xlabel('HouseAge')
plt.ylabel('MedHouseVal')
plt.grid()
plt.show()

# # Visualization 2:

plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred, color='blue')

# Perfect prediction line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color='red'
)

plt.title('Actual Price vs Predicted Price')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

plt.grid()
plt.show()

#Phase 7 — Model Interpretation

w1 = model.coef_
w0 = model.intercept_
print(w1)
print(w0)
