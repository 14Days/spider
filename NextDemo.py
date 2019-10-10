import requests
import hashlib


def save_image(url, name):
    r = requests.get(url)
    with open('./image/' + name + '.jpg', 'wb') as f:
        f.write(r.content)


def send_request():
    for i in range(100):
        url = 'https://image.baidu.com/search/acjson'
        data = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'word': '家居设计',
            'pn': 10 * i,
            'rn': 10
        }
        print('发送第' + str(i) + '请求')
        try:
            response = requests.get(url, params=data).json()
            data = response['data']
            for item in data:
                if 'thumbURL' in item:
                    m2 = hashlib.md5()
                    m2.update(str(item['thumbURL']).encode('utf-8'))
                    print(m2.hexdigest())
                    save_image(item['thumbURL'], m2.hexdigest())
        except:
            continue


def main():
    send_request()


if __name__ == '__main__':
    main()
