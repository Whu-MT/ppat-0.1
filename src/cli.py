"""
Transliterate in CLI mode
"""
import sys

from translators.translator import IndexTranslator, RuleTranslator



if __name__ == '__main__':
    print("""!!!Welcome to Places & People Automate Translator!!!
     /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$
    | $$__  $$| $$__  $$ /$$__  $$|__  $$__/
    | $$  \ $$| $$  \ $$| $$  \ $$   | $$   
    | $$$$$$$/| $$$$$$$/| $$$$$$$$   | $$   
    | $$____/ | $$____/ | $$__  $$   | $$   
    | $$      | $$      | $$  | $$   | $$   
    | $$      | $$      | $$  | $$   | $$   
    |__/      |__/      |__/  |__/   |__/   
    """)

    index_translator = IndexTranslator()
    rule_translator = RuleTranslator()
    available_codes = ''
    for k in rule_translator.rules.keys():
        available_codes += k + ''
    print("""Usage:
    Type names and hit ENTER to get transliterations.
    Use option "-l" to specify language codes. Available codes are:
    
        {}
    
    Default is ALL language codes.
    Use Ctrl+C to quit.
    """.format(available_codes))

    while True:
        line = input('> ').split('-l')
        words = line[0].rstrip()
        lang_codes = []
        if len(line) == 2:
            lang_codes = line[1].lstrip().split(' ')
        print('Result:')
        print('From dictionary:')
        print(index_translator.search(words))
        print('From rule:')
        print(rule_translator.translate(words, lang_codes))