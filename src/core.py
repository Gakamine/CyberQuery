import importlib
import os
import yaml
import re
import sys

def search(keyword):
    data_sources=get_sources(keyword)
    if data_sources:
        for data_source in data_sources:
            try:
                module = importlib.import_module("src.sources."+data_source["source"])
                return module.run(keyword,data_source["context"])
            except:
                return "An error occured"
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
            context = yml_file['name']
            for rule in rules:
                if re.search(rule,keyword):
                    for source in yml_file['sources']:
                        sources.append({"source":source,"context":context})
                    break
    return sources

# Sort data in a readable format after parsing and querying all sources
#def prettifier(data):
# ...
# ...