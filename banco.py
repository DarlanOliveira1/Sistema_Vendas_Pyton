import sqlite3
from sqlite3 import Error
import os

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect('banco/pdv2.db')
    except Error as ex:
        print(ex)
    return con

def dql(query): #select
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.commit()
    vcon.close()
    return res

def dml(query):
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)