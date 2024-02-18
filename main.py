import json
import time
from datetime import datetime
from typing import Union
import os
import pygetwindow as gw

try:
    with open('program name.json', encoding='utf-8') as f:
        string = (f.read())
    program_name = json.loads(string)
except:
    program_name = {'': 0}
len_program_name = len(program_name)


def ch_name(name: Union[str, list]):
    if isinstance(name, str):
        if name not in program_name.keys():
            program_name[name] = len(program_name)
        return program_name[name]
    elif isinstance(name, list):
        output = []
        for title in name:
            output.append(ch_name(title))
        return output


old_timestamp = 0
while True:
    dt = datetime.now()
    ymd = dt.strftime('%y%m%d')
    timestampf = dt.timestamp()
    timestamp = int(timestampf)
    if timestamp > old_timestamp:
        old_timestamp = timestamp

        all_windows = [win.title for win in gw.getAllWindows() if win.title]
        gwActive = gw.getActiveWindow()
        active_window = gwActive.title if gwActive else ''

        n_active_window = ch_name(active_window)
        n_name = [ch_name(title) for title in all_windows]

        write = f'{timestamp}, {n_active_window}, {n_name}'
        print(write)
        # update file data/{ymd}.txt
        with open(fr'data/{ymd}.txt', 'a', encoding='utf-8') as f:
            f.write(f'{write}\n')

        # update file program name.json
        if len_program_name != len(program_name):
            len_program_name = len(program_name)
            print('update file program name.json')
            with open('program name.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(program_name, indent=4))
