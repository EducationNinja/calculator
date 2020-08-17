
def main():
	first_num = input("Enter the first number: ")
	second_num = input("Enter the second number: ")

	try:
		first_num = int(first_num)
		second_num = int(second_num)
	except:
		print("Invalid input")
	else:
		op = input("Choose the operation (+, -, /, *): ")
		if op == "+":
			print(first_num + second_num)
		elif op == "-":
			print(first_num - second_num)
		elif op == "*":
			print(first_num * second_num)
		elif op == "/":
			print(round(float(first_num) / float(second_num), 2))
		else:
			print("Invalid operation")

if __name__ == '__main__':
	main()
