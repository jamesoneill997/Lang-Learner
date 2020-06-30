from googletrans import Translator
import json

words = ["lamp", "cup", "fridge", "microwave", "radiator", "blinds", "candle", "window", "beef", "spice"]

def make_translation(words, lang):
    translator = Translator()
    dictionary = {}
    translation = [translator.translate(word, dest=lang).text for word in words]

    for i in range(len(words)):
        dictionary[words[i]] = translation[i]

    return dictionary
#note - add all words to hist.txt

es_words = make_translation(words,"es")
fr_words = make_translation(words,"fr")

def add_to_history(es, fr):
    with open('es.json', 'w') as file:
        file.write(json.dumps(es_words))

    with open('fr.json', 'w') as file:
        file.write(json.dumps(fr_words))

add_to_history(es_words, fr_words)