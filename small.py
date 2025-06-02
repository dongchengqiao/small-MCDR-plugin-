# -*- coding: utf-8 -*-
from mcdreforged.api.all import *

import os
import json
import time
import re
PLUGIN_METADATA = {
    'id': 'small',
    'version': '1.0',
    'name': 'big! small!',
    'author': [
        'DC_Provide'
    ],
    'link': 'Nope...[doge]'
}




def on_info(server, info):
    # PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
    i = 0
    if info.content == '!!small':
        server.execute("attribute " + info.player + " minecraft:generic.scale base set 0.3") 
    if info.content == '!!ultrasmall':
        server.execute("attribute " + info.player + " minecraft:generic.scale base set 0.1") 
    if info.content == '!!normal':
        server.execute("attribute " + info.player + " minecraft:generic.scale base set 1") 
