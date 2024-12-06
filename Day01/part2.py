def build_lists(filename, left, right):
    with open(filename) as file:
        total = 0
        count = 0
        for row in file:
            fields = row.split();
            left.append(int(fields[0]))
            right.append(int(fields[1]))

def compute_based_on_right_count(left, right):
    counts = {}
    for val in right:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1

    sum = 0
    for val in left:
        sum += val * counts.get(val, 0)

    return sum

def main():
    # Build the lists from the input file
    left = []
    right = []
    # build_lists('sampleData.txt', left, right)
    build_lists('realData.txt', left, right)

    # Compute the value in left * occurances in right
    total = compute_based_on_right_count(left, right)
    print('Similarity score:', total)

if __name__ == "__main__":
    main()