from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS
import logging

# Desativa o log padrão de requisições HTTP do Flask
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # Define para apenas exibir erros


app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Rota para carregar a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Evento de conexão
@socketio.on('connect')
def handle_connect():
    print('🟢 Cliente conectado ao servidor!')

# Evento de desconexão
@socketio.on('disconnect')
def handle_disconnect():
    print('🔴 Cliente desconectado do servidor.')

# Evento que escuta as mensagens e as envia para todos os conectados
@socketio.on('message')
def handleMessage(msg):
    print(f'Mensagem recebida: {msg}')
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=5000)
