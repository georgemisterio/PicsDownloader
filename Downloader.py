import requests

def download_pic(URL):
    pic_url=URL
    with open('pic2.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
download_pic('https://of-leaks.pics/wp-content/uploads/2023/06/1686580267_264_amouredelavie.jpg')            