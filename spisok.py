spisok=[{'school_class':'4a','scores':[1,4,5,4,3]},
{'school_class':'5a','scores':[3,1,5,2,3]},
{'school_class':'7a','scores':[3,4,5,4,3]},
{'school_class':'4a','scores':[3,4,2,5,3]}]

total = 0
middle=0
for school in spisok:
	result = 0
	for result1 in school['scores']:
		result = result + result1
	print (result/len(school['scores']))
	total = total+result
	middle=middle+len(school['scores'])

print (total)
print(middle)
print (total/middle)



#for class1 in spisok:
	#result_for_class=0
	#for result_for_class1 in class1 ['scores']:
		#result_for_class = result_for_class1
	#print (result_for_class/len(class1 ['scores']))	




