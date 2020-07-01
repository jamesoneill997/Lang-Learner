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

def add_to_history(dic, lang):    
    with open('{}.json'.format(lang), 'a') as file:
        file.write(json.dumps(dic))

def main():
    fr = make_translation(words, 'fr')
    es = make_translation(words, 'es')

    add_to_history(fr, 'fr')
    add_to_history(es, 'es')


if __name__ == '__main__':
    main()