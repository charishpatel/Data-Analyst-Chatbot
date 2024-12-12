import pandas as pd
import openai
import chainlit as cl
import os
from helpers import get_columns_information, code_executer, gpt_reply

# Initialize OpenAI API key and model
#openai.api_key_path = "openaikey.txt"

# Retrieve the API key from the environment variable

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is not set!")


model_name = "gpt-3.5-turbo"
settings = {
    "temperature": 1,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

df = None

# Prompts for different modes
dataset_prompt = """
You are a great assistant at Python DataFrame analysis. You will reply to the user's messages and provide the user with the necessary information.
The user will ask you to provide the code to answer any question about the dataset.
Besides, Here are some requirements:
1: The pandas DataFrame is already loaded in the variable "df".
2: Do not load the DataFrame in the generated code!
3: The code has to save the figure of the visualization in an image called img.png; do not use plot.show().
4: Give explanations along with the code about how important the visualization is and what insights we can derive.
5: If the user asks for suggestions for analysis, just provide possible analysis without the code.
6: For any visualizations, write only one block of code.
7: The available fields in the dataset "df" and their types are: {}
"""

general_prompt = """
You are a helpful and friendly assistant. You can answer general questions, chat about various topics, and provide advice or information. Keep responses concise and engaging.
"""

@cl.on_chat_start
async def start_chat():
    # Send a welcoming message
    welcome_message = """
    **🎉 Welcome to the Data Analysis Assistant! 🎉**

    I am currently in **Data Analysis** mode by default. You can:
    - Ask me questions about your dataset 📊
    - Request visualizations or insights from your data 🔍

    **To switch modes, type:**
    - `Switch to General Chat` to talk about general topics 💬
    - `Switch to Data Analysis` to return to data analysis 📈
    """
    await cl.Message(content=welcome_message).send()

    # Wait for a dataset upload
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload your CSV/XLSX dataset file to begin data analysis!", accept=["csv", "xlsx"], max_size_mb=100
        ).send()

    # Decode and load the dataset
    text_file = files[0]
    text = text_file.content
    f = open(text_file.path, "wb")
    f.write(text)
    f.close()
    global df
    if "csv" in text_file.path:
        df = pd.read_csv(text_file.path)
    else:
        df = pd.read_excel(text_file.path, index_col=0)

    # Notify user of the successful upload
    await cl.Message(
        content=f"`{text_file.name}` uploaded successfully!\nIt contains {df.shape[0]} Rows and {df.shape[1]} Columns with the following fields:\n{get_columns_information(df)}"
    ).send()

    # Save dataset prompt with field info
    system_message = dataset_prompt.format(get_columns_information(df))
    cl.user_session.set("dataset_prompt", system_message)
    cl.user_session.set("general_prompt", general_prompt)

    # Set default mode to Data Analysis
    cl.user_session.set("mode", "Data Analysis")


@cl.on_message
async def main(message: str):
    # Check for toggle commands
    if message.lower() == "switch to data analysis":
        cl.user_session.set("mode", "Data Analysis")
        await cl.Message(content="You are now in **Data Analysis** mode. Ask me questions about your dataset! 📊").send()
        return
    elif message.lower() == "switch to general chat":
        cl.user_session.set("mode", "General Chat")
        await cl.Message(content="You are now in **General Chat** mode. Feel free to ask me anything! 💬").send()
        return

    # Retrieve the current mode
    mode = cl.user_session.get("mode")
    system_message = (
        cl.user_session.get("dataset_prompt") if mode == "Data Analysis" else cl.user_session.get("general_prompt")
    )

    # Delete any existing image
    try:
        os.remove("img.png")
    except FileNotFoundError:
        pass

    # Response from the OpenAI model
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": message}],
        stream=False, **settings
    )

    # Get response text
    gpt_response = response['choices'][0]['message']['content']

    # If in Data Analysis mode, execute code
    elements = []
    if mode == "Data Analysis":
        has_code = code_executer(gpt_response, df)  # Pass df as a parameter
        if os.path.exists("./img.png"):
            elements = [
                cl.Image(name="image1", display="inline", size="large", path="./img.png")
            ]
        if has_code:
            infos = has_code
            result = gpt_reply(infos, message)
            await cl.Message(content=result, elements=elements).send()
        else:
            await cl.Message(content=gpt_response, elements=elements).send()
    else:
        # General Chat mode
        await cl.Message(content=gpt_response).send()
