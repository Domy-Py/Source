#直接赋值
set1 = {1,2,3,4,5}
print(type(set1))
#set函数
set2 = set()
print(type(set2))
#不能直接{}
set3 = {}
print(type(set3))
#去重功能
str1 = 'moremore'
set4 = set(str1)
print(set4)
#不可为可变数据
set5 = {'ywyw',6356,76467.336,(1,1,1)}
print(set5)
