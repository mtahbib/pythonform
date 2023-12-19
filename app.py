from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'sex': request.form.get('sex'),
            'age': request.form.get('age'),
            'email': request.form.get('email'),
            'address': request.form.get('address'),
        }
        # Process or store user_data as needed (e.g., save to a database)
        print('User Data:', user_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
