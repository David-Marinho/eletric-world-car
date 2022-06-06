from json import dump
import json


arq = open('server/dados.json', 'r') 
dados = json.load(arq)