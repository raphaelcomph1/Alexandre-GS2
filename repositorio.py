from pathlib import Path
import json, csv
class Repositorio:
    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent/"data"
        self.DATA_DIR.mkdir(exist_ok=True) 
        self.DB_PATH = self.DATA_DIR/"usuarios.json" 

    def _load(self):
            if not self.DB_PATH.exists():
                return[]
            
            try:
                return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return []
            
    def _save(self, usuario): #usa o _ para dizer que a função vai ser usada apenas nesse arquivo
        self.DB_PATH.write_text(json.dumps(usuario, ensure_ascii=False, indent=2), encoding="utf-8")
    
    def criandoUsuario(self, lista_usuario):
        usuarioCriado = self._load() #1º vez retorna array vazio []
        usuarioCriado.append(lista_usuario)
        self._save(usuarioCriado)

    def usuarios_db(self):
        return self._load()
