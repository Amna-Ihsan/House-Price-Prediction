## House Price Prediction using Linear Regression

This project predicts house prices using a **Linear Regression** machine learning model. The model is trained on housing data with features such as square footage, number of bedrooms, number of bathrooms, year built, lot size, garage size, and neighborhood quality.<br>
<a href ="https://house-price-prediction-8uwxj4tvxwvvarnwenih9r.streamlit.app/">Live Demo</a>
### Project Overview

The goal of this project is to build a simple machine learning application that estimates the selling price of a house based on user-provided property details. The trained model is deployed using **Streamlit**, allowing users to enter house features through an interactive web interface and receive a predicted price.

### Features Used

The model uses the following input features:

* `Square_Footage`
* `Num_Bedrooms`
* `Num_Bathrooms`
* `Year_Built`
* `Lot_Size`
* `Garage_Size`
* `Neighborhood_Quality`

The target variable is:

* `House_Price`

### Machine Learning Workflow

1. Loaded the dataset using pandas.
2. Removed duplicate records.
3. Split the data into training and testing sets.
4. Applied `MinMaxScaler` to scale the input features.
5. Trained a `LinearRegression` model using scikit-learn.
6. Evaluated the model using:

   * R² Score
   * Mean Absolute Error
   * Root Mean Squared Error
7. Saved the trained model and scaler using joblib.
8. Built a Streamlit app for user interaction and prediction.

### Technologies Used

* Python
* pandas
* NumPy
* scikit-learn
* matplotlib
* joblib
* Streamlit

### Important Note

Since the model was trained using scaled input features, the same scaler must be applied before making predictions. The Streamlit app loads the saved scaler and model to ensure predictions are made correctly.
