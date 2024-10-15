# Car Price Prediction System

This project was developed during the **Data Science & Business Analytics** course at EDIT. The goal was to create a car price prediction system using a dataset derived from the **1985 Ward's Automotive Yearbook**.

## Dataset

The dataset used for this project consists of various features related to automobiles from 1985. Key features include:
- Engine size
- Curb weight
- Highway MPG
- Horsepower
- Width

## Files

The following files are included in this project:

- `MLM_Automobile_Dataset.pdf`: The dataset used for analysis.
- `ML_FinalExercise.pdf`: Final project documentation.
- `app.py`: Main application file for running the prediction model.
- `descriptive_analysis.ipynb`: Jupyter Notebook containing descriptive analysis of the dataset.
- `imports-85.data`: Raw data file.
- `mega_model.pkl`: Trained machine learning model for car price prediction.
- `predict_page.py`: Streamlit app for car price predictions.
- `work_v2.ipynb`: Additional analysis and work on the dataset.

## How to Run the Application

1. Ensure you have Streamlit installed. If not, you can install it via pip:

   ```bash
   pip install streamlit

2. The app will load in your web browser. You will need to input the following features to get the predicted car price:

* Engine Size
* Curb Weight
* Highway MPG
* Horsepower
* Width

## Model Description

The model is a machine learning model saved in the mega_model.pkl file. It predicts the price of cars based on the input features provided through the Streamlit application.

## License

This project is for educational purposes only. Feel free to use and modify it as you wish.
