import requests


# IMAGE_URL = "http://p2.ifengimg.com/cmpp/2016/11/11/11/ab788c9d-86da-4a20-8b97-fe51a776bf93_size54_w500_h281.jpg"
#
#
def save_image(image_url, name):
    r = requests.get(image_url)

    with open("./image/" + name, "wb") as f:
        f.write(r.content)


def main():
    url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%9D%8E%E6%B2%81"
    html = requests.get(url).text
    print(html)
    # soup = BeautifulSoup(html, 'lxml')

    # pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    # i = 1
    # for each in pic_url:
    #     print (each)
    #     saveImage(each, str(i) + ".jpg")
    #     i += 1


if __name__ == '__main__':
    main()
