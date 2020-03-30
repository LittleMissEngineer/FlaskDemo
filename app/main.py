import os
import random

from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])

def game():
  t = {'currentGuess': 0}
  secret_number = random.randint(1,101)
  print(secret_number)
  response = ""
  
  #if request.method == 'POST':
   # currentGuess = request.form['userGuess']

  if 'currentGuess' in request.args:
   t['currentGuess'] = request.args.get('currentGuess')

  
#loop to determine if input is higher or lower

  if secret_number > int(t['currentGuess']) :
    response = "Your guess is too low"

  elif secret_number < int(t['currentGuess']) :
      response = "Your guess is too high"

  else:
     response = "Congratulations! Your guess is correct"


  



  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)
  if 'times' not in session:
    session['times'] = 0
  session['times'] += 1

  return render_template('index.html',t = t,times = session['times'], response = response ) # Send t to the template

@app.route('/logout')
def logout():
  #session.clear()
  return redirect(url_for('game'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
