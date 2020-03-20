import os
import math


from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])

def tempCalculate():
  temp = ""
  speed = ""
  

  if request.method == 'POST':
temp    = float(input("Enter the air temperature in (degrees Celsius): "))
speed   = float(input("Enter the wind speed (kilometer per hour): "))

windchill = 13.12 + 0.6215*temp -  11.37*math.pow(speed, 0.16) + 0.3965*temp*math.pow(speed, 0.16)

temp = float(request.form["temp"])
speed = float(request.form["speed"])
  
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)
  if 'times' not in session:
    session['times'] = 0
  session['times'] += 1

  return render_template('windchill.html',times = session['times'] , temp = temp, speed = speed , windchill = windchill) # Send t to the template

@app.route('/logout')
def logout():
  #session.clear()
  return redirect(url_for('tempCalculate'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
