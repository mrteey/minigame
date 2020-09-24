from flask import Flask, request, session, redirect, render_template, flash

import random

app = Flask(__name__)

app.secret_key = "kjshfdjkhdfsjkhkjlhsz82932389"

@app.route('/')
def index():
    return 'Welcome to the index page lol'

@app.route('/login')
def login():
    return 'Welcome to the login page'

@app.route('/start')
def start():
    session['states'] = {'Abia':'Umuahia', 'Anambra': 'Awka', 'Akwa Ibom':'Uyo', 'Adamawa':'Yola', 'Bauchi':'Bauchi', 'Bayelsa':'Yenagoa', 'Benue':'Makurdi', 'Borno':'Maiduguri', 'Cross River':'Calabar', 'Delta':'Asaba', 'Ebonyi':'Abakaliki', 'Edo':'Benin', 'Ekiti':'Ado-Ekiti', 'Enugu':'Enugu', 'Gombe':'Gombe', 'Imo':'Owerri', 'Jigawa':'Dutse', 'Kaduna':'Kaduna', 'Kano':'Kano', 'Katsina':'Katsina', 'Kebbi':'Birnin Kebbi', 'Kogi':'Lokoja', 'Kwara':'Ilorin', 'Ogun':'Abeokuta', 'Ondo':'Akure', 'Osun':'Osogbo', 'Oyo':'Ibadan', 'Plateau':'Jos', 'Rivers':'Porthacourt', 'Sokoto':'Sokoto', 'Taraba':'Jalingo', 'Yobe':'Damaturu', 'Zamfara':'Gusau', 'FCT':'Abuja'}
    state = random.choice(list(session['states']))
    question = f'What is the capital of {state}?'
    if 'score' not in session:
        session['score'] = 0
    # html = f"""<p>{question}<p> <form method='POST' action='/submit'><input type='text' name='answer' placeholder='your answer'> <input name='state' value='{state}' hidden> <br> <input type='submit'> <p>Score: {session['score']}</p></form>"""
    # return html
    return render_template('start.html', state=state)

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form.get('answer')
    state = request.form.get('state')
    if answer.lower() == session['states'][state].lower():
        session['score']+=1
        flash('correct')
    else:
        session['score']-=1
        flash([state, session['states'][state]])
    return redirect('start')

if __name__ == '__main__':
    app.run(debug=True, port='5553')
