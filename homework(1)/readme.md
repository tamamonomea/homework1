# 暑期DEMO说明
## 功能说明
本程序主要是对编程中常常需要用到的排序，主要使用了普通选择排序，冒泡排序以及最简单的交换排序，之后还将冒泡排序进行了优化，使运行的比较次数可以减少，特别是序列较为工整时可以减少比较次数。
## 程序介绍
### 声明部分以及函数准备部分
```python
class SQList:
    def __init__(self, lis=None):
        self.r = lis
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret
    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp
```
用于声明排序的类、初始化列表以及字符串转化，还有列表中元素交换的函数，用于后面的各种排序。
### 选择排序
```python
    def select_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            minimum = i
            for j in range(i+1, length):
                if lis[minimum] > lis[j]:
                    minimum = j
            if i != minimum:
                self.swap(i, minimum)
```
使用简单的选择排序为列表进行排序，这种排序的特点是先找出最小的数置于列表最前端，再依次选择次小的数第三小的数等等重复以上操作，直至排序完成。
### 交换排序
```python
    def bubble_sort_simple(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)
```
交换排序是用第一个数分别跟后面的其他数进行比较，只要遇到比它小的就和它进行交换，直至到列表末尾；然后再用第二个数重复以上步骤，直至排序完成。
### 冒泡排序
```python
    def bubble_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length-2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1
```
冒泡排序是从后往前依次使相邻的数进行比较，小的数交换到前面于是可以一次地将较小的数向前排达到排序的效果，亦所谓的“冒泡”。
### 改善冒泡排序
```python
    def bubble_sort_advance(self):
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                    flag = True
                j -= 1
            i += 1
```
改良的冒泡排序是使用flag作为判断，若是比较中一次次序都没有交换则说明后面已经是从小到大排序了，不需要再冒泡比较，这样就减小了运算量。
### 主程序
```python
if __name__ == '__main__':
    sqlist = []
    i = 0
    sqlist1 = []
    print('请输入一系列数,并以end结尾')
    a = input('请输入一个数：')
    while a != 'end':
        sqlist.append(a)
        i += 1
        a = input('请输入一个数：')
    length = len(sqlist)
    for each in range(length):
        sqlist1.append(int(sqlist[each]))
    sqlist2 = SQList(sqlist1)
    sqlist2.bubble_sort()
    print(sqlist2)
```
主程序中主要是读取输入的数以及调用相关的函数，上述程序调用了冒泡排序，实际上都可以调用。
## 程序运行图
![运行成功](新建文件夹\运行图.png)