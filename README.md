# Data-Analyst-Chatbot

## Chainlit DataFrame Analysis & General Bot
This app is a Chainlit-powered chatbot with two main modes: a Data Analyst and a General Bot. It helps you analyze your datasets and also answers general questions. You can upload CSV or Excel files, and the assistant will generate code, provide insights, and visualize data.

### Features
Data Analyst Mode:

** Upload a CSV or Excel file.
** Get Python code to analyze your dataset.
** Visualize data and save plots as images (img.png).
** Get insights and explanations for the visualizations.
    
General Bot Mode:

* Ask general questions, and the bot will provide helpful answers based on its knowledge.

Requirements -

    Python 3.x
    pandas
    matplotlib
    openai
    chainlit


# How to Run Using Python Environment

open command prompt in folder

### Create a Virtual Environment:

For Python 3.x:

write command

    python -m venv myenv

### Activate the Environment:

        
    myenv\Scripts\activate

### Install Dependencies:

    pip install -r requirements.txt

### Set Your OpenAI API Key as environment:

    set OPENAI_API_KEY=your-api-key-here

### Run the App:

    chainlit run main.py

# How to run using Docker

Build the Docker Image:

    docker build -t my-chainlit-app .

Run the Docker Container:

    docker run -e OPENAI_API_KEY="your-api-key-here" -p 8080:8080 my-chainlit-app

# Output images from chatbot

![image1](https://github.com/user-attachments/assets/c2fe320c-2e44-4544-b512-577c7b887ab0)

![WhatsApp Image 2024-12-12 at 6 12 08 PM](https://github.com/user-attachments/assets/8e3ef70c-cfdc-47ba-b5b8-64f1962e6f5d)

![WhatsApp Image 2024-12-12 at 6 12 53 PM](https://github.com/user-attachments/assets/28833c57-6c7f-4847-a5f3-e9470e5359d8)

![WhatsApp Image 2024-12-12 at 6 13 29 PM](https://github.com/user-attachments/assets/ad25a7ef-1708-43b2-94fd-bd3b2365f802)

![WhatsApp Image 2024-12-12 at 6 13 40 PM](https://github.com/user-attachments/assets/6d691274-2fa7-4dbf-ad69-aad17a1d8b9f)

![WhatsApp Image 2024-12-12 at 6 14 03 PM](https://github.com/user-attachments/assets/8ba20114-9ef8-4a91-bc61-ea6b4f182be5)

![WhatsApp Image 2024-12-12 at 6 14 13 PM](https://github.com/user-attachments/assets/7bfb015a-3d60-4d54-8573-11491b1a29b0)

![WhatsApp Image 2024-12-12 at 6 14 41 PM](https://github.com/user-attachments/assets/8d9231ef-8084-4fad-83a8-4960e5ce857f)





















