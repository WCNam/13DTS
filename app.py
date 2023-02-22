from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/19147/OneDrive - Wellington College/13DTS/templates/smile_cafe.db"

app = Flask(__name__)

def create_connection("db_name"):
    try:
        connecion = sqlite3.connect(db_file)
        return create_connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_home():  # put application's code here
    return render_template("home.html")

@app.route('/contact')
def render_contact():  # put application's code here
    return render_template("contact.html")

@app.route('/menu/cat_id')
def render_menu(cat_id):  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products"
    cur = con.cursor()
    cur.execute(query)
    product_life = cur.fetchall()
    con.close()
    print(category_list)
    return render_template('menu.html', category = categories = category_list)


if __name__ == '__main__':
    app.run()
