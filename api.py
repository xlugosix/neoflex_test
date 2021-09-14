import requests
def test_get_all():
    r = requests.get('https://swapi.dev/api/')
    print(r.text)
def test_get_films():
    r = requests.get('https://swapi.dev/api/films')
    print(t.text)
def test_get_return_of_the_jedi():
    return_of_the_jedi = requests.get('https://swapi.dev/api/films/3/')
    print(return_of_the_jedi.json())
def test_get_planets():
    return_of_the_jedi = requests.get('https://swapi.dev/api/films/3/')
    x = return_of_the_jedi.json()
    for i in x['planets']:
        r = requests.get(i)
        print(r.text)
def test_get_species():
    return_of_the_jedi = requests.get('https://swapi.dev/api/films/3/')
    x = return_of_the_jedi.json()
    for i in x['species']:
        r = requests.get(i)
        print(r.text)

def test_get_peoples():
    mil_falcon = requests.get('https://swapi.dev/api/starships/10/')
    x = mil_falcon.json()
    for i in x['pilots']:
        r = requests.get(i)
        rjson = r.json()
        print (rjson['name'])