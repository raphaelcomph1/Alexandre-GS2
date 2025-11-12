#  Grupo 
1CCPH \
563415 Fernando Caires Silva \
563567 Raphael Mischiatti de Souza \
563500 Guilherme Martins Rezende


# Descrição do projeto e propósito
Nesse projeto o grupo teve a iniciativa de criar um codigo, juntando POO (progamacao orientada a objetos) e um agente de IA visando gerar recomendações ao usuário referente a progressos para sua carreira profissional.
# Instruções de execução

### Primeiro passo 
Crie uma pasta chamada ".venv" e ative-a utilizando os codigos abaixo no terminal.\
<br>
Para Criar
```
python -m venv .venv
```
Para Ativar
```
.\.venv\Scripts\activate
```
<br>


### Segundo Passo 
Baixar os requirements utilizando o comando abaixo no terminal. 
```
pip install -r requirements.txt
```
<br>

### Terceiro passo 
Neste passo voce precisar criar o arquivo ".env" para anexar sua key do Gemini.\
<br>
Em sequencia acesse o link para adquirir sua Key do Google IA Studio. 

```
https://aistudio.google.com/api-keys
```
Criando uma nova Key no canto superior direito ou apenas reutilizando uma ja existente.\
<br>
<br>

Agora dentro do arquivo ".env" crie uma variavel com sua Key.

```
GEMINI_API_KEY = "sua Key"
```

### Ultimo Passo

Por fim rode o arquivo "gs2-alexandre.py" no terminal.

```
python gs2-alexandre.py
```

<br>
<br>

# Estrutura de arquivos e classes

```
GS2-ALEXANDRE/
│
├── gs2-alexande.py            
├── usuarios.py          
├── repositorio.py       
├── .env                 
└── README.md            
```
- gs2-alexande.py -> Arquivo principal do programa (contém o menu e lógica de execução).

- usuarios.py -> Define a classe Usuario, com atributos e métodos para representar o perfil do usuário.

- repositorio.py -> Define a classe Repositorio, responsável por armazenar e gerenciar os usuários cadastrados.

- .env -> Armazena variáveis de ambiente, como a chave da API Gemini.

- README.md -> Documento explicativo do projeto.

<br>
<br>

# Demonstração
Segue em anexo o video do codigo em funcionamento no Youtube.
```
https://www.youtube.com/watch?v=xyBmeDp5Gjo
```