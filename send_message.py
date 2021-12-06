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
TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
PROJECT_NAME = os.environ.get('PROJECT_NAME')

# identify action 
action = 'updated in' if 'edited' in PROJECT_NAME else 'added to'

# make GET request: send message to private telegram channel about updates in repo
requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=dict(
   chat_id=CHAT_ID,
   text=f'Info on tips for 42 project {PROJECT_NAME} was {action} repo'
))

