import re


def passport_dict(passport):
    split_strings = (prop.split(':') for prop in passport)
    return {typ: value for typ, value in split_strings}


if __name__ == '__main__':
    # Parse input
    with open('input/Day_4.txt') as f:
        passports = f.read().split('\n\n')
    passports = [passport_dict(re.split(r"[\s\n]", passport)) for passport in passports]

    # Part 1
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    for passport in passports:
        for required_field in required_fields:
            if required_field not in passport:
                break
        else:
            count += 1
    print("Part One:", count)

    # Part 2
    count = 0
    for passport in passports:
        for required_field in required_fields:
            try:
                value = passport[required_field]
            except KeyError:
                # Invalid passport
                break
            if required_field == 'byr':
                if not 1920 <= int(value) <= 2002:
                    break
            elif required_field == 'iyr':
                if not 2010 <= int(value) <= 2020:
                    break
            elif required_field == 'eyr':
                if not 2020 <= int(value) <= 2030:
                    break
            elif required_field == 'hgt':
                if value[-2:] == 'cm':
                    if not 150 <= int(value[:-2]) <= 193:
                        break
                elif value[-2:] == 'in':
                    if not 59 <= int(value[:-2]) <= 76:
                        break
                else:
                    break
            elif required_field == 'hcl':
                if re.fullmatch(r'#[0-9a-f]{6}', value) is None:
                    break
            elif required_field == 'ecl':
                if value[:3] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    break
            elif required_field == 'pid':
                if re.fullmatch(r'[0-9]{9}', value) is None:
                    break
        else:
            count += 1

    print("Part Two:", count)
