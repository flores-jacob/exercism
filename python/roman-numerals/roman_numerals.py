def numeral(number):
    thousands = number // 1000
    hundreds = (number - (thousands * 1000)) // 100
    tens = (number - (thousands * 1000) - (hundreds * 100)) // 10
    ones = number - (thousands * 1000) - (hundreds * 100) - (tens * 10)

    thousands_portion = int(thousands) * "M"

    hundreds_val_dict = {
        0: "",
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",
    }

    tens_val_dict = {
        0: "",
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
    }

    ones_val_dict = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }

    return thousands_portion + hundreds_val_dict[hundreds] + tens_val_dict[tens] + ones_val_dict[ones]
