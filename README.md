## Virtual Environments em Python

##

### <p align="justify"> Esse repositório foi criado com o intuito de realizar testes durante o aprendizado dos ambientes virtuais em python (Virtual Enviroments), usando a virtualenv: <p/>

<br/>

**<p align="justify"> O funcionamento do virtualenv é realmente simples. Ele basicamente cria uma cópia de todos os diretórios necessários para que um programa Python seja executado, isto inclui: As bibliotecas comuns do Python (standard library). </p>**

## 
<br/>

### Comentários Feitos nos Códigos:
<br/>

<p align="justify">
'''
Se o script (main.py) for executado dentro de um ambiente virtual que
não tem o biblioteca resquests instalada, o script não irá funcionar.

O mesmo script executado fora do ambiente virtual irá funcionar se a 
biblioteca estiver instalada nas pastas base da linguagem dentro do 
sistema operacional.

Aparentemente o ambiente virtual é útil na medida em que o programador
pode instalar bibliotecas somente para o ambiente em que ele deseja utiliza-la,
sem precisar instalar elas de forma permanente na linguagem base do sistema.
'''
</p>

</br>

<p align="justify">
'''
Aparentemente mesmo acessando o ambiente virtual, os arquivos de cógido são os mesmos, sendo assim 
altera-los dentro ou fora do ambiente vitual não gera versões diferentes do mesmo arquivo.
'''
</p>

##
<br/>

## Principais Comandos Utilizados:

- pip install vitualevn -> Instala a biblioteca
- vitualenv nome-do-ambiente -> Cria ambiente virtual no diretório
- nome-do-ambiente\Scripts\activate.ps1 -> Ativa o ambiente virtual (Ao menos no PowerShell e VSCode)
- deactivate -> Desativa o ambiente virtual (Ao menos no PowerShell e VSCode)

##
<br/>

## Virtual Environments e o GitHub
<br/>

Aparentemente não é recomendado realizar o push do ambiente virtual para o GitBuh.

Sendo assim, aconselha-se que um arquivo .gitignore seja criado na raiz do nosso ambiente virtual.

**Em vez disso, o arquivo requirements.txt deve ser criado utilizando o comando:**

- pip freeze > requirements.txt 

**Dentro do ambiente virtual. O arquivo será criado automaticamente fora do ambiente virtual, contendo as informações de dependências do seu projeto.**

<br/>

##

Agora se outro desenvolvedor for rodar o projeto, ele pode utilizar o comando:

- **pip install -r requirements.txt**

Que o gerenciador de pacotes cuidará de baixar e instalar as versões corretas de todos os pacotes que foram utilizados no sistema.

##

## Pesquisas realizadas:

<br/>

Por padrão, o virtualenv não suporta a renomeação de ambientes. É mais seguro apenas excluir o diretório virtualenv e criar um novo com o nome correto. Você pode fazer isso:

Ative seu virtualenv: source vnev/bin/activate
Crie um arquivo requirements.txt dos pacotes atualmente instalados: pip freeze > requirements.txt
Exclua o virtualenv com erro ortográfico: rm -r vnev/
Crie um novo virtualenv com o nome correto: virtualenv venv
Ative o novo virtualenv: source venv/bin/activate
Instale os pacotes de requirements.txt: pip install -r requirements.txt
Se a recriação não for uma opção, existem ferramentas de terceiros, como virtualenv-mv, que podem ser úteis.

Fonte: https://pt.answacode.com/stackoverflow/43256369/como-renomear-um-virtualenv-em-python