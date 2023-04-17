from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            # Redirecionar o usuário para a página de sucesso do login
            return redirect(url_for('login_success'))
        else:
            # Exibir mensagem de erro
            error = 'Nome de usuário ou senha incorretos'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/login_success')
def login_success():
    return 'Login bem-sucedido!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

