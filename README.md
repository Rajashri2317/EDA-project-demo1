# Titanic Dataset – Exploratory Data Analysis (EDA) and Data Preprocessing
📌 Project Overview

This project focuses on Exploratory Data Analysis (EDA) and data preprocessing using the Titanic dataset.

The main objective is to understand the dataset, explore relationships between different passenger attributes, handle data preprocessing, and apply feature transformation techniques using Python libraries.

The project also demonstrates how to use Scikit-learn preprocessing tools, custom functions, and Pickle to save and reuse processed data.

🎯#Objectives
Understand and explore the Titanic dataset.
Perform data inspection and analysis.
Identify missing values and handle data preprocessing.
Apply feature scaling and encoding techniques.
Use ColumnTransformer for handling different types of features.
Create custom transformation functions.
Save and load processed data using Pickle.
Understand how to reuse preprocessing transformations.
#📂 Project Structure
text
EDA-project-demo1/
│
├── Titanic.pkl
├── custom_functions.py
├── pickle.ipynb
├── processed_data.ipynb
├── processed_data.pkl
├── train (1).xls
├── transformer_pickle_demo (1).ipynb
│
└── README.md

#🛠️ Technologies Used
Python
Jupyter Notebook
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Pickle
📊 Dataset Description

The project uses the Titanic passenger dataset.

It contains information about passengers, including:

Feature	Description
PassengerId	Unique passenger ID
Survived	Survival status (0 or 1)
Pclass	Passenger class
Name	Passenger name
Sex	Gender
Age	Passenger age
SibSp	Number of siblings/spouses aboard
Parch	Number of parents/children aboard
Ticket	Ticket number
Fare	Ticket fare
Cabin	Cabin number
Embarked	Port of embarkation
🔍 Project Workflow
1. Data Loading
Import the required Python libraries.
Load the Titanic dataset using Pandas.
Inspect the dataset structure.
2. Exploratory Data Analysis
Understand the dataset using statistical summaries.
Explore numerical and categorical features.
Examine relationships between passenger attributes.
3. Data Preprocessing
Identify missing values.
Prepare numerical and categorical features.
Apply suitable preprocessing techniques.
4. Feature Transformation

The project demonstrates the use of Scikit-learn preprocessing methods:

StandardScaler
LabelEncoder
OneHotEncoder
OrdinalEncoder
ColumnTransformer
FunctionTransformer
5. Custom Functions

The custom_functions.py file contains custom transformation functions that can be reused during preprocessing.

6. Pickle Implementation

Pickle is used to serialize and deserialize Python objects.

The project includes .pkl files to demonstrate saving and loading processed datasets and preprocessing objects.

⚙️ Installation and Setup
Step 1: Clone the repository
bash
git clone https://github.com/Rajashri2317/EDA-project-demo1.git

Step 2: Navigate to the project directory
bash
cd EDA-project-demo1

Step 3: Install the required libraries
bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter xlrd

Step 4: Launch Jupyter Notebook
bash
jupyter notebook

Step 5: Run the notebooks

Open the notebooks in Jupyter:

transformer_pickle_demo (1).ipynb
processed_data.ipynb
pickle.ipynb

Run the cells sequentially to explore the preprocessing and Pickle demonstrations.

Note: Ensure that the dataset filename and file path used in each notebook match the files available in the repository.

💡 Key Learnings
Understanding and exploring real-world datasets.
Data cleaning and preprocessing techniques.
Feature encoding and scaling.
Using ColumnTransformer for feature transformation.
Creating custom preprocessing functions.
Saving and loading Python objects using Pickle.
Reusing preprocessing objects in data workflows.
🚀 Future Improvements
Perform more detailed visual analysis.
Add additional data visualization techniques.
Build a machine learning model to predict Titanic passenger survival.
Evaluate model performance using suitable metrics.
Improve the preprocessing pipeline.
👩‍💻 Author

Rajashri

GitHub: https://github.com/Rajashri2317

📄 License

This project is intended for educational and learning purposes.
