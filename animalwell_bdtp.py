coded_text = str(input("Enter entire string: "))

# replace all numbers with new numbers
decoded_text = (coded_text.replace('6', '0').replace('2', '1')
                .replace('4', '2').replace('8', '3'))

# divide the string into 4-character chunks
decoded_text = " ".join([decoded_text[i:i + 4] for i in range(0, len(decoded_text), 4)])

# Assuming decoded_text is a list of strings
for i in range(len(decoded_text)):
    # Get the first two characters and apply the replacements
    first_two = (decoded_text[i][:2].replace('0', '00').replace('1', '01')
                 .replace('2', '10').replace('3', '11'))
    # Concatenate the modified first two characters with the rest of the string
    decoded_text[i] = first_two + decoded_text[i][2:]

print(decoded_text)
