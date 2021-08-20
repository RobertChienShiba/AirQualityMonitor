# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:37:32 2021

@author: rober
"""

from db_wrapper import DbWrapper


if __name__ == '__main__':
    db = DbWrapper()
    db.clear_db()