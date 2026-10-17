from flask import Flask, render_template , request,redirect,url_for
import sqlite3
DATABASE = "database.db"

app = Flask(__name__)


@app.route("/") #webアプリのトップURLにリクエストが来たらindex()
def index():
    
    pyt_problems = []
    con = sqlite3.connect(DATABASE)
    db_problem = con.execute("SELECT rowid,title,url,memo FROM problem").fetchall() #pythonのリストオブジェクト
    con.close()
    for row in db_problem:
        pyt_problems.append({"id":row[0],"title":row[1],"url":row[2],"memo":row[3]})

    return render_template("index.html",html_problems=pyt_problems) #html側で使う変数にpyt_problemを代入

@app.route("/new",methods=["GET","POST"]) #GET or POSTの要求が来たらnew()を呼ぶ
def new():

    p_title = None
    p_url = None
    p_memo = None
    
    if request.method == "POST":
        
        p_title = request.form.get("new_problem_title") #引数はhtml側のname
        p_url = request.form.get("new_problem_url")
        p_memo = request.form.get("new_problem_memo")
        
        con = sqlite3.connect(DATABASE)
        con.execute("INSERT INTO problem VALUES(?,?,?)",[p_title,p_url,p_memo])
        con.commit()
        con.close()

        return redirect(url_for("index"))
        
    return render_template("new.html", problem_title=p_title,problem_url=p_url,problem_memo=p_memo)

@app.route("/delete",methods=["POST"])
def delete():
    p_id= request.form.get("del_problem_id")
    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM problem WHERE rowid = ?",[p_id])
    con.commit()
    con.close()
    return redirect(url_for("index"))

@app.route("/edit",methods=["GET","POST"])
def edit():
    id = request.args.get("problem_id",type=int) #URLから取得
    con = sqlite3.connect(DATABASE)
    row = con.execute("SELECT rowid,title,url,memo FROM problem WHERE rowid = ?",[id]).fetchone() #row = (id,title,url,memo)
    con.close()
    if row is None:
        return "問題が見つかりません"
    pyt_edi_prob={"id":row[0],"title":row[1],"url":row[2],"memo":row[3]}

    if request.method == "POST":
        edi_title = request.form.get("new_title")
        edi_url   = request.form.get("new_url")
        edi_memo  = request.form.get("new_memo")

        con = sqlite3.connect(DATABASE)
        con.execute("UPDATE problem SET title = ?,url = ?,memo = ? WHERE rowid = ?",[edi_title,edi_url,edi_memo,id])
        con.commit()
        con.close()
        return redirect(url_for("index"))
    
    return render_template("edit.html",html_edi_prob=pyt_edi_prob)
