import urllib2

from pprint import pprint

from bs4 import BeautifulSoup

import simplejson as json

import requests

def getLists():
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    # url_params = url_params or {}
    # url = 'https://{0}{1}{2}'.format(host, urllib.quote(path.encode('utf8')))


    url = 'http://placelister.herokuapp.com/lists/'
    # url = 'http://odds.betgun.com/makeBB.php?id={0}'.format(sport)
    # print(url)

    new_lists = []

    conn = urllib2.urlopen(url, None)
    content = conn.read()
    print(content)
    lists = json.loads(str(content))
    # pprint(lists)

    for list in lists:
        this_id = list['_id']

        list_url = 'http://placelister.herokuapp.com/lists/' + this_id
        list_conn = urllib2.urlopen(list_url, None)
        list_content = list_conn.read()
        this_list = json.loads(str(list_content))
        pprint(this_list)

        new_list = {}
        new_list['title'] = this_list['title']
        new_list['author'] = 'kdenny'
        new_list['list_type'] = 'etc'
        new_list['fake_id'] = this_list['_id']

        r = requests.post('http://placelist.pythonanywhere.com/lists/', new_list)

        print r.status_code
        print r.text

        # pprint(new_list)

        new_list['places'] = []
        for pla in this_list['places']:
            pla['name'] = pla['realName']
            pla['place_type'] = pla['type']
            pla['street_address'] = pla['address']
            pla['state'] = 'MD'
            new_list['places'].append(pla)

        new_lists.append(new_list)

    return new_lists


lists = getLists()



r = requests.post('http://placelist.pythonanywhere.com/lists/', lists[2])
# r = requests.post('http://localhost:8000/lists/1/', data)

