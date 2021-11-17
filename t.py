"""

最远足迹
莫探险队对地下洞穴探索
会不定期记录自身坐标，在记录的间隙中也会记录其他数据，探索工作结束后，探险队需要获取到某成员在探险过程中，对于探险队总部的最远位置
1.仪器记录坐标时，坐标的数据格式为 x，y
x和y——》0-1000
（01,2）（1,01）
设定总部位置为0,0
计算公式为x*（x+y）*y
"""
import re,math
s = "abcccc(3,10)c5,13d(1$f(6,11)sdf(510,200)adas2d()(011,6)" #原始字符串
#print(re.findall(r'[^()a-z]+', s))
pattern = re.compile(r'\(([0-9]{1,3},[0-9]{1,3})\)') #提取坐标正则表达式对象
result = re.findall(pattern,s) #查询整个字符串，得出坐标列表
f_result={}
#判断是否为合格的十进制整数,且大于0小于500
def isDigit(str1):
    if len(str1)==3:
        if str1[0]=='0':
            return False
        else:
            return True
    if len(str1)==2:
        if str1[0]=='0':
            return False
        else:
            return True
    if len(str1)==1:
        if str1=='0':
            return False
        else:
            return True
#遍历得出的坐标列表，求得他距离总部(0,0)的距离，距离为x^2+y^2，并保存到字典f_result
for i in result:
    i=i.split(',')
    if isDigit(i[0]) and isDigit(i[1]):
        f_result[','.join(i)]=i[0]*(i[1]+i[0])*i[1]
#求得最远距离
a=max(f_result.values())
#最远距离的距离和坐标字典
z_result=[]
for i in f_result:
    if f_result[i]==a:
        z_result.append(i)
#最远距离下，x+y和与坐标
he_result={}
#如果最远距离相等，判断谁先到达，规则x+y
for i in z_result:
    i=i.split(',')
    he_result[','.join(i)]=int(i[0])+int(i[1])
#求得和的最小值
b=min(he_result.values())
#遍历，打印出最小和的坐标
for i in he_result:
    if he_result[i]==b:
        print('('+i+')')
#print(i,i[0],i[1],isDigit(i[0]),isDigit(i[1]),f_result,a,z_result,z_result[0],he_result)