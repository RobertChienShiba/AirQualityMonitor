# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:36:36 2021

@author: rober
"""

from pymongo import MongoClient
from datetime import datetime
import pytz


class DBWrapper:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://Robert:CKekR4fP1ZUTf4pj@cluster0.xur0l.mongodb.net/air?retryWrites=true&w=majority')
        self.db = self.client.air

    def insert_data(self, pm25, pm10):
        at = datetime.now(tz=pytz.UTC)
        d = {
            'PM25': pm25, 
            'PM10': pm10,
            'at': at,
        }
        self.db.air.insert_one(d)