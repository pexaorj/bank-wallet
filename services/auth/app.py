from flask import Flask, request, jsonify, render_template
from config import Config
from models import db, User
import logging
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variável de versão definida pelo ambiente do Docker
APP_VERSION = os.getenv("APP_VERSION")

# Criar tabelas do banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        logger.warning(f"Attempted registration with existing username: {username}")
        return jsonify({"message": "Username already exists!"}), 400
    
    new_user = User(username=username, password=password)
    
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
    
    logger.info(f"New user registered: {username}")
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        logger.info(f"User {username} logged in successfully.")
        return jsonify({"message": "Login successful!"}), 200
    else:
        logger.warning(f"Invalid login attempt for user {username}.")
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(users_list), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
