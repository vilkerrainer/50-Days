# ============================================================ #
# -----------Desenvolvimento Web básico com Flask------------- #
# Crie uma API REST simples que retorne uma lista de usuários. #
# ============================================================ #

from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 30},
    {"id": 2, "nome": "João", "idade": 25},
    {"id": 3, "nome": "Maria", "idade": 40}
]


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


if __name__ == "__main__":
    app.run(debug=True)

# ================================= #
# Para rodar: python -m Dia_40.main #
# ================================= #
