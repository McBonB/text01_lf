def comparessString(s):
    """
    字符串转换。
将一个只包含英文大小写和数字的字符串
按照如下规则转换
1.字符串中连续出现的字符串转换为 a3

输入： aa233a*19 1
输出     a2 21 32 a19 1
    :param s:
    :return:
    """
    if len(s) == 0:
        return s
    count = 1
    tmp = s[0]
    res = ""
    for i in range(1, len(s)-1):
        if s[i] == tmp:
            count += 1
        if s[i] != tmp:
            res = res + str(tmp) + str(count)
            count = 1
            tmp = s[i]
    res = res + str(tmp) + str(count)
    # if len(res) < len(s):
    #     return res
    # else:
    #     return s
    return res

if __name__ == '__main__':
    a = "aa233aacvvvvvaaaaaaaaaa1"
    print(comparessString(a))