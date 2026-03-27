from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="schools"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    db.commit()
    cursor.close()
    return redirect('/students')

@app.route('/students')
def students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    cursor.close()
    return render_template("students.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)


    