import os
import math
import json


from flask import Flask, request, redirect, render_template, flash, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/')
def form():
  return render_template('windchill.html')


@app.route('/', methods=['GET','POST'])
def tempCalculate():
  temp = 0.0
  speed = 0.0
  temp_type = ""
  speed_type = ""
  temp_option = None
  speed_option = None
  windChill = None

  
  #get the values from the form

  #temp = request.args.get('temp')
  #temp = request.form['temp']
  #speed = request.form['speed']
  #temp_option = request.form['temp_option']
  #speed_option = request.form['speed_option']
  #temp_type = request.args.get('temp_type')
  #speed_type = request.args.get('type_of_speed')
  #speed = float(request.form["speed"])

  if request.method == 'POST':
    if 'submit_button' in request.form:
      temp = float(request.form['temp'])
      speed = float(request.form['speed'])
      temp_option = request.args.get('temp_option')
      speed_option = request.args.get('speed_option')
      #return speed_option

      if temp_option == "c":
        temp = convertFahtoCel(temp)
        if speed_option == "kph":
          speed = convertMPHtoKPH(speed)
          windChill = calculateWindchill(temp, speed)
          #return float(windChill)
      elif temp_option == "f":
          temp = convertCeltoFah(temp)
          if speed_option == "mph":
            speed = convertKPHtoMPH(speed)
            windChill = calculateWindchill(temp, speed)
            

#if 'json' request.args:
  #return jsonify(windChill)

      return render_template('windchill.html', temp = temp, speed = speed, temp_type = temp_type, temp_option = temp_option, speed_option = speed_option) # Send t to the template




def convertCeltoFah(temp):
  return (1.8 * temp) + 32

def convertFahtoCel(temp):
  return(temp - 32) /1.8

def convertMPHtoKPH(speed):
  return speed * 1.609344

def convertKPHtoMPH(speed):
  return kph * 0.62137

def calculateWindchill(temp , speed):
  return 13.12 + 0.6215*temp -  11.37*math.pow(speed, 0.16) + 0.3965*temp*math.pow(speed, 0.16)

  

















  
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)

#if 'times' not in session:
 #   session['times'] = 0
  #session['times'] += 1

  #return render_template('windchill.html', temp = temp, speed = speed, temp_type = temp_type, temp_option = temp_option, speed_option = speed_option) # Send t to the template

@app.route('/logout')
def logout():
  #session.clear()
  return redirect(url_for('tempCalculate'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
