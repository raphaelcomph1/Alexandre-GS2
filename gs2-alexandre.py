from usuarios import Usuario
from repositorio import Repositorio

repositorio_usuario = Repositorio()

def menu():
    condicao = True
    while condicao:
        print('------------------------------------')
        print("1 Cadastrar usuário")
        print("2 Exibir usuários")
        print("3 Procurar usuário")
        print("4 Recomendacao")
        print("0 Sair do programa")
        escolha = int(input(("Selecione a opção desejada: ")))
        match escolha:
            case 1:
                cadastar_usuario()
            case 2:
                exibindo_usuarios()
            #case 3:
                #procurar_usuario()
            #case 4:
                #recomendacao()
            case 0:
                print("Até mais!")
                condicao=False

def cadastar_usuario():
    nome = input("Digite seu nome: ")

    caracteristicas_input = input("Digite as caracteristicas (separado por virgula): ")
    caracteristicas = [c.strip() for c in caracteristicas_input.split(",")]

    carreira = input("Digite a carreira: ")

    linguagens_input = input("Digite as linguagens (separadas por vírgula): ")
    linguagens = [l.strip() for l in linguagens_input.split(",")]

    usuario = Usuario(nome, caracteristicas, carreira, linguagens)

    convertendoUsuario = usuario.informacoes()
    repositorio_usuario.criandoUsuario(convertendoUsuario)
    print('Usuário cadastrado!')

def exibindo_usuarios():
    lista_usuarios = repositorio_usuario.usuarios_db()
    if not lista_usuarios:
        print ("Nenhum usuario cadastrado")
        return
    print(f"\n## | {'Nome':<20} | {'Caracteristicas':<50} | {'Carreira':<20} | {'Linguagens':<30}")
    for i, usuario in enumerate(lista_usuarios):
        caracteristicas = ', '.join(usuario['caracteristicas'])
        linguagens = ', '.join(usuario['linguagens'])
        print(f"{i+1:02d} | {usuario['nome']:<20} | {caracteristicas:<50} | {usuario['carreira']:<20} | {linguagens:<30}")
    
menu()