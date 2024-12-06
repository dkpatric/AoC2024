def build_lists(filename, left, right):
    with open(filename) as file:
        total = 0
        count = 0
        for row in file:
            fields = row.split();
            left.append(int(fields[0]))
            right.append(int(fields[1]))

def compute_absolute_difference(left, right):
    sum = 0

    for x, y in zip(left, right):
        sum += abs(x - y)

    return sum

def main():
    # Build the lists from the input file
    left = []
    right = []
    # build_lists('sampleData.txt', left, right)
    build_lists('realData.txt', left, right)

    # Sort the lists
    left.sort()
    right.sort()

    # Compute the absolute distance between the pairs
    total = compute_absolute_difference(left, right)
    print('Difference:', total)

if __name__ == "__main__":
    main()