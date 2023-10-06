# Banglore Home Price Prediction

This project focuses on predicting home prices in Bangalore, India, using a machine learning model. The application allows users to estimate the price of a house based on various factors such as square footage, the number of bedrooms (BHK), the number of bathrooms, and the location.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Linear Regression
- **Data Processing**: Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Web Framework**: Flask

## Project Overview

### Data Exploration and Preprocessing

- The dataset used for this project was obtained from Kaggle and contains information about home prices in Bangalore.

- Data preprocessing steps include handling missing values, data cleaning, and feature engineering.

### Data Visualization

- The project includes data visualization using Matplotlib and Seaborn to understand the distribution of home prices and explore correlations between variables.

### Model Building

- A Linear Regression model is implemented to predict home prices. The model is trained and evaluated using cross-validation.

### Web Application

- The frontend of the application is developed using HTML, CSS, and JavaScript to create an interactive user interface.

- The backend is powered by a Flask server, which serves as an API for the machine learning model.

- Users can input details such as square footage, the number of bedrooms, bathrooms, and select a location to estimate home prices.

### Deployment

- The application is deployed on Heroku to make it accessible online.

## Usage

To run the project locally:

1. Clone the repository.

2. Install the required Python libraries listed in `requirements.txt`.

3. Run the Flask app using the command `python app.py`.

4. Access the web application at `http://localhost:5000` in your web browser.

## Project Structure

The project directory structure is organized as follows:

- `app.py`: Flask application for serving the web interface and making predictions.

- `data.csv`: The dataset used for training and testing the model.

- `client/`: Contains CSS and JavaScript files for styling and interactivity and HTML templates for the web interface.

- `model/`: Contains the trained machine learning model and preprocessing artifacts.

- `requirements.txt`: List of Python dependencies.

## Contributors

- Daanyal Parbulkar

## License

This project is licensed under the [MIT License](LICENSE).

