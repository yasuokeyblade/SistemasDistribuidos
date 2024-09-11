# Chat em Tempo Real com Flask e Socket.IO

Este projeto é uma aplicação simples de chat em tempo real, construída com **Flask** e **Socket.IO**. A aplicação permite a comunicação em tempo real entre diferentes clientes conectados ao servidor. Cada mensagem enviada por um usuário é transmitida instantaneamente para todos os outros usuários conectados.

## 📋 Funcionalidades

- Enviar mensagens em tempo real.
- Suporte a múltiplos clientes conectados simultaneamente.
- Frontend básico com HTML e JavaScript.
- Backend desenvolvido com Flask gerenciando a comunicação com WebSockets via Socket.IO.

## 🛠️ Tecnologias Utilizadas

### Backend:
- **Flask**: Framework minimalista em Python para o desenvolvimento de aplicações web.
- **Flask-SocketIO**: Extensão que adiciona suporte a WebSockets, permitindo comunicação em tempo real entre o servidor e os clientes.
- **Flask-CORS**: Habilita Cross-Origin Resource Sharing (CORS), permitindo que o frontend faça requisições para o backend, mesmo estando em diferentes origens.

### Frontend:
- **HTML**: Utilizado para estruturar a página do chat.
- **JavaScript**: Gerencia a comunicação com o servidor utilizando Socket.IO.
- **Socket.IO**: Biblioteca para comunicação bidirecional em tempo real entre cliente e servidor.

## 🚀 Como Executar o Projeto

### 1. Requisitos

Antes de começar, você precisará ter o **Python 3** instalado no seu sistema.

### 2. Clonar o Repositório

Clone o repositório com o seguinte comando:

```bash
git clone <link-do-repositorio>
cd <nome-do-repositorio>

```

### 3. Instalar Dependências

Instale as dependências necessárias utilizando o pip:
```bash
pip install flask flask-socketio flask-cors
```

