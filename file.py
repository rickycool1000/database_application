from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_1:test@localhost/first_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"id : {self.id} name : {self.name} email : {self.email}"


@app.route("/insert")
def index():
    data = Data(name="Ritik",email="ritik@gmail.com")
    db.session.add(data)
    db.session.commit()
    return "Done"  

@app.route("/show")
def index2():
    data = Data.query.all()
    print(data)
    return "Done" 

if __name__ == "__main__":
    app.run(debug=False,port=5000,host='0.0.0.0')
