import json
import csv

def leer_txt(path):
    with open(path) as f:
        return [line.strip() for line in f]

def leer_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        return [row for row in reader]

def leer_json(path):
    with open(path) as f:
        return json.load(f)