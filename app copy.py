from flask import Flask,render_template,request
import pickle as pkl
from artifacts import model.pkl as mdl
model = pkl.load(open(r"artifacts/model.pkl","rb"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    # return "SUCCESS"

@app.route("/predict", methods = ["POST","GET"])
def student():
    var_cgpa = float(request.form.get("cgpa"))
    var_iq = int(request.form.get("iq"))
    var_ps = int(request.form.get("ps"))

    print(f"{var_cgpa},{var_iq},{var_ps}")
    

    result = mdl.predict([[var_cgpa,var_iq,var_ps]])
    print(result[0])
    return "PLACED"


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)

# PORT NUMBER BY DEFAULT FOR LOCAL SYSTEM IS 5000
# HOST NUMBER BY DEAFAULT FOR LOCAL SYSTEM IS 127.0.0.1