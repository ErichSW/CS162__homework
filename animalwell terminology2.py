def decoder2(coded_digits):
    # replace each number with a different number
    decoded_digits = (coded_digits.replace('6', '0').replace('2', '1')
                      .replace('4', '2').replace('8', '3'))
    return decoded_digits


coded_row = input("Enter entire string: ")
coded_row = coded_row.replace(" ", "")
print(decoder2(coded_row))
