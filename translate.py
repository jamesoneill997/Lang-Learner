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

def add_to_history(lang):
    with open('{}.json'.format(lang), 'w') as file:
        file.write(json.dumps(make_translation(words, lang)))
    return

add_to_history("es")
add_to_history("fr")