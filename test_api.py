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
	# r = requests.post('http://localhost:8000/lists/1/', data)
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

def test_put_place():
	data = 	{
		"name": "9:30",
		"street_address": '815 V St NW',
		"city": "Washington, DC",
		"url": "http://www.930.com/",
		"zip_code": 20002,
		"lon": -77.02369199999998,
		"lat": 38.91799689999999
	}

	r = requests.post('http://placelist.pythonanywhere.com/places/', data)
	# r = requests.post('http://localhost:8000/lists/', data)
	print r.status_code
	print r.text


def get_lists():
	r = requests.get('http://placelist.pythonanywhere.com/lists/')

	print r.status_code
	print r.text


def get_one_list(list_id):
	list_url = 'http://placelist.pythonanywhere.com/lists/' + str(list_id) + '/'
	r = requests.get(list_url)

	print(r.status_code)
	print(r.text)


def test_delete_list():
	data = {
	}

	r = requests.delete('http://placelist.pythonanywhere.com/lists/31/')
	# r = requests.post('http://localhost:8000/lists/', data)
	print r.status_code
	print r.text


def test_remove_from_list(list_id, place_id):
	r = requests.delete('http://placelist.pythonanywhere.com/lists/{0}/places/{1}'.format(list_id, place_id))
	# r = requests.post('http://localhost:8000/lists/', data)
	print r.status_code
	print r.text


def pending_places():
	r = requests.get('http://placelist.pythonanywhere.com/places/pending/')
	# r = requests.post('http://localhost:8000/lists/', data)
	print r.status_code
	print r.text

# test_new_list()

# test_add_place_to_list()

# get_list()

get_one_list('37')

# test_put_place()

# test_delete_list()

test_remove_from_list('37', '2')
#
# # test_put_place()
#
# # pending_places()
#
# get_one_list('38')
