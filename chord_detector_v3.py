

string_low_e = input()
string_a = input()
string_d = input()
string_g = input()
string_b = input()
string_high_e = input()

temp_list = [string_low_e, string_a, string_d, string_g, string_b, string_high_e]
print(temp_list)


def empty_input_check(input_list):
    checked_list = []
    for item in input_list:
        print(item)
        print(bool(item))
        if bool(item) == False:
            item = '--'
            checked_list.append(item)
        else:
            checked_list.append(item)
    return checked_list

print(empty_input_check(temp_list))