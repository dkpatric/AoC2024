def isAscending(list):
    previous = list[0]
    for number in list[1:]:
        if number <= previous:
            return False
        if (number - previous) > 3:
            return False
        previous = number
    return True

def isDecending(list):
    previous = list[0]
    for number in list[1:]:
        if number >= previous:
            return False
        if (previous - number) > 3:
            return False
        previous = number
    return True

def process_file(filename):
    with open(filename) as file:
        safeCnt = 0
        for row in file:
            numbers = row.split()
            list = []
            for number in numbers:
                list.append(int(number))
            if isAscending(list):
                # print(list, "Safe")
                safeCnt += 1
            elif isDecending(list):
                # print(list, "Safe")
                safeCnt += 1
            # else:
                # print(list, "Unsafe")
    return safeCnt

def main():
    # safeCnt = process_file('sampleData.txt')
    safeCnt = process_file('realData.txt')
    print('There are', safeCnt, 'safe reports')

if __name__ == '__main__':
    main()