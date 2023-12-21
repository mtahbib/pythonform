from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='flask_user',
    password='your_password',
    database='flask_app'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cursor = db.cursor(dictionary=True)
        user_data = request.json.get('users', [])

        for data in user_data:
            query = "INSERT INTO users (name, sex, age, email, address) VALUES (%s, %s, %s, %s, %s)"
            values = (data['name'], data['sex'], data['age'], data['email'], data['address'])
            cursor.execute(query, values)
            db.commit()

        return jsonify({'message': 'Form submitted successfully'})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
