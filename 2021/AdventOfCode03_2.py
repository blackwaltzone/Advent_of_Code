
def convert_bin_to_dec(num):
    print("Converting binary to decimal")
    return sum(2**pos*value for pos, value in enumerate(num))

def get_bit_criteria(list_array_bits, pos):
    # This function will return the most common or uncommon bit for the position
    # specified.
    bit_counter = 0
    for bit_array in list_array_bits:
        if bit_array[pos]:
            bit_counter += 1
    
    # Return 1 if there are >1
    return 1 if bit_counter >= ((len(list_array_bits) + 1) // 2) else 0

def get_filter_criteria(raw_data, max):
    print("Filtering ...")
    # if max = 1, take most common
    all_lines = [[int(x)  for x in line.strip()] for line in raw_data.readlines()] 
    line_len = len(all_lines[0])
    o2_val = []

    # get o2 value
    for i in range(line_len):
        if len(all_lines) > 1:
            # get most common bit
            criteria_bit = get_bit_criteria(all_lines, i)
            if max:
                # filter the new list
                all_lines = list(filter(lambda array_bit: array_bit[i] == criteria_bit, all_lines))
            else:
                criteria_bit = 0 if criteria_bit else 1
                all_lines = list(filter(lambda array_bit: array_bit[i] == criteria_bit, all_lines))
            o2_val.append(criteria_bit)
        else:
            o2_val.append(all_lines[0][i])

    return o2_val

print("Starting program ...")
o2_rating_bin = get_filter_criteria(open("input03.txt", "r"), True)
co2_rating_bin = get_filter_criteria(open("input03.txt", "r"), False)

print("Converting binary to decimal")
o2_rating_dec = convert_bin_to_dec(o2_rating_bin[::-1])
co2_rating_dec = convert_bin_to_dec(co2_rating_bin[::-1])

life_support_rating = o2_rating_dec * co2_rating_dec

print(f"Life support rating: {life_support_rating}")

print("END")