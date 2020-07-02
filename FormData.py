from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'patientkanchan@gmail.com'
app.config['MAIL_PASSWORD'] = 'testgadha'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def medicalhome():
   return render_template('medicalhome.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      med1 = request.form['Med1']
      med2 = request.form['Med2']
      med3 = request.form['Med3']
      med4 = request.form['Med4']
      med5 = request.form['Med5']
      msg = Message('Medicine Order', sender = 'patientkanchan@gmail.com', recipients = ['pharmacyrecipient@gmail.com'])
      msg.body = "Please create the order for the following medecines:\n"+ med1 + "\n" + med2 + "\n" + med3 + "\n" + med4 + "\n" + med5 + "\n\n" + "Thank you"
      mail.send(msg)
   return render_template("medicalhome.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      emailaddress = request.form['emailaddress']
      emailmessage  = request.form['emailmessage']
      msg = Message('Hello', sender = 'patientkanchan@gmail.com', recipients = [emailaddress])
      msg.body = emailmessage
      mail.send(msg)
      return render_template("medicalhome.html")

@app.route('/questions',methods = ['POST', 'GET'])
def question():
   if request.method == 'POST':
      emailmessage  = request.form['question']
      msg = Message('Hello', sender = 'patientkanchan@gmail.com', recipients = ['pharmacyrecipient@gmail.com'])
      msg.body = "Hi,I have a quick question:\n"+ emailmessage
      mail.send(msg)
      return render_template("medicalhome.html")


@app.route('/feedback',methods = ['POST', 'GET'])
def feedback():
   if request.method == 'POST':
      emailmessage  = request.form['feedback']
      msg = Message('Hello', sender = 'patientkanchan@gmail.com', recipients = ['pharmacyrecipient@gmail.com'])
      msg.body = "Hi,I have some feedback:\n"+ emailmessage
      mail.send(msg)
      return render_template("medicalhome.html")

@app.route('/createaccount',methods = ['POST', 'GET'])
def createaccount():
   if request.method == 'POST':
      firstname  = request.form['firstname']
      lastname  = request.form['lastname']
      dateofbirth  = request.form['dob']
      address  = request.form['address']
      phone  = request.form['phone']
      msg = Message('Hello', sender = 'patientkanchan@gmail.com', recipients = ['pharmacyrecipient@gmail.com'])
      msg.body = "Hi,Please create an account for:\n"+ firstname + " " + lastname
      mail.send(msg)
      return render_template("medicalhome.html")
   
if __name__=="__main__":
    app.run(host='127.0.0.1',port=4455,debug=True)
