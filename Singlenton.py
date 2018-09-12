from os import read
import pandas as pd

class miLector(object):
    data = None
    doc = open("lectura.txt", "r")

    def __new__(param):
        if not param.data:
            param.data = super(miLector, param).__new__(param)
            param.doc = param.doc.read()
        return param.data


b = miLector()
print(b.doc, '\n')
b.doc = open("lectura2.txt", "r")
c = miLector()
print(c.doc.read())
