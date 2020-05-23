def data_collection():
	data_no_obj_list = []
	data_object_list = []
	quantity_objects = 0
	money = input('Enter quantity your money: ')
	cost_case = input('Enter cost case: ')

	while True:
		answer_user = input('Want to specify an new object? Yes or Not? ')
		if (answer_user == 'Yes') or (answer_user == 'y'):
			data_object_list.append(input('Enter cost object: '))
			quantity_objects += 1
		elif (answer_user == 'Not') or (answer_user == 'n'):
			break

	data_no_obj_list.append(money)
	data_no_obj_list.append(cost_case)
	data_list = data_no_obj_list + data_object_list

	return data_list, quantity_objects

def math_waiting_cal(import_data_collection = data_collection()):
	data_list = import_data_collection[0]
	theSum = 0
	for j in data_list:
		theSum = theSum + int(j)

	theSum

	arith_mean = theSum / len(data_list)

	# E[X] = (/infty /sum i = 1)Xi_Pi
	# E = X
	# X - it's 'arith_mean')
	# /infty /sum i = 1)Xi_Pi - means the sum of the series consiting of 'Xi' and 'Pi'
	# P - probablity in % of drop item of list 'data_list'
	# i = 1
	# Xi = X ** i
	# Pi = P ** i
	quantity_objects = import_data_collection[1]
	X = arith_mean
	P = 100 / quantity_objects
	i = 1
	Xi = X ** i
	Pi = P ** i
	math_waiting = Xi / Pi

	return print('math waiting: ' + math_waiting)


print(math_waiting_cal())