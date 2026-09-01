driving = input('你有沒有開過車:')
age = input('你幾歲:')
age=int(age)

if driving == '有':
	if age <= 18 :
		print('幹你怎麼開過車')
	else:
		print('那你可以去很多地方了')
elif driving == '沒有':
	if age <= 18 :
		print('那你快可以考駕照了')
	else:
		print('那你可以去考駕照了呀')	
else:
	print('只能打有/沒有')