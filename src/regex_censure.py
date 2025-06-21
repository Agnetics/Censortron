# [=====]   PPPP    Y   Y  TTTTT  H   H   OOO    N   N
# [=====]   P   P    Y Y     T    H   H  O   O   NN  N
# [=====]   PPPP      Y      T    HHHHH  O   O   N N N
# [=====]   P         Y      T    H   H  O   O   N  NN
# [=====]   P         Y      T    H   H   OOO    N   N


import sys
import os
import traceback


if __name__ == '__main__':
    # for manual testing
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    # sys.path.append(r"D:\Pets\NetTyan\Python\NetTyanRepo\NetTyan\docker\filter\feature_filter\src")
else:
    # for in-docker launch...
    sys.path.append(r"/app/src")
from src.censure import Censor


class SimpleRegexCensor:
    def __init__(self, debug=False):
        self.censors = {
            "ru": Censor.get(lang='ru', do_compile=not debug),  # for debug
            # do compile changes output regex behaviour: False returns string regex, True - big string with ..
            "en": Censor.get(lang='en', do_compile=not debug)
        }

    def check_profinity(self, text, langs=["ru"]):
        # TODO implements many langs and main_lang
        ru_acceptable = self._inner_check_profanity(text, "ru")
        en_acceptable = self._inner_check_profanity(text, "en")  # NOT IMPLEMENTED!!! NOT WORK!
        acceptable = ru_acceptable["acceptable"] and en_acceptable["acceptable"]
        filtered_text = ru_acceptable["filtered_text"] if en_acceptable["acceptable"] else "[ENGLISH AND RUSSIAN BAD WORDS FOUND]"
        return {
            "acceptable": acceptable,
            "filtered_text": filtered_text,
            "additional_regex_filter_info": ru_acceptable if en_acceptable["acceptable"] else {},
            "additional_regex_filter_info_full": {"ru": ru_acceptable, "en": en_acceptable}
        }

    def _inner_check_profanity(self, text, lang):
        # TODO Add custom wordslists
        # now we can manually inject them into libs/censure/lang/ru/constants.py
        try:
            line_info = self.censors[lang].clean_line(text)

            acceptable = line_info[1] <= 0 and line_info[2] <= 0
            return {"acceptable": acceptable, "filtered_text": line_info[0], "additional_regex_filter_info": line_info}
        except Exception as e:
            traceback.print_exc()
            print("[REGEX FILTER] ERROR!!! cannot filter words, assuming them are bad", e)
        return {"acceptable": False, "filtered_text": "[ERROR IN FILTER SYSTEM]", "additional_regex_filter_info": {}}
