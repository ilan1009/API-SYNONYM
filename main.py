import json
import random

import requests


def flatten(l):
    return [item for sublist in l for item in sublist]


def findSim(text):
    text = text
    key = "get key from merriam webster api for free"
    url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{text}?key={key}"
    response = requests.get(url)

    jt = json.loads(response.text)
    try:
        data = jt[0]['def'][0]['sseq'][0][0][1]
    except TypeError:
        return text, True
    except IndexError:
        return text, True
    sim_list = [data[x] for x in ['syn_list'] if x in data]
    return [n['wd'] for n in sum(flatten(sim_list), [])], False


line = "bro thinks hes tough talking on tiktok, if you ever see me on the streets you better run because i don't play no games"
dnt = ['on', 'the', 'if', 'no', 'your', 'him', 'you']
txtArray = line.split(' ')
a = []
for word in txtArray:
    if word == '':
        break
    f_out = findSim(word)
    if word in dnt:
        a.append(word)
    elif f_out[1]:
        a.append(f_out[0])
    else:
        if len(f_out[0]) == 0:
            a.append(word)
        else:
            a.append(f_out[0][random.randrange(len(f_out[0]))])
            a.append(f" ({word}) ")

print(" ".join(a))
