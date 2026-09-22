import socket

host = "127.0.0.1"
ports = [21, 22, 25, 80, 110, 143, 443, 3306, 8000]

print("开始扫描", host)

for p in ports:
    s = socket.socket()
    s.settimeout(2)
    r = s.connect_ex((host, p))
    if r == 0:
        try:
            s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")
            data = s.recv(100)
            if len(data) > 0:
                text = data.decode("gbk", errors="ignore")
                firstline = text.split("\r\n")[0]
                print(p, "开着 = 真服务 |", firstline)
            else:
                print(p, "开着 = 门后没人（可能是加密或特殊协议）")
        except Exception:
            print(p, "开着 = 假货或死服务")
    else:
        print(p, "关着")
    s.close()

print("扫描完毕")