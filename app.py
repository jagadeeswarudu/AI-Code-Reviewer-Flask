from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

def result(code):
    key = "AIzaSyAHi-rg6OcKjfcXm-QNYrOP7HXVJE-xMYE"
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    prompt = f"""You are an expert Python developer. Please review the following code for bugs, errors, or inefficiencies:
    code is: {code}
    Provide bug report and fixed code only."""
    response = model.generate_content(prompt)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    review = None
    if request.method == 'POST':
        code = request.form['code']
        if code:
            review = result(code)
    return render_template('index.html', review=review)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
