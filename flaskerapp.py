import datetime
from flask import Flask, request, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, DateTime
from passlib.hash import sha256_crypt

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
db  = SQLAlchemy(app)

class Pin(db.Model):
    id    = Column(Integer,primary_key=True)
    title = Column(Text,unique=False)
    image = Column(Text,unique=False)

class User(db.Model):

    id         = Column(Integer,primary_key=True)
    username   = Column(Text,unique=True)
    password   = Column(Text,unique=False)
    createdAt  = Column(DateTime)

db.create_all()


@app.route('/template/', methods=['GET', 'POST'])
def index():
   #return render_template("form_submit.html")'
   if request.method == "POST":
       command = request.form['expression']
       return command
   return render_template('index.html')

@app.route('/submit/')
def submit():
    return  render_template('form_submit.html')

@app.route('/action/',methods=['GET','POST'])
def imgposter():
    if request.method == "POST":
      name  = request.form['yourname']
      email = request.form['youremail']
      pin1 = Pin(title=name,image=22)
      db.session.add(pin1)
      db.session.commit()
    return render_template('form_action.html',name=name,email=email)

@app.route('/inpage',methods=['GET','POST'])
def inpage():
    if request.method == "POST":
        text = request.form['yourname']
        passd = sha256_crypt.encrypt((str(request.form['yourpass'])))
        user = User(username=text,password=passd,createdAt=datetime.datetime.utcnow())
        db.session.add(user)
        db.session.commit()

    return render_template('inpage_form_submit.html')


@app.route('/displayid/<int:userid>/',methods=['GET'])
def displayid(userid):
   # userid = request.form['']
    u = User.query.get(userid)
    username = u.username
    return render_template('display_id.html',userid=u.id,username=username)


if __name__ == '__main__':
    app.debug = True
    app.run()
