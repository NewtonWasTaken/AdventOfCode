import re

with open('input.txt','r') as f:
    passcode = f.read()


total = 0
part2_data =[]



def decode(passcode):
    passcode2 = passcode.split('\n\n')
    final_passcode = []
    x = 0
    for i in passcode2:
        code = re.split('[\n ]', i)
        code2 = dict(x.split(':') for x in code)
        final_passcode.append(code2)
    return(final_passcode)
data = decode(passcode)



def part1(total):
    for i in data:
        try:
            byr = i['byr']
            iyr = i['iyr']
            eyr = i['eyr']
            hgt = i['hgt']
            hcl = i['hcl']
            ecl = i['ecl']
            pid = i['pid']
            total += 1
            part2_data.append(i)
        except:
            pass
    return (total)
print(part1(total))



def part2():
    hcl_param = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    total_part2 = 0
    ecl_params = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for i in part2_data:
            auth = 0
            byr = i['byr']
            iyr = i['iyr']
            eyr = i['eyr']
            hgt = i['hgt']
            hcl = i['hcl']
            ecl = i['ecl']
            pid = i['pid']
            if 1920 <= int(byr) <= 2002:
                auth += 1
            if 2010 <= int(iyr) <= 2020:
                auth += 1
            if 2020 <= int(eyr) <= 2030:
                auth += 1
            if hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193:
                auth += 1
            if hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76:
                auth += 1
            if hcl[0] == '#' and len(hcl) - 1 == 6:
                hcl_str = hcl[1:]
                hcl_auth = 0
                for i in hcl_str:
                    if i in hcl_param:
                        hcl_auth += 1
                if hcl_auth == 6:
                    auth += 1
            if ecl in ecl_params:
                auth += 1
            if len(pid) == 9 and pid[0] == '0':
                auth += 1
            if auth == 7:
                total_part2 += 1
    return(total_part2)

print(part2())