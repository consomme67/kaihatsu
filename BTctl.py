import queue
import requests
import os

def kinnjiti_central():
    #fxt = os.stat("ファイルパス").st_size == 0
    fxt = os.stat("textTest").st_size == 0
    print(fxt)

    if not fxt:
        aaa = []
        nearTime = queue.Queue()
        print("a\n")
        with open("textTest") as t:
            nt = t.readlines()
            print(nt)

        for i in nt:
            nearTime.put(i.split())
        print(nearTime)
        print(nearTime.empty())
        print(nearTime.get())
        print(nearTime.get())
        #print(nearTime.get())
        #print(nearTime.empty())
        return nearTime
    else:
        return

"""
    if not fxt:
        nt = []
        nearTime = queue.Queue()
        with open("読み込むテキスト絶対パス", mode="a") as t:
            nt = t.readlines()
            t.write("ここでファイルクリア")
        for i in nt:
            nearTime.put(i.strip())

    else:
        return
"""

def cut():
    print("cut処理")


def send():
    url = "https://sirius.e-catv.ne.jp/shimanami_movie/int/api/upload_movie/"
    video = open('for_send/WIN_20210212_13_18_37_Pro.mp4', 'rb')
    files = {
        'file_upload': ('hoge.mp4', video, 'video/mp4'),
        'timestamp': (None, '1611796299')
    }
    r = requests.post(url, files=files)
    return

def main():
    main_que = kinnjiti_central()

    print("==main==")
    if not main_que.empty():
        i = main_que.get()
        print(i)
    else:
        print("queの中身無いから戻す")
        return


"""
def hoge():
    a=1
    b=2
    c="ccc"

    que = queue.Queue()

    que.put(a)
    print(que)
    que.put(c)

    while not que.empty():
        print(que.get())
"""




if __name__=='__main__':
    print("==start==")
    main()