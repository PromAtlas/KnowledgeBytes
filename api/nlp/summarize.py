from aylien import summerizedSentences
from azure_processing import grab_key_phrases
from wikipedia_processing import create_maps
import json


def summerize_animals(wiki_data, wolfram_data, language="en"):
    animal_summary = {}

    # Organize and grab the Wikipedia data + making sure the wikipedia data exists
    if wiki_data['exists']:
        animal_summary['title'] = wiki_data['title']
        animal_summary["summary"] = summerizedSentences(wiki_data["title"], wiki_data["summary"])
        animal_summary['text'] = summerizedSentences(wiki_data["title"], wiki_data["text"])
        animal_summary["related"] = grab_key_phrases(wiki_data["summary"])
        animal_summary['wiki-url'] = wiki_data['wiki-url']
        animal_summary['wiki-success'] = True
    else:
        animal_summary['wiki-success'] = False
    

    # Grab the scientific name. Given by the Wolfram Alpha API
    if not wolfram_data:
        animal_summary["wolfram-success"] = True
        animal_summary["scientific_name"] = ""
        animal_summary["taxonomy"] = []
    else:
        animal_summary["wolfram-success"] = False

    return animal_summary


def summerize_cities(wiki_data, wolfram_data, language="en"):
    city_summary = {}



    return city_summary

def summerize_planets(wiki_data, wolfram_data, language="en"):
    planet_summary = {}

    return planet_summary

def summerize_person(wiki_data, wolfram_data, language="en"):
    person_summary = {}

    return person_summary

#summerize_animals(create_maps('Shark'))
