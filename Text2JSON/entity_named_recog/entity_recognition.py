import sys
from os.path import dirname, abspath
path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(path)
from Text2JSON.entity_named_recog.minute_entity_recognition import minute_recon
from Text2JSON.entity_named_recog.hour_entity_recognition import hour_recon
from Text2JSON.entity_named_recog.day_entity_recognition import day_recon
from Text2JSON.entity_named_recog.month_entity_recognition import month_recon
from Text2JSON.entity_named_recog.quarter_entity_recognition import quart_recon
from Text2JSON.entity_named_recog.year_entity_recognition import year_recon
from Text2JSON.entity_named_recog.proper_noun_recognition import proper_recon
import chinese2digits as ctd
import copy


def entity_recognition(original_line):
    line = copy.deepcopy(original_line)
    line = line.replace('：', ':')
    line = line.replace(' ', '')
    placeholders_list = {}
    line = proper_recon(line, placeholders_list)
    line = minute_recon(line, placeholders_list)
    line = hour_recon(line, placeholders_list)
    line = day_recon(line, placeholders_list)
    line = month_recon(line, placeholders_list)
    line = quart_recon(line, placeholders_list)
    line = year_recon(line, placeholders_list)
    line = ctd.takeChineseNumberFromString(line)['replacedText']
    for holder, data in placeholders_list.items():
        line = line.replace(holder, data[0])
    line = line.replace('““', '“')
    line = line.replace('””', '”')
    return line
