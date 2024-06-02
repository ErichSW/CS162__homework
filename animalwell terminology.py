def decoder2(coded_digits):
    # replace each number with a unicode directional arrow
    decoded_digits = (coded_digits.replace('1', '→').replace('2', '↘').replace('3', '↓')
                      .replace('4', '↙').replace('5', '←').replace('6', '↖')
                      .replace('7', '↑').replace('8', '↗'))
    return decoded_digits


# create empty variable to store the decoded digits
decoded_list = ""
j = 1
while j < 6:
    coded_row = input(f"Enter row " + str(j) + " of coded digits: ")
    # run decoder and add the decoded row to a new list
    decoded_row = decoder2(coded_row)
    decoded_list += decoded_row
    j += 1

# add a space every 4 digits and a newline every 20 digits
decoded_list = " ".join([decoded_list[i:i + 4] for i in range(0, len(decoded_list), 4)])
decoded_list = "\n".join([decoded_list[i:i + 20] for i in range(0, len(decoded_list), 20)])

print("Decoded digits:")
print(decoded_list)
