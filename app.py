from flask import Flask , render_template, request
import pandas as pd
import model

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html");



@app.route("/", methods = ['GET','POST'])
def submit():
    #html -> .py
    if request.method =="POST": 
        Arg1 = request.form["arg_1"]
        Arg2 = request.form["arg_2"]
        Arg3 = request.form["arg_3"]
        Arg4 = request.form["arg_4"]
        Arg5 = request.form["arg_5"]
        Arg6 = request.form["arg_6"]
        Arg7 = request.form["arg_7"]
        Arg8 = request.form["arg_8"]
        Arg9 = request.form["arg_9"]
        Arg10 = request.form["arg_10"]

    new_data = pd.DataFrame([[Arg1,Arg2,Arg3,Arg4,Arg5,Arg6,Arg7,Arg8,Arg9,Arg10]],
        columns=['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status' ])
    
    Result = model.dtree.predict(new_data)
    print(Result)
    #.py -> html
    return render_template("index.html", predict = Result)


if __name__ == "__main__":
    app.run(debug = True)