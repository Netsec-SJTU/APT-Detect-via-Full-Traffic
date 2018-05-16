with open("get1.txt", "rb") as fh:
    with open("get.txt", "wb") as wh:
        for i in fh:
            wh.write(i.split("/")[-1])