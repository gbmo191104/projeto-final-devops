from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de usuários (in-memory)
users = []

# Rota para adicionar um usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')

    if not username:
        return jsonify({'message': 'Username is required!'}), 400
    if not email:
        return jsonify({'message': 'Email is required!'}), 400
    if not age:
        return jsonify({'message': 'Age is required!'}), 400

    # Verifica se o usuário já existe
    for user in users:
        if user['username'] == username:
            return jsonify({'message': 'Username already exists!'}), 400

    new_user = {
        'username': username,
        'email': email,
        'age': age
    }
    users.append(new_user)
    return jsonify({'message': 'User added successfully!'}), 201

# Rota para listar todos os usuários
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)