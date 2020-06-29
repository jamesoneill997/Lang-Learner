from googletrans import Translator

words = ["lamp", "cup", "fridge", "microwave", "radiator", "blinds", "candle", "window", "beef", "spice"]

def make_translation(words, lang):
    translator = Translator()
    translation = [translator.translate(word, dest=lang).text for word in words]

    for i in range(len(words)):
        print(words[i] + ' : ' + translation[i])

    return
#note - add all words to hist.txt

make_translation(words,"es")
print('\n'*5)
make_translation(words,"fr")