file = open('index.txt', 'r', encoding="utf-8")
pan = open('pan.txt', 'a', encoding="utf-8")
link = open('link.txt', 'a', encoding="utf-8")
for line in file.readlines():
    if line:
        item = eval(line)

        if item["workPreviewAddr1"]:
            pan.write(item['workTypeName'] + "-" + item['workTitle'] + "\t:\t" + item["workPreviewAddr1"] + "\t:\t" + item["workPreviewAddr1Code"] + "\n")
            link.write(item["workPreviewAddr1"] + "," + item["workPreviewAddr1Code"] + "\n")

        f = open("项目信息/" + item['workTypeName'] + "-" + item['workTitle'] + '.txt', 'a')
        for (key,value) in item.items():
            # print(key,value)
            if value:
                try:
                    f.write(str(key) + ":\r\n\t\t" + str(value).strip().replace("\n", ",") + "\n")
                except:
                    pass