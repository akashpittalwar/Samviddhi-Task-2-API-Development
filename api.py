from flask import Flask, jsonify
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="api")
myCursor = conn.cursor()

app = Flask(__name__) #instance or object with main file

@app.route('/app')
def get():

    myCursor.execute('show COLUMNS FROM data;')
    columns = myCursor.fetchall()
    column_names = [column[0] for column in columns]

    myCursor.execute("select * from data;")
    rows = myCursor.fetchall()

    D=[]
    for i in rows:
        D.append(dict(zip(column_names, i)))
        return jsonify(D)

if __name__ == '__main__':
    app.run(debug=True)

conn.commit()
conn.close()