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

    if race == "human":
        for elem in characteristics['ethnos'].keys():
            ethnoses.append(elem)
        ethnos = random.choice(ethnoses)
        characteristics = characteristics['ethnos']
        ethnos = characteristics[ethnos]
        name = random.choice(ethnos[sex])
        clan = random.choice(ethnos['clan'])
    else:
        name = random.choice(characteristics[sex])
        clan = random.choice(characteristics['clan'])
        print(name, clan)
