import sys
from os.path import dirname, abspath
path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(path)
from Text2JSON.entity_named_recog.entity_utils import *


def proper_recon(line, placeholders_list: dict):
    char_span = ''
    flag = False
    for char in line:
        if char == '“':
            char_span = char
            flag = True
            continue
        elif flag and char == '”':
            flag = False
            char_span += char
            index = line.index(char_span)
            first_line = line[0: index]
            sec_line = line[index + len(char_span):]
            placeholder = random_str()
            placeholders_list[placeholder] = (char_span, [None])
            line = first_line + placeholder + sec_line
        elif flag:
            char_span += char
    return line
