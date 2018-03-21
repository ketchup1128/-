import sys
print(len(sys.argv))
for arg in sys.argv:
    print(arg)


#在执行这个 .py 文件的时候要打开cmd然后执行指令：python 1.2.py #你想输入的字符串#
# sys.argv有点类似C语言里面完整版的主函数。在文件之后输入的字符串自动被存入到了变量argv中。
