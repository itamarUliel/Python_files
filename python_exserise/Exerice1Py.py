# sec 1:
def todec(value):
    try:
        print(int(value,16))
    except:
        print("invalid hex number")
# todec("11")


# sec 2:
HEX_CHAR = "0123456789abcdfe"


def string_sum(string):
    value = ""
    result = 0
    global HEX_CHAR
    for char in string:
        if char.lower() in HEX_CHAR:
            value += char
        else:
            if value != "":
                result += int(value,16)
                value = ""
    if value != "":
        result += int(value,16)
    print("2: %s\t 8: %s\t 10: %s" % (bin(result), oct(result), result))
# string_sum("10g10fke")


# sec 3:
import statistics


def avgAmed():
    arr = []
    num = input("ENTER:")
    while num.isnumeric():
        arr.append(int(num))
        num = input("ENTER:")
    print("avg: %s\t med: %s" % ((sum(arr) / len(arr)), statistics.median(arr)))
avgAmed()