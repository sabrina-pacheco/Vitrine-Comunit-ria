
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Permite a comunicação com o Live Server
CORS(app, origins=["http://127.0.0.1:5500"])

# Armazena os serviços temporariamente
servicos = []

@app.route('/')
def inicio():
    return "<h1>Olá! Meu Flask está funcionando!</h1>"

@app.route('/api/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400

    nome = dados.get('nome')
    preco = dados.get('preco')

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "Nome inválido"}), 400

    if type(preco) not in (int, float) or preco < 0:
        return jsonify({"erro": "Preço inválido"}), 400

    novo_servico = {
        "id": len(servicos) + 1,
        "nome": nome.strip(),
        "preco": preco
    }

    servicos.append(novo_servico)

    return jsonify({
        "mensagem": "Serviço cadastrado com sucesso!",
        "registro": novo_servico,
        "total": len(servicos)
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
