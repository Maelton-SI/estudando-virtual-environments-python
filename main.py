import numpy as np
import requests

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

res = requests.get('https://scotch.io')
print(res)

print("Hello World!")

my_array = np.array([1, 2, 3, 4, 5]) 
print(my_array)

'''
Aparentemente mesmo acessando o ambiente virtual, os arquivos de cógido são os mesmos, sendo assim 
altera-los dentro ou fora do ambiente vitual não gera versões diferentes do mesmo arquivo.
'''
print("printed out virtualenv") #Also printed inside virtual environment