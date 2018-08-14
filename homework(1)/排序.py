
class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def bubble_sort_simple(self):
        """
        最简单的交换排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)

    def bubble_sort(self):
        """
        冒泡排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length-2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1

    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度O(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率。
        """
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
    
    def select_sort(self):
        """
        简单选择排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            minimum = i
            for j in range(i+1, length):
                if lis[minimum] > lis[j]:
                    minimum = j
            if i != minimum:
                self.swap(i, minimum)


    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

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
    
