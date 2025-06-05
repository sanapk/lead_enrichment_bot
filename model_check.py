import google.generativeai as genai

genai.configure(api_key='AIzaSyBUmIdfgB7_5V5OQ3nvaX0XKoXu7ZSfNgI')
models = genai.list_models()

for model in models:
    print(model.name)
