import json
import random


def randoming(race, sex):
    races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "half-orc", "halfling", "human", "tiefling"]
    ethnoses = []
    for elem in races:
        if elem == race:
            characteristic = open('static/races/' + race + '.json', encoding='utf-8')
            characteristics = json.load(characteristic)
            characteristic.close()
    with open('static/params.json', 'rt', encoding="utf-8") as params:
        params = json.load(params)
    for elem in params:
        params[elem] = random.randint(1, 50)

    params["Возраст"] = random.randint(18, 50)
    if race == "dragonborn":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " из клана " + clan
        params["Возраст"] = random.randint(18, 400)
        params["Рост"] = random.randint(180, 210)
        params["Вес"] = random.randint(80, 130)
    elif race == "dwarf":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " из клана " + clan
        params["Возраст"] = random.randint(18, 350)
        params["Рост"] = random.randint(120, 137)
        params["Вес"] = random.randint(40, 70)
    elif race == "elf":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " " + clan
        params["Возраст"] = random.randint(18, 1400)
        params["Рост"] = random.randint(172, 190)
        params["Вес"] = random.randint(60, 80)
    elif race == "gnome":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " по прозвищу " + clan
        params["Возраст"] = random.randint(18, 350)
        params["Рост"] = random.randint(120, 140)
        params["Вес"] = random.randint(40, 70)
    elif race == "half-elf":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " " + clan
        params["Возраст"] = random.randint(18, 160)
        params["Рост"] = random.randint(178, 200)
        params["Вес"] = random.randint(60, 80)
    elif race == "half-orc":
        name = random.choice(characteristics[sex])
        ready_name = name
        params["Возраст"] = random.randint(18, 70)
        params["Рост"] = random.randint(178, 195)
        params["Вес"] = random.randint(65, 90)
    elif race == "halfling":
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        ready_name = name + " " + clan
        params["Возраст"] = random.randint(18, 150)
        params["Рост"] = random.randint(150, 175)
        params["Вес"] = random.randint(40, 70)
    elif race == "human":
        for elem in characteristics['ethnos'].keys():
            ethnoses.append(elem)
        ethnos = random.choice(ethnoses)
        characteristics = characteristics['ethnos']
        ethnos = characteristics[ethnos]
        name = random.choice(ethnos[sex])
        clan = random.choice(ethnos['clan'])
        ready_name = name + " " + clan
        params["Возраст"] = random.randint(18, 70)
        params["Рост"] = random.randint(150, 190)
        params["Вес"] = random.randint(60, 90)
    elif race == "tiefling":
        name = random.choice(characteristics[sex])
        idea_name = random.choice(characteristics['ideaName'])
        ready_name = name + " с идейным именем " + idea_name
        params["Возраст"] = random.randint(18, 70)
        params["Рост"] = random.randint(160, 190)
        params["Вес"] = random.randint(60, 90)
    params["Имя"] = ready_name
    return params
