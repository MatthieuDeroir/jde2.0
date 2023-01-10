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
        print("Error : Wrong method input")

