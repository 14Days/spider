import requests
import hashlib


def save_image(url, name):
    heads = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Referer": "http://www.bigbigwork.com/tupian/jiajusheji1.html"
    }

    params = {"x-oss-process": "style/pc_236_webp_2x"}

    r = requests.get(url, headers=heads, params=params)

    with open('./design/' + name + '.jpg', 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)


def send_request():
    url = "http://www.bigbigwork.com/q"
    for i in range(100):
        data = {
            "w": "home furnishing design",
            "c": "家居设计",
            "p": i,
            "h": "家居设计"}
        response = requests.get(url, data).json()
        data = response["data"]
        for each in data:
            m2 = hashlib.md5()
            m2.update(str(each["url"]).encode('utf-8'))
            print(m2.hexdigest())
            save_image(each["url"], m2.hexdigest())


def main():
    send_request()


if __name__ == '__main__':
    main()
