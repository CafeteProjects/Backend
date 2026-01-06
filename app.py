from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # erlaubt Flutter Zugriff von anderen Domains
# MySQL-Verbindungsdaten, standen gott sei dank auf der Seite
db_config = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME'),
    'port': 3306
}

# API-Endpunkt für Menü
@app.route('/menu', methods=['GET'])
def get_menu():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT itemname, price, category FROM menu")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)  # liefert JSON zurück
@app.route('/active', methods=['GET'])
def get_active():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT active FROM active")  # SQL-Query
    rows = cursor.fetchall()                     # Ergebnis korrekt zuweisen
    cursor.close()
    conn.close()
    return jsonify(rows)
@app.route('/about', methods=['GET'])
def get_aboutus():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT title, content FROM active")  # SQL-Query
    rows = cursor.fetchall()                     # Ergebnis korrekt zuweisen
    cursor.close()
    conn.close()
    return jsonify(rows)
@app.route('/news', methods=['GET'])
def get_news():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, date, news,title FROM news")  # SQL-Query
    rows = cursor.fetchall()                     # Ergebnis korrekt zuweisen
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render setzt PORT
    app.run(debug=True, host='0.0.0.0', port=port)

