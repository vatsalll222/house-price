# House Price Prediction

A Machine Learning project that predicts house prices based on various features using Python and Scikit-learn.

## Project Overview

This project uses a housing dataset to train a machine learning model capable of predicting house prices. The model is trained on historical housing data and can be used to estimate prices for new houses based on their characteristics.

## Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Train-test split
* Machine Learning model training
* Hyperparameter tuning
* Model serialization using Pickle
* Price prediction for new data

## Project Structure

```
house-price/
│
├── app.py
├── book.ipynb
├── model.pkl
├── House Price India.csv
├── requirements.txt
└── README.md
```

## Dataset

The dataset contains housing information such as:

* Number of bedrooms
* Number of bathrooms
* Area
* Location-related features
* Other property attributes

Target Variable:

* House Price

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook
* Pickle

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vatsalll222/house-price.git
```

2. Navigate to the project directory:

```bash
cd house-price
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### Jupyter Notebook

```bash
jupyter notebook
```

Open `book.ipynb` and run the cells.

### Python Application

```bash
python app.py
```

## Model Training

The model is trained using Scikit-learn after splitting the dataset into training and testing sets.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)
```

## Results

The trained model is saved as:

```text
model.pkl
```

This file can be loaded later for predictions without retraining.

## Author

Vatsal

## Live Demo

[🔗 Try the App](https://house-price-prediction-vatsal.streamlit.app/)

## Source Code

[📂 GitHub Repository](https://github.com/vatsalll222/house-price)



```
```