import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Coloque o link com o ID no final para encontrar o personagem <br>" \
           "<br>" \
           "Exemplo : 127.0.0.1:500/1 para encontrar o personagem com ID 1"

@app.route("/<id>")
def home(id):
    titus = ['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'url', 'location', 'image', 'episode',
             'url', 'created']
    url = "https://rickandmortyapi.com/api/character/{}".format(id)
    infos = requests.get(url)
    if str(infos) != '<Response [200]>':
        return "Não encontrado"
    else:
        infos_json = infos.json()
        Nome = infos_json['name']
        ID = infos_json['id']
        Especie = infos_json['species']
        IMAGEM = infos_json['image']
        return render_template('formulario.html', Nome = Nome, ID = ID, Especie = Especie, IMAGEM = IMAGEM)

if __name__ == "__main__":
    app.run(debug=True)