import turtle

# Author WeiKangJian
# Date 2019/11/6


turtle.left(90)
turtle.back(300)
turtle.forward(100)
toplevel = 7  # 绘制的叶子的分叉数目，也是递归的层数
leftangle = 30   #一开始偏移的角度
rightangle = 30  #向另一边偏移的角度
turtle.speed('fastest')  #画笔绘画的快慢
turtle.color('blue','blue')# 图画的颜色

#递归画图
def diguiTree(length, deep):
    turtle.left(leftangle)  # 绘制左枝
    turtle.forward(length)

    if deep == toplevel:  # 叶子
        turtle.circle(5, 360) #画圆

    if deep < toplevel:  # 在左枝退回去之前递归.每次递归，层数加一
        diguiTree(length - 10, deep + 1)
    turtle.back(length)

    turtle.right(leftangle + rightangle)  # 绘制右枝
    turtle.forward(length)

    if deep == toplevel:  # 叶子
        turtle.circle(5, 360)

    if deep < toplevel:  # 在右枝退回去之前递归
        diguiTree(length - 10, deep + 1)
    turtle.back(length)
    turtle.left(rightangle)

diguiTree(100, 1)  #设定树枝干的长短
turtle.done()


