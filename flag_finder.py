filename = input("要搜索的文件名：")

file = open(filename, encoding="utf-8")
content = file.read()
file.close()

lines = content.split("\n")

found = False

for line in lines:
    if "flag{" in line:
        print("找到啦：", line)
        found = True

if found:
    print("搜查完毕")
else:
    print("整个文件里没有 flag")