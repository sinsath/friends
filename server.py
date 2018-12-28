from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL('mydb')
# now, we may invoke the query_db method
    all_friends = mysql.query_db("SELECT * FROM friends;")
    print("Fetched all friends", all_friends)
    return render_template("index.html", friends = all_friends)

@app.route('/create', methods=['POST'])
def create_friend():
    mysql = connectToMySQL('mydb')
    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    new_friend_id = mysql.query_db(query, data)
    print(new_friend_id)
    #first_name = request.form['first_name']
    #print(first_name)
    #last_name = request.form['last_name']
    #print(last_name)
    #occupation = request.form['occupation']
    #print(occupation)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 