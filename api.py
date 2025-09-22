from flask import Flask, request, jsonify

app = Flask (__name__)

musicas = [
    {
        'id': 1,
        'nome': 'Stitches',
        'artista': 'Shawn Mendes'
    },
    {
        'id': 2,
        'nome': 'Monalisa',
        'artista': 'Jorge Vercillo'
    },
    {
        'id': 3,
        'nome': 'Back in Black',
        'artista': 'AC/DC'
    },
]

@app.route('/musicas', methods=['GET'])
def Obter_Musicas():
    
    return jsonify(musicas)

@app.route('/musicas/<int:id>', methods=['GET'])
def Obter_Musicas_Por_Id(id):
    for musica in musicas:
        if musica.get('id') == id:
            
            return jsonify(musica)
        
@app.route('/musicas/<int:id>', methods=['PUT'])
def Editar_Musicas_Por_Id(id):
    musica_alterada = request.get_json()
    for indice, musica in enumerate(musicas):
        if musica.get('id') == id:
            musicas[indice].update(musica_alterada)
            
            return jsonify(musica_alterada)
        
@app.route('/musicas', methods=['POST'])
def Adicionar_Musica():
    nova_musica = request.get_json()
    musicas.append(nova_musica)
    
    return jsonify(nova_musica)

@app.route('/musicas/<int:id>', methods=['DELETE'])
def Excluir_Musicas(id):
    for indice, musica in enumerate(musicas):
        if musica.get('id') == id:
            del musicas[indice]

    return jsonify(musicas)

app.run(port=5000, host='localhost', debug=True)