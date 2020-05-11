# -*- author:caoyue -*-
import re

# 查找字符串中有多少个af
s1 = "asdfjvjadsffvaadfkfasaffdsasdffadsafafsafdadsfaafd"

list1 = re.findall(r'af', s1)
print(len(list1))

# 取出字符串中的所有字母
s2 = "abDEe23dJfd343dPOddfe4CdD5ccv!23rr"
list2 = re.findall(r'[a-zA-Z]', s2)
print(list2)

# 规则是按照空格出现一次或者多次切割
s3 = "zhangsan   lisi  wangwu"
list3 = re.split(r'\s+', s3)
print(list3)

# 用正则\\切割
s4 = "c:\\abc\\a.txt"
list4 = re.split(r'\\', s4)
print(list4)

# 将连续5个以上数字替换成#
s5 = "wer8934605juo123wa89320571f"
res5 = re.sub(r'\d{5,}', '#', s5)
print(res5)

# # 将多个重复字母替换成&
s6 = "cudddbhuuujddd"
res6 = re.sub(r'([a-zA-Z])\1+', '&', s6)
print(res6)

# 获取长度为3个字母的单词
s7 = "min tian jiu yao fang jia le ,da jia"
list7 = re.findall(r'\b([a-zA-Z]{3})\b', s7)
print(list7)

# 获取单词结尾是e的单词,忽略大小写
s8 = 'THREE people at HERE do some THING'
list8 = re.findall(r'[a-zA-Z]*e\b', s8, re.I)
print(list8)

# 修改为‘我要学编程’
s9 = "我我...我我...我要..要要...要要...学学学...学学...编编编..编程..程.程...程...程"
res9 = re.sub(r'(\.)+', '', s9)
res9 = re.sub(r'(.)\1+', r'\1', res9)
print(res9)

# 输出结果为列表
# [ "<img src='1.png'><img src='2.png'>" , "<img src='11.png'><img src='22.png'>" ]
s10 = """
<div>
	<img src='1.png'>
	<img src='2.png'>
</div>
<div>
	<img src='11.png'>
	<img src='22.png'>
</div>
"""
res10 = re.sub(r'[\n\t]+', '', s10)
list10 = re.findall(r'<div>(.*?)</div>', res10, re.S)
print(list10)



