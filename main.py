# Import
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables that allow for the calculation of the appliances' energy draw
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# The first page
@app.route('/')
def index():
    return render_template('index.html')
# The second page
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# The third page
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Calculation
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# The form
@app.route('/form')
def form():
    return render_template('form.html')

#The form's results
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declare variables for the data collection
    name = request.form['name']

    # You can save your data or email it
    return render_template('form_result.html', 
                           # Place the variables here
                           name=name,
                           )

app.run(debug=True)
