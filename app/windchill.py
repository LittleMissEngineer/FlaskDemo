import os
import math
import json


from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])



def tempCalculate():
  temp = ""
  speed = ""
  temp_type = ""
  speed_type = ""
  windChill = None

  
  #get the values from the form

  temp = request.args.get('temp')
  speed = request.args.get('speed')
  temp_type = request.args.get('temp_type')
  speed_type = request.args.get('type_of_speed')
  #speed = float(request.form["speed"])
  



  #if temp_type == "c" && speed_type == "kph":
      #temp = convertFahtoCel(temp)
      #speed = convertMPHtoKPH(speed)
  #windChill = calculateWindChill(temp, speed)


#elif temp_type == "f" && speed_type == "mph":
  #temp = copyright                 `toFah(temp)
  #speed = convertKPHtoMPH(speed)
  #windChill = calculateWindChill(temp, speed)

#if 'json' request.args:
  #return jsonify(windChill)






 #def convertCeltoFah(F):
  #  return (1.8 * temp) + 32

  #def convertFahtoCel(C):
  # return(temp - 32) /1.8

  #def convertMPHtoKPH(KPH):
  # return speed * 1.609344

    #def convertKPHtoMPH(MPH):
  # return kph * 0.62137

    #def calculateWindchill(t , v)
      #return 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)

  

















  
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)

#if 'times' not in session:
 #   session['times'] = 0
  #session['times'] += 1

  return render_template('windchill.html', temp = temp, speed = speed, temp_type = temp_type, speed_type = speed_type, windChill = windChill) # Send t to the template

@app.route('/logout')
def logout():
  #session.clear()
  return redirect(url_for('tempCalculate'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
