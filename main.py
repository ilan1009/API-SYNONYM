import json
import random
import requests


def flatten(l_f):
    """flatten stuff"""
    return [item for sublist in l_f for item in sublist]


def find_sim(text):
    """
    connects to api and gets all the data
    :param text:
    :return:
    """
    key = "get key from merriam webster api for free"
    url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{text}?key={key}"
    response = requests.get(url, timeout=10000)

    json_loaded = json.loads(response.text)
    try:
        data = json_loaded[0]['def'][0]['sseq'][0][0][1]
    except TypeError:
        return text, True
    except IndexError:
        return text, True
    sim_list = [data[x] for x in ['syn_list'] if x in data]
    return [n['wd'] for n in sum(flatten(sim_list), [])], False


LINE = "bro thinks hes tough talking on tiktok, if you ever see me on the streets you better run because i don't play no games"
dnt = ['on', 'the', 'if', 'no', 'your', 'him', 'you']
txtArray = LINE.split(' ')
a = []
for word in txtArray:
    if word == '':
        break
    f_out = find_sim(word)
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
