from translate import Translator

def translate_to_german():
    word = input("Enter the word to translate to German: ")
    translator= Translator(to_lang="german")
    translation = translator.translate(word)
    print(translation)
    return translation
    
translate_to_german()
