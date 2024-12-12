import pandas as pd
import sys
import io
import re
import openai

def get_columns_information(df): 
    # Get the column names and their value types
    column_types = df.dtypes
    # Convert the column_types Series to a list
    column_types_list = column_types.reset_index().values.tolist()
    infos = ""
    # Print the column names and their value types
    for column_name, column_type in column_types_list:
        infos += "{}({}),\n".format(column_name, column_type)
    return infos[:-1]

def gpt_code_extract(gpt_response): #extract_code
    pattern = r"```(.*?)```"
    matches = re.findall(pattern, gpt_response, re.DOTALL)
    if matches:
        return matches[-1]
    else:
        return None

def filter_excel_rows(text): 
    # Split the input string into individual rows
    lines = text.split('\n')
    filtered_lines = [line for line in lines if "pd.read_csv" not in line and "pd.read_excel" not in line and ".show()" not in line]
    filtered_text = '\n'.join(filtered_lines)
    return filtered_text

def code_executer(gpt_response, df):  #code_executer
    if "```" in gpt_response:
        just_code = gpt_code_extract(gpt_response)

        if just_code.startswith("python"):
            just_code = just_code[len("python"):]

        just_code = filter_excel_rows(just_code)
        print("CODE part:{}".format(just_code))

        # Interpret the code
        print("Interpret the code")

        # Redirect standard output to a string buffer
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            exec(just_code)
        except Exception as e:
            sys.stdout = old_stdout
            return str(e)

        # Restore original standard output
        sys.stdout = old_stdout

        # Return captured output
        return new_stdout.getvalue().strip()

    else:
        return False

def gpt_reply(infos, text):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        temperature=0.10,
        max_tokens=512,
        messages=[
            {"role": "system", "content": f"Reply to the user questions using the informations you have contained in INFOS:\"\"\"{infos}\"\"\""},
            {"role": "user", "content": f"{text}"}
        ]
    )['choices'][0]['message']['content']
