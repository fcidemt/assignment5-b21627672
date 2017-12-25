import sys

try:
    record = open(sys.argv[1], "r")
except IOError:
    record = open(sys.argv[1], "w")
    record.close()
    record = open(sys.argv[1], "r")

records = open("records_copy.txt", "w")
for line in record:
    if len(line) != 0:
        line = line.strip()
        records.write(line)

while True:
    print(" ---HUBM DVD----")
    print("A:  Add new dvd\n" +
          "R:  Remove dvd\n" +
          "S:  Search dvd\n" +
          "L:  List   dvd\n" +
          "E:  Edit   dvd\n" +
          "H:  Hire   dvd\n" +
          "Q:  Quit\n"+
          "Enter Command: ", end="")
    commands = sys.argv[1]
    command = commands.split(",")
    if command[0] is "A":
        for i in records:
            if command[1] == i[0]:
                print("Serial number already exists.")
        records.write(command[1])
        records.write(",")
        price_input = sys.argv[1]
        records.append(price_input + ",")
    else:
        print("You can only enter A, R, S, L, E, H, Q. Please enter one of these.")





