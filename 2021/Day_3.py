
if __name__ == '__main__':
    with open('input/Day_3.txt') as f:
        data = [line.strip() for line in f]

    # Part 1
    gamma, epsilon = [], []
    for i in range(len(data[0])):
        zero_count = 0
        one_count = 0
        for j in range(len(data)):
            if data[j][i] == '0':
                zero_count += 1
            else:
                one_count += 1
        if zero_count > one_count:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    print(gamma * epsilon)

    # Part 2
    # oxygen
    filtered_data = data
    for i in range(12):
        zero_count = 0
        one_count = 0
        for j in range(len(filtered_data)):
            if filtered_data[j][i] == '0':
                zero_count += 1
            else:
                one_count += 1
        if zero_count == one_count:
            filtered_data = list(filter(lambda x: x[i] == '1', filtered_data))
        elif zero_count > one_count:
            filtered_data = list(filter(lambda x: x[i] == '0', filtered_data))
        elif zero_count < one_count:
            filtered_data = list(filter(lambda x: x[i] == '1', filtered_data))
        print(filtered_data)
    oxygen = int(filtered_data[0], 2)

    # co2
    filtered_data = data
    for i in range(12):
        zero_count = 0
        one_count = 0
        for j in range(len(filtered_data)):
            if filtered_data[j][i] == '0':
                zero_count += 1
            else:
                one_count += 1
        if zero_count == one_count:
            filtered_data = list(filter(lambda x: x[i] == '0', filtered_data))
        elif zero_count > one_count:
            filtered_data = list(filter(lambda x: x[i] == '1', filtered_data))
        elif zero_count < one_count:
            filtered_data = list(filter(lambda x: x[i] == '0', filtered_data))
        if len(filtered_data) == 1:  # Quick fix
            break
    co2 = int(filtered_data[0], 2)
    print(oxygen, co2, oxygen*co2)


