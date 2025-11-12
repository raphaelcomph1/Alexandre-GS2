#  Grupo 
1CCPH \
563415 Fernando Caires Silva \
563567 Raphael Mischiatti de Souza \
563500 Guilherme Martins Rezende

# Como rodar o Código

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




