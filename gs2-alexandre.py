from usuarios import Usuario
from repositorio import Repositorio

repositorio_usuario = Repositorio()

def menu():
    condicao = True
    while condicao:
        print('------------------------------------')
        print("1 Cadastrar usuario")
        print("2 Exibir usuarios")
        print("3 Procurar usuario")
        print("4 Recomendacao")
        print("0 Sair do programa")
        escolha = int(input(("Selecione a opcao desejada: ")))
        match escolha:
            case 1:
                cadastar_usuario()
            case 2:
                exibindo_usuarios()
            case 3:
                usuario_desejado = input("Digite o nome do usuario desejado: ").lower()
                procurar_usuario(usuario_desejado)
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
    print('Usuario cadastrado!')

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

def procurar_usuario(usuario):
        if not usuario:
            print("Digite o nome para procurar")
            return
    
        lista_usuarios = repositorio_usuario.usuarios_db()
        results = []
        
        for i, user in enumerate(lista_usuarios):
            caracteristicas = ', '.join(user['caracteristicas'])
            linguagens = ', '.join(user['linguagens'])
            linha_usuario = f'{user["nome"]} {caracteristicas} {user["carreira"]} {linguagens}'.lower()
            if usuario in linha_usuario:
                results.append(user)
        if not results:
            print("Nada encontrado!")
            return
        print(f"\n## | {'Nome':<20} | {'Caracteeristicas':<50} | {'Carreira':<20}  | {'Linguagens':<30}")
        for i, usuario in enumerate(results):
            caracteristicas = ', '.join(user['caracteristicas'])
            linguagens = ', '.join(user['linguagens'])
            print(f"{i+1:02d} | {user['nome']:<20} | {caracteristicas:<50} | {user['carreira']:<20} | {linguagens:<30}")
    
menu()