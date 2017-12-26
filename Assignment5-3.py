import sys
text_file = sys.argv[1]
searching_value = sys.argv[2]

students_file = open(text_file, "r")
output_file = open("output.txt", "w")

student_city_list = [line.strip().split(":") for line in students_file]
student_city_dict = {item[0]:item[1] for item in student_city_list}
student_list = [student[0] for student in student_city_list]
studentlist = " ".join(student_list)
output_file.write(studentlist)
print(studentlist)

sorted_list = []
def sorting_func(arg_list):
    global sorted_list
    while len(arg_list) > 0:
        sorted_list.append(min(arg_list))
        arg_list.remove(min(arg_list))
sorting_func(student_list)
sortedlist = " ".join(sorted_list)
output_file.write("\n")
output_file.write(sortedlist)
print(sortedlist)

statement = True
def binary_search(aim, list_arg):
    global statement
    if len(list_arg) == 1 and list_arg[0] == aim:
        return 0
    elif len(list_arg) == 1 and list_arg[0] != aim:
        return 0
    else:
        mid_point = (len(list_arg) - 1) // 2
        if list_arg[mid_point] == aim:
            output_file.write("\n")
            output_file.write(aim)
            print(aim)
            return 0
        first_list = list_arg[:mid_point]
        second_list = list_arg[mid_point + 1:]
        if aim < second_list[0]:
            if len(first_list) == 1 and first_list[0] != aim:
                statement = False
            firstlist = " ".join(first_list)
            output_file.write("\n")
            output_file.write(firstlist)
            print(firstlist)
            return binary_search(aim, first_list)
        else:
            if len(second_list) == 1 and second_list[0] != aim:
                statement = False
            secondlist = " ".join(second_list)
            output_file.write("\n")
            output_file.write(secondlist)
            print(secondlist)
            return binary_search(aim, second_list)

binary_search(searching_value, sorted_list)

if statement is True:
    output_file.write("\n\nThe search string is ")
    output_file.write(searching_value)
    output_file.write(" and the city is ")
    output_file.write(student_city_dict[searching_value])
    print("\nThe search string is", searching_value, "and the city is", student_city_dict[searching_value])
else:
    output_file.write("\n\nThe search string was not found in file")
    print("\nThe search string was not found in file")

students_file.close()
output_file.close()
