# -*- coding: utf-8 -*-
""" 
Парсер макетов 80020 

"""
import xml.etree.ElementTree as ET
import glob
from datetime import datetime, date, time
import pprint

thefolder = '80020/*.xml'

# exit with error message
def err_message(msg):
    messages = {
        'wrong_xml': 'Wrong XML file content. Maybe not 80020 maket?',
        'unknown': 'Unknown error'
    }
    print('--')
    print(messages[msg])
    print('--')


# start

# loop through xml files in current dir
fnames = glob.glob(thefolder)
for f in fnames:
    print('\n===')
    print('Parsing file: ' + f)
    tree = ET.parse(f)
    root = tree.getroot()
    tstamp = root.find('datetime').find('day')
    if tstamp is None:
        err_message('wrong_xml')
        continue
    dt = datetime.strptime(tstamp.text, '%Y%m%d')
    print(dt)
    exit()
