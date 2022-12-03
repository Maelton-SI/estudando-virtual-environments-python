## Virtual Environments em Python

<br/>

### <p align="justify"> Esse repositório foi criado com o intuito de realizar testes durante o aprendizado dos ambientes virtuais em python (Virtual Enviroments), usando o gerenciado de dependências python virtualenv: <p/>

<br/>

**<p align="justify"> O funcionamento do virtualenv é realmente simples. Ele basicamente cria uma cópia de todos os diretórios necessários para que um programa Python seja executado, isto inclui: As bibliotecas comuns do Python (standard library). </p>**

##
<br/>

## Principais Comandos Utilizados:

- pip install vitualevn -> Instala a biblioteca
- vitualenv nome-do-ambiente -> Cria ambiente virtual no diretório
- virtualenv path-desejado/nome-do-ambiente -> Também é possível especificar/criar o diretório desejado
- virtualenv -p diretorio-de-instalacao-da-versao-desejada\python.exe nome-do-ambiente -> É possível escolher a versão do python desejada para o ambiente virtual.
- nome-do-ambiente\Scripts\activate.ps1 -> Ativa o ambiente virtual (No PowerShell)
- nome-do-ambiente\Scripts\activate.bat -> Ativa o ambiente virtual (No CMD do Windows)
- deactivate -> Desativa o ambiente virtual (Em ambos, PowerShell e CMD)

##
<br/>

## Virtual Environments e o GitHub
<br/>

Aparentemente não é recomendado realizar o push do ambiente virtual para o GitBuh.

Sendo assim, aconselha-se que um arquivo .gitignore seja criado no diretório em que nosso ambiente virtual foi criado.

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

**Por padrão, o virtualenv não suporta a renomeação de ambientes. É mais seguro apenas excluir o diretório virtualenv e criar um novo com o nome correto. Você pode fazer isso:**

- Ative seu ambiente virtual -> source nome-do-ambiente/bin/activate (linux) <br/>
- Ative seu ambiente virtual -> diretorio/nome-do-ambiente/Scripts/activate (windows) <br/><br/>

- Crie um arquivo requirements.txt dos pacotes atualmente instalados -> pip freeze > requirements.txt <br/>
- Exclua o ambiente virtual com erro ortográfico -> rm -rf diretorio-do-ambiente-virtual <br/><br/>

- Crie um novo ambiente com o nome correto -> virtualenv nome-desejado <br/>
- Ative o novo ambiente virtual -> source nome-do-ambiente/bin/activate (linux) <br/>
- Ative o novo ambiente virtual -> diretorio/nome-do-ambiente/Scripts/activate (windows) <br/><br/>

- Instale os pacotes de requirements.txt -> pip install -r requirements.txt <br/><br/>

Se a recriação não for uma opção, existem ferramentas de terceiros, como virtualenv-mv, que podem ser úteis. <br/>

Fonte: https://pt.answacode.com/stackoverflow/43256369/como-renomear-um-virtualenv-em-python

##

**Não recomendo que você envie seu ambiente virtual para seu repositório remoto no GitHub.**

Ao invés disso, use o comando pip freeze para obter uma lista de todos pacotes utilizados no seu ambiente virtual e salve a saída no arquivo requirements.txt. Este arquivo sim, deve ser enviado para seu repositório. Usando pip install -r requirements.txt em um ambiente virtual novo, você conseguirá reinstalar todos pacotes necessários ao seu projeto (nas versões corretas inclusive).

O ideal seria configurar um arquivo .gitignore na pasta raiz do seu projeto para ignorar os arquivos do ambiente virtual. Se seu ambiente virtual está dentro da pasta venv por exemplo, adicione venv/ no .gitignore e salve.

**Em geral, não suba conteúdos de dependência que podem ser facilmente obtidos. Procure escrever um README.md esclarecedor, descrevendo os procedimentos de obtenção dos módulos dos quais o programa depende, de sua instalação e exemplos de uso.**

Fonte: https://pt.stackoverflow.com/questions/391796/devo-commitar-meu-virtualenv-no-github
