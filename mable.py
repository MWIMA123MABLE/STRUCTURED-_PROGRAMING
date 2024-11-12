#number1
def even_numbers(integers):
    return[x for x in integers if x %2==0]

list = [1,2,3,4,5,6,7,8,9,10]
even_num = even_numbers(list)
print(even_num)

#number2
def multiplication_table(number):
   
    for i in range(1,13):
        print(f"{number} * {i} = {number*i}")
number = 4
multiplication_table(number)         

#number3
def biggest_num(list):
    if not list:
        return None
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

list = [12,3,5,6]
largest = biggest_num(list)
print(largest)

#number4
input = "hello world"
compare = "hello " 
if input == compare:
    print("same_string")
else:
    print("not the same string")
          