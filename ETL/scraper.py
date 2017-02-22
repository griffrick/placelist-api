import urllib2

from pprint import pprint

from bs4 import BeautifulSoup

def getList():
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

    lists = []
    url = 'http://placelister.herokuapp.com/lists/'
    # url = 'http://odds.betgun.com/makeBB.php?id={0}'.format(sport)
    # print(url)

    conn = urllib2.urlopen(url, None)
    try:
        soup = BeautifulSoup(conn, 'json')
        pprint(soup)
    except:
        return
