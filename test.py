#!/usr/bin/python
#coding=utf-8

print "Hello, World!"
print "你好"
print("Hello, World!")
print("你好，世界!")

print "Hello,py2.7"
print "---------------------------------------"
if True:
    print "True"
else:
  print "False";
print "---------------------------------------"
str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:6]  # 输出字符串中第三个至第六个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

print "---------------------------------------"
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

print "---------------------------------------"
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

print "---------------------------------------"
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()    # 输出所有值