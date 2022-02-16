from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd




app = Flask(__name__)
# configuration sqlalchemy 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datamart.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

class Datamart(db.Model):
    SerialNo = db.Column(db.Integer,primary_key = True,autoincrement=True)
    Table_Name = db.Column(db.String(400),nullable = False)
    #date_inserted_on = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    Last_updated = db.Column(db.String(200), nullable=True)
    Max_Latest_Record = db.Column(db.String(200), nullable=True)
    Count = db.Column(db.BigInteger, nullable=True)

    def __repr__(self) -> str:
        return f"{self.sro} - {selt.table}"

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        #tbl = request.form['table']
        print("post")
    #Datamart.objects.all().delete()
    df=pd.read_csv('D:\\PythonCode\\Django\\data_Mart_Schedule.csv',index_col=False)

    #p1=df.drop(df.index[49:90])
    p1 = df.dropna(how='all')
    p2=p1.drop(columns=['Unnamed: 4'])
    #p3=p2.to_dict()
    index = df.index
    cnt=0
    for i,j in p2.iterrows():
        obj=Datamart(Table_Name= j['Table Name'],Last_updated= j['Last Updated'],Max_Latest_Record= j['Max_Latest_ Record'],Count= j['           Count'])
        if cnt <= len(index):
            db.session.add(obj)
            db.session.commit()
            cnt = cnt+1
        #Last_updated= Datamart(Last_updated= j['Last Updated'])
        #Max_Latest_Record= Datamart(Max_Latest_Record= j['Max_Latest_ Record'])
        #Count= Datamart(Count= j['           Count'])
        #db.session.add(table)
        #db.session.commit()
        #db.session.add(Last_updated)
        #db.session.commit()
        #db.session.add(Count)
        #db.session.commit()
        #db.session.add(Max_Latest_Record)
       # db.session.commit()   
    alldata = Datamart.query.all()
    
    return render_template('index.html',alldata=alldata)
    #return "<p>Hello, World!</p>"



@app.route("/show")
def products():
    return "this is products page"


if __name__ == "__main__":
    app.run(debug=True)