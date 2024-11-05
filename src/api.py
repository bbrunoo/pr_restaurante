from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL

#instalar o pacote sqlalchemy
# pip install Flask-SQLAlchemy

app = Flask(__name__)

# SQL-inMemory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definindo o modelo para a tabela 'Restaurante'
class Restaurante(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    categoria = db.Column(db.String(30), nullable=False)

# Cria as tabelas antes do primeiro request
with app.app_context():
    db.create_all()

# Endpoint GET para retornar todos os restaurantes
@app.route('/restaurantes', methods=['GET'])    
def get_restaurantes():
    restaurantes = Restaurante.query.all()
    result = [{"id": r.id, "nome": r.nome, "ativo": r.ativo, "categoria": r.categoria} for r in restaurantes]
    return jsonify(result)

# Endpoint GET para retornar um restaurante especifco
@app.route('/restaurantes/<int:id>', methods=['GET'])
def get_restaurante_by_id(id):
    restaurante = Restaurante.query.get(id)
    if not restaurante:
        return jsonify({"message": "Restaurante não encontrado"}), 404

    result = {
        "id": restaurante.id,
        "nome": restaurante.nome,
        "ativo": restaurante.ativo,
        "categoria": restaurante.categoria
    }
    return jsonify(result), 200

# Endpoint POST para adicionar um novo restaurante
@app.route('/restaurantes', methods=['POST'])
def add_restaurante():
    data = request.json
    novo_restaurante = Restaurante(nome=data['nome'], ativo=data.get('ativo', True), categoria=data['categoria'])
    db.session.add(novo_restaurante)
    db.session.commit()
    return jsonify({"message": "Restaurante adicionado com sucesso"}), 201

# Método PUT para atualizar um restaurante existente
@app.route('/restaurantes/<int:id>', methods=['PUT'])
def update_restaurante(id):
    data = request.json
    restaurante = Restaurante.query.get(id)
    if not restaurante:
        return jsonify({"message": "Restaurante não encontrado"}), 404

    restaurante.nome = data.get('nome', restaurante.nome)
    restaurante.ativo = data.get('ativo', restaurante.ativo)
    restaurante.categoria = data.get('categoria', restaurante.categoria)

    db.session.commit()
    return jsonify({"message": "Restaurante atualizado com sucesso"}), 200

# Método DELETE para deletar um restaurante existente
@app.route('/restaurantes/<int:id>', methods=['DELETE'])
def delete_restaurante(id):
    restaurante = Restaurante.query.get(id)
    if not restaurante:
        return jsonify({"message": "Restaurante não encontrado"}), 404

    db.session.delete(restaurante)
    db.session.commit()
    return jsonify({"message": "Restaurante deletado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
