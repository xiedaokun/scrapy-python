import hashlib


def get_md5(url):
    # str就是unicode了
    if isinstance(url,str):
        url=url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == "__main__":
    print(get_md5('https://jobbole.com'.encode('utf-8')))
