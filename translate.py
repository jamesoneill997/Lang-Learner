from googletrans import Translator
import json

words = ["plug", "floor", "wall", "lampshade", "oven", "cupboard", "freezer", "porridge", "charger", "hallway"]       

def make_translation(words, lang):
    translator = Translator()
    dictionary = {}
    translation = [translator.translate(word, dest=lang).text for word in words]

    for i in range(len(words)):
        dictionary[words[i]] = translation[i]

    return dictionary

def add_to_history(dic, lang):    
    with open('{}.json'.format(lang), 'a') as file:
        file.write('\n')
        file.write(json.dumps(dic))
        

def main():

    try:
        fr = make_translation(words, 'fr')
        es = make_translation(words, 'es')

    except:
        print("Error translating words, please check your internet connection and try again.")
    add_to_history(fr, 'fr')
    add_to_history(es, 'es')


if __name__ == '__main__':
    main()