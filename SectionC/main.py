def numeral_to_word(numeral):
    ones_place = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_place = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    suffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

    num = int(numeral)
    if num == 0:
        return "zero"

    num_str = ""
    suffix_index = 0

    while num > 0:
        # Split the number into its place values
        thousands = num % 1000
        num //= 1000
        hundreds = (thousands // 100) % 10
        tens = (thousands // 10) % 10
        ones = thousands % 10

        # Build the string representation of the number for this group of 3 digits
        group_str = ""
        if hundreds > 0:
            group_str += ones_place[hundreds] + " hundred "
            if tens > 0 or ones > 0:
                group_str += "and "
        if tens == 1 and ones > 0:
            group_str += teens[ones] + " "
        elif tens > 1:
            group_str += tens_place[tens] + " "
            if ones > 0:
                group_str += ones_place[ones] + " "
        elif ones > 0:
            group_str += ones_place[ones] + " "

        # Add the suffix for this group of 3 digits
        if group_str != "":
            group_str += suffixes[suffix_index] + " "

        num_str = group_str + num_str
        suffix_index += 1
        if num_str.strip() != "":
            num_str += " "

    # Add the final punctuation
    if num_str[-1] == " ":
        num_str = num_str[:-1]
    num_str += "."
   
    return num_str.capitalize()

numeral = input("Enter a number without separators: ")
print(numeral_to_word(numeral))
