
# Heart Failure Prediction: Exploratory Data Analysis and Machine Learning Models

This repository contains a comprehensive notebook that analyzes heart failure data, applies Exploratory Data Analysis (EDA), and builds seven machine learning models to predict heart failure. Additionally, a deployed web application is available for interactive use.

## Links
- **Streamlit Web App**: [Heart Failure Prediction App](https://heartfailureprediction-nk7dudqu5hffqkkby6kxqg.streamlit.app/)
- **Kaggle Notebook**: [EDA and Machine Learning Models](https://www.kaggle.com/code/benyamingheiji/eda-data-analysis-7-machine-learning-models)
- **GitHub Repository**: [Heart Failure Prediction](https://github.com/BenyGH2003/heart_failure_prediction/tree/main)

## Dataset
The dataset used in this project is the **Heart Failure Clinical Records Dataset** (`heart_failure_clinical_records_dataset.csv`), which contains data on clinical features and heart failure outcomes. The dataset includes:
- 12 clinical features such as age, ejection fraction, and serum creatinine.
- A target variable indicating if the patient experienced heart failure.

For more information on the dataset, refer to [Kaggle](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data).

## Files in the Repository
- **`eda-data-analysis-7-machine-learning-models.ipynb`**: The main Jupyter Notebook containing analysis, visualization, and model building.
- **`heart_failure_clinical_records_dataset.csv`**: The dataset used for EDA and training machine learning models.
- **`app.py`**: The Python script for deploying the Streamlit web application.
- **`svc.joblib`**: The trained Support Vector Classifier (SVC) model saved as a `.joblib` file. This model is used in the web app for real-time predictions.
- **`README.md`**: This documentation file.

## Features
1. **Exploratory Data Analysis (EDA)**:
   - Detailed visualization of the dataset.
   - Feature engineering and correlation analysis.
   
2. **Machine Learning Models**:
   - Implementation and comparison of 7 machine learning models.
   - Hyperparameter tuning and evaluation metrics.

3. **Streamlit Web App**:
   - Interactive user interface for predicting heart failure risk.
   - Simple and user-friendly design.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/BenyGH2003/heart_failure_prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the web app locally:
   ```bash
   streamlit run app.py
   ```
4. Alternatively, visit the deployed [web app](https://heartfailureprediction-nk7dudqu5hffqkkby6kxqg.streamlit.app/).

## How It Works
1. The dataset (`heart_failure_clinical_records_dataset.csv`) is loaded and processed for training and prediction.
2. Machine learning models, including an SVC, are trained and evaluated.
3. The best-performing model is saved as `svc.joblib`.
4. The `app.py` script uses the saved model to provide real-time predictions via the Streamlit web app.

## How to Contribute
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
