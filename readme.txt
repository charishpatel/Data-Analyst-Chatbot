# For Python 3.x
python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

set OPENAI_API_KEY =  your-api-key-here

chainlit run main.py



docker build -t my-chainlit-app .


docker run -e OPENAI_API_KEY="openai api key here" -p 8080:8080 my-chainlit-app



