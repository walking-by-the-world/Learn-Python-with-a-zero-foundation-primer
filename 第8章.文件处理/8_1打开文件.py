# autor: zhumenger
'''
使用open()这个函数打开文件
    第一个参数为文件的路径，第二个参数声明以何种方式打开该文件
        'r': 以只读的方式打开（默认） 'w': 以写入的方式打开,但是会覆盖原来的文件
        'a':以写入模式打开,在文件末尾追加写入
'''
f = open("hello.txt",'r')

#close关闭文件
f.close()