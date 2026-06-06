# 这是一个图片等比例缩放的工具

#选择是否更换图片比例然后继续
circle = "1"
while circle == "1":

    # 设定原始图片比例
    origin_width = int(input("图片原始宽度："))
    origin_height = int(input("图片原始高度："))

    # 选择是否在同一个比例中继续操作
    same_circle = "1"
    while same_circle == "1":

        # 选择固定宽度或者高度
        width_or_height = input("你想固定宽度还是高度(宽度：0，高度：1)\n")
        if width_or_height == "0":

            # 得到图片的数值(宽度为主)
            width = int(input("图片预期宽度："))

            # 开始程序，逻辑(origin_width/origin_height=width/height)
            height = int((origin_height / origin_width) * width)
            print(height)
        else:
            # 得到图片的数值(高度为主)
            height = int(input("图片预期高度："))

            # 开始程序，逻辑(origin_width/origin_height=width/height)
            width = int((origin_width / origin_height) * height)
            print(width)
        circle = input("你是否要继续(停止：0，继续：1)\n")
        if circle == "1":
            same_circle = input("你是否要在同一张图片中继续(更换原始图片比例：0，继续：1)\n")
        else:
            break
