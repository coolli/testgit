#Python实现插入排序
li = [5,4,6,2,1,3]
for i in range(1,len(li)):
	key = li[i]
	j = i - 1
	while j>=0 and li[j]>key:
		li[j+1] = li[j]
		j -=1
	li[j+1]= key
print(li)