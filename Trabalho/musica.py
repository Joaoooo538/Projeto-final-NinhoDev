import os
from Conexao import Conexao
import sys 

conexaoBD = Conexao("localhost", "root", "mysql", "spotninho")

def resource_path(relative_path):
    
    """Obtém o caminho absoluto para o recurso, lidando com PyInstaller."""
    
    try:
       
        base_path = sys._MEIPASS
        
    except Exception:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class musica():
    def __init__(self, idmusic, artista, duracao, nome, estilo, file, album_capa):
        self.id = idmusic
        self.artista = artista
        self.nome = nome
        self.estilo = estilo
        self.duracao = duracao
        self.file = file
        self.album_capa = album_capa 

    def mostrar(selfie):
        print(f'''Artista: {selfie.artista}.
Nome: {selfie.nome}.
Estilo: {selfie.estilo}.
Duração: {selfie.duracao}.''')

    def get_album_cover_path(self):
        
        return resource_path(self.album_capa) if hasattr(self, 'album_capa') and os.path.exists(resource_path(self.album_capa)) else None
    
    
musicas = []

musicas_resultado = conexaoBD.consultar("SELECT * FROM musicas")

for musicaA in musicas_resultado:
   
    idmusic, artista, duracao, nome, estilo, album_capa, file = musicaA
        
    musicas.append(musica(idmusic, artista, duracao, nome, estilo, file, album_capa))
