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

### 4. Executar o Projeto

Agora você pode executar o projeto com o comando:
```bash
python app.py
```
O servidor Flask será iniciado em http://127.0.0.1:5000

## 📂 Estrutura do Projeto

.
├── app.py                 # Arquivo principal da aplicação Flask
├── templates
│   └── index.html         # Página HTML com o frontend do chat
├── static
│   ├── js
│   │   └── chat.js        # Lógica do chat em JavaScript
│   └── style.css          # Estilos CSS para o frontend
└── README.md              # Arquivo de instruções (você está aqui)


### Explicação dos Arquivos:
 - app.py: O servidor backend que serve o frontend e gerencia as conexões WebSocket. O Flask renderiza a página HTML e o Socket.IO gerencia o envio e recebimento de mensagens em tempo real.
 - templates/index.html: Arquivo HTML que define a interface de usuário do chat. Ele contém os elementos básicos para a entrada de mensagens e a exibição das conversas.
 - static/js/chat.js: Código JavaScript que gerencia o envio de mensagens e a recepção de mensagens do servidor em tempo real via WebSocket.
 - static/style.css: Estilos básicos para a aparência do chat, como a área de mensagens e o campo de entrada.

## 🧠 Explicação das Tecnologias

### Flask
 O Flask é um microframework web em Python. Ele é minimalista, mas poderoso o suficiente para criar servidores web completos. No nosso projeto, o Flask é responsável por:

 - Servir a página HTML.
 - Gerenciar as rotas.
 - Funcionar como o servidor backend que recebe as conexões dos clientes.

### Flask-SocketIO
 O Flask-SocketIO permite adicionar suporte a WebSockets na aplicação Flask. WebSockets são usados para permitir comunicação em tempo real entre o cliente (navegador) e o servidor. Diferente do HTTP comum, que funciona por meio de requisições e respostas, os WebSockets mantêm uma conexão aberta e permitem que os dados sejam enviados e recebidos constantemente.

### Flask-CORS
 Flask-CORS é uma extensão que permite o suporte ao Cross-Origin Resource Sharing. Ela é útil quando o frontend e o backend estão rodando em domínios ou portas diferentes. CORS ajuda a evitar bloqueios de segurança que o navegador impõe quando tentamos fazer requisições entre diferentes origens.

### Socket.IO
 Socket.IO é uma biblioteca de JavaScript que facilita a comunicação em tempo real. No frontend, o Socket.IO estabelece uma conexão com o servidor Flask e possibilita o envio e recebimento de mensagens sem a necessidade de atualizar a página. Isso cria uma experiência de chat interativa e fluida para o usuário.

## 📚 Conclusão

Este projeto é uma introdução simples ao desenvolvimento de aplicações web em tempo real utilizando Flask e Socket.IO. Ele é ideal para quem está começando a aprender sobre comunicação em tempo real e como integrar frontend e backend de forma eficaz.

Se tiver alguma dúvida, sinta-se à vontade para abrir uma issue no repositório!
