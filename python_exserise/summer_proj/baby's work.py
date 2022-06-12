def serialize(file_r="python.txt", file_w="serialize_file"):

    file = open(file_r, 'r')
    serialize_file = []
    count_in = -1
    count_val = 1
    for line in file:
        count_in += 1
        serialize_file.append([])
        num = 0
        while num < (len(line) - 1):
            try:
                while line[num] == line[num + 1]:
                    count_val += 1
                    num += 1
                serialize_file[count_in].append(str(count_val)+line[num])
                num, count_val = num + 1, 1
            except IndexError:
                pass
    file.close()
    file = open(file_w, 'w')
    for line in serialize_file:
        file.write("".join(line + ["\n"]))
    file.close()
    return serialize_file


def deserialize(file_r="serialize_file", file_w="deserialize_file"):
    with open(file_r, 'r') as file:
        file_write = open(file_w, 'w')
        writing = ""
        for line in file:
            writing = ""
            line = line.replace("\n", "")
            reading = ""
            print()
            for char in line:
                if char.isnumeric():
                    reading += char
                else:
                    print(char * int(reading), end="")
                    writing += char * int(reading)
                    reading = ""
            file_write.write(writing + "\n")


def table_read(path="conversion_table.txt"):
    file = open(path, 'r')
    table = {}
    for line in file:
        line.replace("\n", "")
        table[line[0]] = line[::2]
    file.close()
    return table


def convert(num=1, path="python.txt",towrite="converted.txt"):
    serialized_file = serialize(path)
    table = table_read()
    reading = ""
    for line in range(len(serialized_file)):
        for sub_line in range(len(serialized_file[line])):
            reader = 0
            try:
                string = serialized_file[line][sub_line]
                char = string[-1]
                try:
                    serialized_file[line].append(serialized_file[line][sub_line][:-1] + table[char][num])
                except KeyError:
                    if serialized_file[line][-1][-1] == "X":
                        new = int(serialized_file[line][-1][:-1]) +\
                              int(serialized_file[line][sub_line][:-1])
                        new = str(new) + "X"
                        serialized_file[line][-1] = new
                    else:
                        serialized_file[line].append(serialized_file[line][sub_line][:-1] + "X")
            except IndexError:
                pass
        serialized_file[line] = serialized_file[line][sub_line+1:]
    file = open(towrite, 'w')
    file.write("")
    file.close()
    file = open(towrite, 'a')
    for line in serialized_file:
        file.write(r"".join(line + ["\n"]))
    file.close()


def printer(rotator=90, file_r="python (1).txt", file_w="rotated_file.txt"):
    file = open(file_r, 'r')
    printing = []
    for line in file:
        line = line.replace("\n", "")
        printing.append(list(line))
    file.close()
    file = open(file_w,'w')
    collector = []

    if rotator == 90:
        for num in range(0,len(printing[0])):
            printor = ""
            for sub_num in range(len(printing) - 1, -1, -1):
                printor += printing[sub_num][num]
            collector.append("\n" + printor)
            print(printor)

    elif rotator == 180:
        for num in range(len(printing) - 1, -1, -1):
            printor = ""
            for sub_num in range(len(printing[0]) - 1, -1, -1):
                printor += printing[num][sub_num]
            collector.append("\n" + printor)
            print(printor)

    elif rotator == 270:
        for num in range(len(printing[0]) - 1, -1, -1):
            printor = ""
            for sub_num in range(len(printing)):
                printor += printing[sub_num][num]
            collector.append("\n" + printor)
            print(printor)

    elif rotator == 360:                                       #mirroring
        for num in range(len(printing)):
            printor = ""
            for sub_num in range(len(printing[0])-1, -1,-1):
                printor += printing[num][sub_num]
            collector.append("\n" + printor)
            print(printor)
    file.writelines(collector)
    file.close()

deserialize("python (1).txt_serializes", "test.txt")
