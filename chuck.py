import json
from resteasy import RESTEasy

api = RESTEasy(base_url='https://api.chucknorris.io')

jokes = api.route('jokes')
random = jokes.route('random')

categories = jokes.route('categories').get()

for category in categories:
    random_joke = random.get(category=category)
#    print(category, ':', random_joke['value'])

    arquivo = open('Chuck.txt', 'r')
    conteudo = arquivo.readlines()
    
    piada = category, ':', random_joke['value']
    
    conteudo.append(str(piada) +"\n")

    arquivo = open('Chuck.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()