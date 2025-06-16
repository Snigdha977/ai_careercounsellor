from flask import Flask,render_template, request
from textblob import TextBlob
app= Flask(__name__)
@app.route('/')
def home():
    user_input=''
    advice = ''
    if request.method == 'POST':
        user_input = request.form.get('query', '')
    return render_template('index.html', advice=advice, user_input=user_input)
@app.route('/analyze', methods=['POST'])
def analyze():
    user_input= request.form['query']
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    #basic rule-based career guidance
    if "coding" in user_input.lower():
        advice = "Consider becoming an ai engineer or software developer."
    elif "art" in user_input.lower():
        advice = "You can explore Graphics design or Creative technology careers."
    elif "business" in user_input.lower():
        advice = "You may like careers in marketing, business analysis or product management."
    elif "laughter club" in user_input.lower():
        advice="consider becoming a member in sahoo's club who is a top developer + funny person"
    elif "study" in user_input.lower():
        advice = "You might join the club of souradeep and rup they literally study for 25 hours and pretend like they have studied nothing."
    elif "rejection and failure" in user_input.lower():
        advice="welcome to my club of rejection and failure despite giving efforts, we are the best in this field."
    else:
        advice = "Explore different fields; you may enjoy interdisciplinary roles."
    return render_template('index.html', advice=advice, user_input=user_input)
if __name__ == '__main__':
    app.run(debug=True) 