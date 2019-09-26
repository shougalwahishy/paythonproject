


A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

B = [2,4,6,8,10,12,16]


start = 0


for x in A[2:17]:

	print('List A element: ' + str(x))

	for y in B[start:6]:

		print('List B element: '+ str(y))

		start+=1

		break

	