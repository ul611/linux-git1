#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 06 00:46:25 2021
@author: ul611
"""
# %% required libraries
import os
import requests

# get evvironment variables
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
AFTER = os.environ.get('AFTER')[1:].replace('_Некоторые особенности написания кода и запуска популярных юнит-тестов проектов', '').replace(' на Linux._', '')
BEFORE = os.environ.get('BEFORE')[1:].replace('_Некоторые особенности написания кода и запуска популярных юнит-тестов проектов', '').replace(' на Linux._', '')

# split the string with the names of projects
AFTER = set(AFTER.split(', '))
BEFORE = set(BEFORE.split(', '))

# form progect name
project_name = ', '.join(list(AFTER.difference(BEFORE))).replace(' (edited)', '')

# identify action 
action = 'updated in' if 'edited' in project_name else 'added to'

# make GET request: send message to private telegram channel about updates in repo
requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=dict(
   chat_id=CHAT_ID,
   text=f'Info on tips for 42 project {project_name} was {action} repo'
))

