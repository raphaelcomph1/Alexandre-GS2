from datetime import date
class Usuario:
    def __init__(self,nome, caracteristicas, carreira, linguagens):
        self.nome =nome
        self.caracteristicas = caracteristicas
        self.carreira = carreira
        self.linguagens = linguagens
        self.criado = date.today().isoformat()
    
    def informacoes(self):
        return{
            'nome':self.nome,
            'caracteristicas':self.caracteristicas,
            'carreira':self.carreira,
            'linguagens':self.linguagens,
            'data criacao':self.criado
        }