import os
import random

from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])

def game():
  secret_number = random.randrange(1,100)
  response = ""
  lower = "Your guess is too low"
  higher = "You guess is too high"
  correct = "Congrats! You have guessed correctly!"

  if 'userGuess' in request.args:
    userGuess = int(input('userGuess'))

    if userGuess > secret_number:
     response = lower

    elif userGuess < secret_number:
         response = higher

    else:
      response = correct


  userGuess = request.form['userGuess']
    
  
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)
  if 'times' not in session:
    session['times'] = 0
  session['times'] += 1

  return render_template('index.html',times = session['times'] , response = response , lower= lower , higher = higher , correct = correct) # Send t to the template

@app.route('/logout')
def logout():
  #session.clear()
  return redirect(url_for('game'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
