import requests


def req(method, url, data=None, headers=None):
    try:
        if method == "put":
            return requests.put(url, json=data, headers=headers)
        elif method == "post":
            return requests.post(url, json=data, headers=headers)
        elif method == "get":
            return requests.get(url)
    except:
        if method == "put":
            print("(Req.py) error ! Can't modify data in " + url)
        elif method == "post":
            print("(Req.py) error ! Can't post data to " + url)
        elif method == "get":
            print("(Req.py) error ! Can't get data from " + url)
        else:
            print("(Req.py) error ! Can't \'" + method + "\' data from " + url)


