# Data-Analyst-Chatbot

## Chainlit DataFrame Analysis & General Bot
This app is a Chainlit-powered chatbot with two main modes: a Data Analyst and a General Bot. It helps you analyze your datasets and also answers general questions. You can upload CSV or Excel files, and the assistant will generate code, provide insights, and visualize data.

### Features
Data Analyst Mode:

    Upload a CSV or Excel file.
    Get Python code to analyze your dataset.
    Visualize data and save plots as images (img.png).
    Get insights and explanations for the visualizations.
    
General Bot Mode:

Ask general questions, and the bot will provide helpful answers based on its knowledge.

Requirements -

Python 3.x
pandas
matplotlib
openai
chainlit


### How to Run
Using Python Environment

open command prompt in folder

### Create a Virtual Environment:

For Python 3.x:

hit command - python -m venv myenv

### Activate the Environment:

On Windows:
myenv\Scripts\activate

### Install Dependencies:

pip install -r requirements.txt

### Set Your OpenAI API Key as environment:

set OPENAI_API_KEY=your-api-key-here

### Run the App:

chainlit run main.py
