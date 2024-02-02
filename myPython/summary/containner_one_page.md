操作|List|Tup|Set|Dict
--:|:--|:--|:--|---
创建|`list1 = [1, 2, 3, 4]`|`tup1 = (1, 2, 3, 4)`<br />`tup1 = 1, 2, 3, 4`|`set1 = {1, 2, 3, 4}`<br />`set2 = set((1, 2, 3))`<br />`set2 = set()`|`dict1 = {'name':'bob','age':19}`<br />`dict2 = {}`
访问元素|`list1[0]` <br />`list1[-1]`|`set1[0]` <br />`set1[-1]`||`dict1['name']`<br />`dict1.items()`<br />`dict1.keys()`<br />`dict1.values()`
更新|`list1[2] = 99`|||`dict1['age']=22`
添加|`list1.append(999)`||`set1.update({1, 3})`<br />`set1.update([1,2],[3,4])`<br />`set1.add(99)`|`dict1['school']='CUFE'`
插入|`list1.insert(2,888)  # index, value`||||
删除|`del list1[2]`|||
移除|`list1.remove(1)`||`set1.remove(1)`<br />`set1.discard(99)`|
移除并返回|`a = list1.pop()`||`a = set1.pop() # 随机移除`|`a_value = dict1.pop('age')`
拼接|`list1 + list2` <br /> `list1.extend(list2)`|`tup3 = tup1 + tup2`||`dict1.update(dict2)`
A+B并集|||`set1 \| set2`|
A-B差集|||`set1 - set2`|
A&B交集|||`set1 & set2`|
A^B不同元素|||`set1 ^ set2`|s
重复|`list1 * 5`|`tup1 * 5`||
排序|`list1.sort()`|||
反转|`list1.reverse()`|||
复制|`list1.copy()`|`tup2 = tup1`|`set1.copy()`|`dict1.copy()`
清除|`list1.clear()`||`set1.clear()`|`dict1.clear()`
切片|`list1[:4]` <br /> `list1[-3:]`|`set1[:4]` <br /> `set1[-3:]`||
长度|`len(list1)`|`len(tup1)`|`len(set1)`|`len(dict1)`
最小值|`min(list1)`|`min(tup1)`|`min(set1)`|`min(dicst1)`
最大值|`max(list1)`|`max(tup1)`|`max(set1)`|`max(dicst1)`
元素是否存在|` 3 in list1    # True`|`3 in tup1`|`3 in set1`|`key in dict1`
元素个数统计|`list1.count(99)`|`tup1.count(99)`||
元素index|`list1.index(99)  # 99的第一个index`|`tup1.index(99)`||
迭代|`for i in list1: print(i, end='')`|`for i in tup1: print(i)`|`for i in set1: print(i)`|`for i in dict1: print(i)  # keys`
列表推导式|`[i*i if i%3==0 else i for i in list1 if i>=2]`|格式相同，得到generator <br />`list(generator)`|`{x for x in 'abracadabra' if x not in 'abc'}`|`{i: i*3 for i in range(5)}`<br />`{i: j for i, j in zip(tup1, tup2)}`
    转化|`list(a_seq)`|`tuple(iterable)`|`set()`|Dict