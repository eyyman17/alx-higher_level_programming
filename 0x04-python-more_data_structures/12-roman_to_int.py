#!/usr/bin/python3

def roman_to_int(roman_string):
    value = 0
    if (roman_string and isinstance(roman_string, str)):
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50}
        roman_dict.update({"C": 100, "D": 500, "M": 1000})
        roman_list = [roman_dict.get(x) for x in roman_string]
        for idx, char in enumerate(roman_list):
            if (idx < len(roman_list) - 1):
                if roman_list[idx + 1] > char:
                    value -= char
                else:
                    value += char
            else:
                value += char
    return value
