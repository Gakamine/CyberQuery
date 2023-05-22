import importlib
import os
import yaml
import re
import sys

def search(keyword):
    data = []
    data_sources=get_sources(keyword)
    for data_source in data_sources:
        try:
            module = importlib.import_module("src.sources."+data_source["source"])
            output = module.run(keyword,data_source["context"])
            data.append({"source": data_source["source"],"type":data_source["type"], "error": False, "data": output})
        except:
            data.append({"source": data_source["source"],"type":data_source["type"], "error": True, "data": "An error occured"})
    return data

def get_sources(keyword):
    files = os.listdir(r"src/regex_rules")
    sources = []
    for file in files:
        with open('src/regex_rules/'+file, 'r') as file:
            yml_file = yaml.safe_load(file)
            rules = yml_file['rules']
            type = yml_file['type']
            context = yml_file['name']
            for rule in rules:
                if re.search(rule,keyword):
                    for source in yml_file['sources']:
                        sources.append({"source":source,"context":context,"type":type})
                    break
    return sources

# Sort data in a readable format after parsing and querying all sources
#def prettifier(data):
# ...
# ...