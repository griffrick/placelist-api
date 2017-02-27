
import json
import random
import requests

# Can make whichever tests you want to execute True; if you don't want to execute a test then make it False
get_single_list = True
get_single_place = True
get_many_places = True
get_many_lists = True

def test_get_single_place():
	data = 	{
		"name": "place1",
		"place_type": "stupid",
		"street_address": "320 Small Court",
		"state": "MD",
		"zip_code": 21228,
		"lon": 17.0,
		"lat": 16.0
	}

	r = requests.get('http://localhost:8000/lists/1/', data)
	print r.status_code
	print r.text


def test_add_place_to_list():
	data = 	{
		"name": "fun",
		"place_type": "stupid",
		"street_address": "320 Small Court",
		"state": "MD",
		"zip_code": 21228,
		"lon": 17.0,
		"lat": 16.0
	}

	r = requests.post('http://placelist.pythonanywhere.com/lists/1/', data)
	print r.status_code
	print r.text

def test_get_single_list():
	data = {
		""
	}

# def test_get_many_places():
# 	data = {}

# def test_create_place():


# def test_create_list():
# 	data = {}

def test_new_list():
	data = 	{
		"title": "doom",
		"author": 'kdenny',
		"list_type": "MD",
		"zip_code": 21228,
		"lon": 17.0,
		"lat": 16.0
	}

	r = requests.post('http://placelist.pythonanywhere.com/lists/', data)
	# r = requests.post('http://localhost:8000/lists/', data)
	print r.status_code
	print r.text

test_new_list()

# test_add_place_to_list()