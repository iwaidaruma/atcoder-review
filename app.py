from flask import Flask, render_template , request

app = Flask(__name__)


@app.route("/") #webアプリのトップURLにリクエストが来たらindex()
def index():
    return render_template("index.html")

@app.route("/new",methods=["GET","POST"]) #GET or POSTの要求が来たらnew()を呼ぶ
def new():
    p_name = None
    p_url = None
    p_memo = None
    if request.method == "POST":
        p_name = request.form.get("problem_name")
        p_url = request.form.get("problem_url")
        p_memo = request.form.get("problem_memo")
    
    return render_template("new.html", problem_name=p_name,problem_url=p_url,problem_memo=p_memo)