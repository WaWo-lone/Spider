# -*- author:caoyue -*-
from lxml import etree

con = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1" id="w"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1" id='abc' style="width:20px;"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
     <span>12345</span>
     <li>lllllll</li>
 </div>
'''

# 1,通过etree.HTML 方法加载需要解析的文档
html = etree.HTML(con)

# 2,通过返回对象的xpath方法，找到需要的数据
# xpath 放回的元素对象都是一个列表
# /是表示当前文档的一级子元素
ele = html.xpath('/html')
print(etree.tostring(ele[0]))

# //是查找当前文档的任何子孙元素
ele = html.xpath('//li')
for e in ele:
    print(etree.tostring(e))

# ./表示查找当前元素的直接元素
ele = html.xpath('//ul')
li = ele[0].xpath('./li')
print(li)

# ../表示当前元素的上级元素
ele = html.xpath('//ul')
ul = ele[0].xpath('../ul')
print(ul)

# 3,所有的非标准会被xpath加载为一个标准的文档，就是含有html和body标签
# print(etree.tostring(html))

# 找含有id属性的li标签
ele = html.xpath('//li[@id]')
print(etree.tostring(ele[1]))

# 找li标签的class值为item-inactive的
ele = html.xpath('//li[@class="item-inactive"]')
print(etree.tostring(ele[0]))

# 找含有id属性的li标签的class属性的值
# ele = html.xpath('//li[@id]/@class')
ele = html.xpath('//li[@id]/@style')
print(ele)

# 查找li元素的class=item-1 并且id=abc
ele = html.xpath('//li[@id="abc" and @class="item-1"]')
print(etree.tostring(ele[0]))

# 查找不含有id属性的li标签
ele = html.xpath('//li[not(@id)]')
for e in ele:
    print(etree.tostring(e))

# 同时找到ul和span标签
ele = html.xpath('//ul | //span')
for e in ele:
    print(etree.tostring(e))


# 查找li标签中class属性包含1
ele = html.xpath('//li[contains(@class, "1")]')
for e in ele:
    print(etree.tostring(e))

# 查找li标签中id属性以w开头
ele = html.xpath('//li[starts-with(@id, "w")]')
for e in ele:
    print(etree.tostring(e))

# 查找li标签中id属性以c结尾
# ele = html.xpath('//li[ends-with(@id, "c")]')
# for e in ele:
#     print(etree.tostring(e))

# 查找最后一个li标签,找的是同级的最后一个
ele = html.xpath('//li[last()]')
for e in ele:
    print(etree.tostring(e))

# 查找第一个li标签，找的也是同级的
# ele = html.xpath('//li[position()=1]')
ele = html.xpath('//li[1]')  #中括号中的位置是从1开始的
for e in ele:
    print(etree.tostring(e))

# 从第三个li标签找到所有的li元素
ele = html.xpath('//li[position()>=3]')
for e in ele:
    print(etree.tostring(e))

# 找到最后一个a标签的内容
ele = html.xpath('//li[last()]/a/text()')
print(ele)








