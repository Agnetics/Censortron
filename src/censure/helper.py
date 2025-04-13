# -*- coding: utf-8 -*-


# [][][]    [YYYY]    [TTTTT]    [HHHHH]     [OOOOO]    [NNNNN]
# [P   P]   [YYY ]    [ TTT ]    [H   H]    [O   O]    [N   N]
# [PPPP ]   [ Y  ]    [ TTT ]    [HHHHH]    [O   O]    [N   N]
# [P    ]   [ Y  ]    [ TTT ]    [H   H]    [O   O]    [N   N]
# [P    ]   [ Y  ]    [ TTT ]    [H   H]     [OOO ]    [N   N]


from __future__ import unicode_literals, print_function
import os
import codecs

from censure.base import Censor



class CensorHelper:
    do_compile = True

    def __init__(self, lang='ru', do_compile=None):
        if do_compile is None:
            do_compile = self.do_compile
        self.lang = lang
        self.c = Censor.get(lang=lang, do_compile=do_compile)

    def censure_text(self, text):
        count = 0
        result = []
        for line in text.splitlines():
            new_line, bad_words_count, bad_phrases_count = self.c.clean_line(line)
            count += bad_words_count + bad_phrases_count
            result.append(new_line)
        return '\n'.join(result), count

    def test(self):
        d = os.path.dirname(os.path.abspath(__file__))
        in_file = os.path.join(d, 'data', '{}_in.txt'.format(self.lang))
        out_file = os.path.join(d, 'data', '{}_out.txt'.format(self.lang))

        with codecs.open(in_file, 'r', 'utf-8') as in_fs, \
                codecs.open(out_file, 'w', 'utf-8') as out_fs:
            text = in_fs.read()
            cleaned_text, count = self.censure_text(text)
            print('Found and replaced count: {}'.format(count))
            out_fs.write(cleaned_text)


def ru_just_test():
    c = CensorHelper(lang='ru', do_compile=False)
    c.test()


def en_just_test():
    c = CensorHelper(lang='en', do_compile=False)
    c.test()


def show_examples():
    beep = '[censored]'

    print('Russian examples:')
    # don't specify do_compile=False unless you want to debug something
    # and see bad words raw (not compiled) patterns
    censor_ru = Censor.get(lang='ru', do_compile=False)
    line = 'ебанамат бляд'
    print('Checking line: "{}"'.format(line))
    line_info = censor_ru.check_line(line)
    print('Does the line contain obscene words? - {}'.format(not line_info['is_good']))
    print('First bad word: {}, bad word pattern: {}'.format(
        line_info['bad_word_info']['word'], line_info['bad_word_info']['accuse'][0]))

    print('Cleaning line with beep word={}'.format(line, beep))
    cleaned_line, bad_words_count, bad_phrases_count = censor_ru.clean_line(line, beep=beep)
    print('resulted cleaned line: "{}", bad words count: {}, bad phrases count: {}'.format(
        cleaned_line, bad_words_count, bad_phrases_count))
    print('\n')

    print('English examples:')
    # don't specify do_compile=False unless you want to debug something
    # and see bad words raw (not compiled) patterns
    censor_en = Censor.get(lang='en', do_compile=False)
    line = 'fucken shit'
    line_info = censor_en.check_line(line)
    print('Does the line contain obscene words? - {}'.format(not line_info['is_good']))
    print('First bad word: {}, bad word pattern: {}'.format(
        line_info['bad_word_info']['word'], line_info['bad_word_info']['accuse'][0]))

    print('cleaning line: {} with beep word={}'.format(line, beep))
    cleaned_line, bad_words_count, bad_phrases_count = censor_en.clean_line(line, beep=beep)
    print('Resulted cleaned line: "{}", bad words count: {}, bad phrases count: {}'.format(
        cleaned_line, bad_words_count, bad_phrases_count))

    print('\n')
    line = 'camel toe towel'
    print('English bad phrase line example: "{}"'.format(line))
    line_info = censor_en.check_line(line)
    print('Does the line contain obscene words/phrases? - {}'.format(not line_info['is_good']))

    print('First accuse pattern: {}'.format(
        line_info['accuse'][0]))

    print('Cleaning bad phrases line with beep word={}'.format(beep))
    cleaned_line, bad_words_count, bad_phrases_count = censor_en.clean_line(line, beep=beep)
    print('Resulted cleaned line: "{}", bad words count: {}, bad phrases count: {}'.format(
        cleaned_line, bad_words_count, bad_phrases_count))

    html_line = '<b><span>bitch</i> whore</b>fu<div>ck</li>'
    print('\n')
    print('Cleaning english html line containing bad words: "{}"'.format(html_line))
    # note: no phrases are cleaned atm in html
    cleaned_line, bad_words_count = censor_en.clean_html_line(
        html_line, beep=beep)
    print('Resulted cleaned html line: "{}", bad words count: {}'.format(
        cleaned_line, bad_words_count))




