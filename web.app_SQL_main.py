from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/create_account', methods=['post'])
def signup():
    user_data = request.get_json()
    connection = sqlite3.connect("ums.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user123(userid TEXT,password TEXT,email,TEXT)")

    # {"userid":"user1","password":"xyz123","email":"test@test"}

    cursor.execute("INSERT INTO user123 VALUES('{}','{}','{}' )".format(user_data["userid"], user_data["password"],
                                                                        user_data["email"]))

    connection.commit()
    connection.close()

    return "Account is created successfully"


@app.route('/show_record')
def show():
    connection = sqlite3.connect("ums.db")
    cursor = connection.cursor()
    return {"user are": list(cursor.execute("SELECT * FROM user123"))}


@app.route('/update_record', methods=['post'])
def update():
    user_data = request.get_json()
    connection = sqlite3.connect("ums.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE user123 SET password = '{}' WHERE userid = '{}'".format(user_data["password"], user_data["userid"]))

    connection.commit()
    connection.close()

    return "detail update successfully"


@app.route('/delete', methods=['post'])
def delete():
    user_data = request.get_json()
    connection = sqlite3.connect("ums.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM user123 WHERE userid = '{}' ".format(user_data["userid"]))

    connection.commit()
    connection.close()

    return "deleted"

app.run(port=5000)
