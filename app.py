from flask import Flask, render_template , request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new")
def new():
    p_name = request.args.get("problem_name")
    p_url = request.args.get("problem_url")
    p_memo = request.args.get("problem_memo")
    print(p_name)
    return render_template("new.html", problem_name=p_name,problem_url=p_url,problem_memo=p_memo)