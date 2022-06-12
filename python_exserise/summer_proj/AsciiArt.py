def table_read(path="conversion_table.txt"):
    file = open(path, 'r')
    table = {}
    for line in file:
        line.replace("\n", "")
        table[line[0]] = line[::2]
    file.close()
    return table


def serialize(file_r="python (1).txt", rotator=180, conversion=0):
    table = table_read()
    file = open(file_r, 'r')
    serialize_file = []
    count_in = -1
    count_val = 1
    printing = []

    for line in file:
        line = line.replace("\n", "")
        line_convert = ""
        for char in line:
            try:
                line_convert += table[char][conversion]
            except KeyError:
                if conversion == 0:
                    line_convert += char
                else:
                    line_convert += "X"
        printing.append(list(line_convert))

    collector = []
    if rotator == 0:
        for ls in printing:
            collector.append("".join(ls))
        print(collector)
    if rotator == 90:
        for num in range(0,len(printing[0])):
            printor = ""
            for sub_num in range(len(printing) - 1, -1, -1):
                printor += printing[sub_num][num]
            collector.append(printor)

    elif rotator == 180:
        for num in range(len(printing) - 1, -1, -1):
            printor = ""
            for sub_num in range(len(printing[0]) - 1, -1, -1):
                printor += printing[num][sub_num]
            collector.append(printor)

    elif rotator == 270:
        for num in range(len(printing[0]) - 1, -1, -1):
            printor = ""
            for sub_num in range(len(printing)):
                printor += printing[sub_num][num]
            collector.append(printor)

    elif rotator == 360:                                       #mirroring
        for num in range(len(printing)):
            printor = ""
            for sub_num in range(len(printing[0])-1, -1,-1):
                printor += printing[num][sub_num]
            collector.append(printor)

    collector = collector[1:]
    collector[0] = collector[0].replace("\n", "")

    for line in collector:
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
    file = open("%s_serializes" % file_r, 'w')
    for line in serialize_file:
        file.write("".join(line + ["\n"]))
    file.close()
    return serialize_file



def main():
    x = input("s / ds?: ")
    conversion = input("0 / 1 / 2")
    rotate = input("0 / 90 / 180 / 270 / 360")
    serialize()

if __name__ == '__main__':
    main()
