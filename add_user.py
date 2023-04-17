from app import app, db, User

def add_user(username, password):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")

        add_user(username, password)
        print("Usuário adicionado com sucesso!")