# def show_examples():
#     beep = '[censored]'
#     censor_ru = Censor.get(lang='ru', do_compile=False)
#     line = 'ебанамат бляд'
#     print('Russian examples:')
#     print(f'Checking line: "{line}"')
#     line_info = censor_ru.check_line(line)
#     print(f'Does the line contain obscene words? - {not line_info["is_good"]}')
#     if not line_info['is_good']:
#         print(f'First bad word: {line_info["bad_word_info"]["word"]}, bad word pattern: {line_info["bad_word_info"]["accuse"][0]}')
#     cleaned_line, bad_words_count, bad_phrases_count = censor_ru.clean_line(line, beep=beep)
#     print(f'Cleaning line with beep word={beep}')
#     print(f'Resulted cleaned line: "{cleaned_line}", bad words count: {bad_words_count}, bad phrases count: {bad_phrases_count}\n')

#     censor_en = Censor.get(lang='en', do_compile=False)
#     line = 'fucken shit'
#     print('English examples:')
#     print(f'Checking line: "{line}"')
#     line_info = censor_en.check_line(line)
#     print(f'Does the line contain obscene words? - {not line_info["is_good"]}')
#     if not line_info['is_good']:
#         print(f'First bad word: {line_info["bad_word_info"]["word"]}, bad word pattern: {line_info["bad_word_info"]["accuse"][0]}')
#     cleaned_line, bad_words_count, bad_phrases_count = censor_en.clean_line(line, beep=beep)
#     print(f'Cleaning line: "{line}" with beep word={beep}')
#     print(f'Resulted cleaned line: "{cleaned_line}", bad words count: {bad_words_count}, bad phrases count: {bad_phrases_count}\n')

#     line = 'camel toe towel'
#     print(f'English bad phrase line example: "{line}"')
#     line_info = censor_en.check_line(line)
#     print(f'Does the line contain obscene words/phrases? - {not line_info["is_good"]}')
#     if not line_info['is_good']:
#         print(f'First accuse pattern: {line_info["accuse"][0]}')
#     cleaned_line, bad_words_count, bad_phrases_count = censor_en.clean_line(line, beep=beep)
#     print(f'Cleaning bad phrases line with beep word={beep}')
#     print(f'Resulted cleaned line: "{cleaned_line}", bad words count: {bad_words_count}, bad phrases count: {bad_phrases_count}\n')

#     html_line = '<b><span>bitch</i> whore</b>fu<div>ck</li>'
#     print(f'Cleaning english html line containing bad words: "{html_line}"')
#     cleaned_line, bad_words_count = censor_en.clean_html_line(html_line, beep=beep)
#     print(f'Resulted cleaned html line: "{cleaned_line}", bad words count: {bad_words_count}')










if __name__ == '__main__':
    # ru_just_test()
    # en_just_test()
    # from timeit import Timer
    # t = Timer('just_test()', 'from __main__ import just_test')
    # print(t.timeit())

    show_examples()
