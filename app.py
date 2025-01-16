from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def form():
    if request.method=="POST":
        email=request.form["email"]
        print(email)
        return redirect(url_for("welcome",name=email))
    return render_template("index.html")

@app.route("/welcome/<name>")
def welcome(name):
    return "welcome %s"%name

if __name__ == "__main__":
    app.run(debug=True)