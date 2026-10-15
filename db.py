import sqlite3
DATABASE = "database.db"
def problem_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS problem (title,url,memo)")
    con.close()

if __name__ == "__main__":
    problem_books_table()