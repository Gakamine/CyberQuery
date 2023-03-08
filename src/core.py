import importlib
import os
import yaml
import re
import sys

def search(keyword):
    data_sources=get_sources(keyword)
    if data_sources:
        for source in data_sources:
            module = importlib.import_module("src.sources."+source)
            return module.run(keyword)
    # else:
    # Set a default option here...
    return None

def get_sources(keyword):
    files = os.listdir(r"src/regex_rules")
    sources = []
    for file in files:
        with open('src/regex_rules/'+file, 'r') as file:
            yml_file = yaml.safe_load(file)
            rules = yml_file['rules']
            for rule in rules:
                if re.search(rule,keyword):
                    for source in yml_file['sources']:
                        sources.append(source)
                    break
    return sources

# Sort data in a readable format after parsing and querying all sources
#def prettifier(data):
# ...
# ...