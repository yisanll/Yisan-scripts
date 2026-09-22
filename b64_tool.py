import base64

while True:
    data = input("粘贴要解的字符（打 quit 退出）：")
    if data == "quit":
        print("再见")
        break
    try:
        print(base64.b64decode(data).decode())
    except:
        print("这串好像不是合法的 Base64")