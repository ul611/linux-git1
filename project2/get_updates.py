#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 07 02:21:21 2021
@author: ul611
"""
# %% required libraries
import os

# get evvironment variables
AFTER = os.environ.get('AFTER')[1:].replace('_Некоторые особенности написания кода и запуска популярных юнит-тестов проектов', '').replace(' на Linux._', '')
BEFORE = os.environ.get('BEFORE')[1:].replace('_Некоторые особенности написания кода и запуска популярных юнит-тестов проектов', '').replace(' на Linux._', '')

# split the string with the names of projects
AFTER = set(AFTER.split(', '))
BEFORE = set(BEFORE.split(', '))

# print added progect name
PROJECT_NAME = ', '.join(list(AFTER.difference(BEFORE)))
print(PROJECT_NAME)
