def isAscending(list):
    # print('isAscending', list)
    dampener = 0
    previous = list[0]
    for number in list[1:]:
        # print('previous:', previous, '- number:', number, '- dampener:', dampener)
        if previous >= number:
            if dampener == 0:
                # print('1st if')
                dampener = 1
            else:
                # print('1st else')
                return False
        elif (number - previous) < 1 or (number - previous) > 3:
            if dampener == 0:
                # print('2nd if')
                dampener = 1
            else:
                # print('2nd else')
                return False
        else:
            previous = number
    return True

def isDescending(list):
    # print('isDescending', list)
    dampener = 0
    previous = list[0]
    for number in list[1:]:
        # print('previous:', previous, '- number:', number, '- dampener', dampener)
        if previous <= number:
            if dampener == 0:
                # print('1st if')
                dampener = 1
            else:
                # print('1st else')
                return False
        elif (previous - number) > 3:
            if dampener == 0:
                # print('2nd if')
                dampener = 1
            else:
                # print('2nd else')
                return False
        else:
            previous = number
    return True

def process_file(filename):
    with open(filename) as file:
        safeCnt = 0
        for row in file:
            status = False
            numbers = row.split()
            list = []
            for number in numbers:
                list.append(int(number))
            rev_list = []
            for num in list[::-1]:
                rev_list.append(num)
            # print('\n*******************************')
            # print(list)
            asc = isAscending(list)
            asc_rev = isAscending(rev_list)
            dsc = isDescending(list)
            dsc_rev = isDescending(rev_list)
            # print('asc: ', asc, '- asc_rev: ', asc_rev, '- dsc:', dsc, '- dsc_rev:', dsc_rev)
            if asc or asc_rev or dsc or dsc_rev:
                # print("Safe")
                safeCnt += 1
            # else: 
                # print("Unsafe")

    return safeCnt

def main():
    # safeCnt = process_file('sampleData.txt')
    # safeCnt = process_file('testData.txt')
    # safeCnt = process_file('edgeCases.txt')
    # safeCnt = process_file('edgeCase.txt')
    safeCnt = process_file('realData.txt')
    print('\nThere are', safeCnt, 'safe reports')

if __name__ == '__main__':
    main()