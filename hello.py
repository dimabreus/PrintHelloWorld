import math
import random
import string

letters = list(string.printable)

printCode = []
brackets = []
phrase1 = []
phrase2 = []
space = []
comma = []
exclamation = []
quote = []

while True:
    letter = random.choice(letters)
    if letter:
        if isinstance(letter, str):
            if letter in letters:
                items = 0
                for i in letter:
                    items += 1
                if items != 0:
                    if items > 0 and items < 2:
                        if items == 1:
                            if math.factorial(items) == 1:
                                if math.floor(math.cos(len(list(letter)))*2) == math.floor(math.sin(1)*2) and len(letter) == math.floor(math.erfc(round(math.pi/math.factorial(math.floor(math.pi))))*math.pi*math.ceil(math.pi))*math.floor(math.e - math.tau/math.pi + abs(math.floor(math.tau) / math.ceil(math.e) / math.floor(math.pi))):
                                    # print(brackets)
                                    if len(printCode) == 0:
                                        if letter == "p":
                                            printCode.append(letter)
                                    elif len(printCode) == 1:
                                        if letter == "r":
                                            printCode.append(letter)
                                    elif len(printCode) == 2:
                                        if letter == "i":
                                            printCode.append(letter)
                                    elif len(printCode) == 3:
                                        if letter == "n":
                                            printCode.append(letter)
                                    elif len(printCode) == 4:
                                        if letter == "t":
                                            printCode.append(letter)
                                    else:
                                        # print(printCode)
                                        if len(brackets) == 0:
                                            if letter == "(":
                                                brackets.append(letter)
                                        elif len(brackets) == 1:
                                            if letter == ")":
                                                brackets.append(letter)
                                        else:
                                            # print(brackets)
                                            if len(phrase1) == 0:
                                                if letter == "h".upper():
                                                    phrase1.append(letter)
                                            elif len(phrase1) == 1:
                                                if letter == "e":
                                                    phrase1.append(letter)
                                            elif len(phrase1) == 2:
                                                if letter == "l":
                                                    phrase1.append(letter)
                                            elif len(phrase1) == 3:
                                                if letter == "l":
                                                    phrase1.append(letter)
                                            elif len(phrase1) == 4:
                                                if letter == "o":
                                                    phrase1.append(letter)
                                            else:
                                                # print(phrase1)
                                                if len(phrase2) == 0:
                                                    if letter == "w":
                                                        phrase2.append(letter)
                                                elif len(phrase2) == 1:
                                                    if letter == "o":
                                                        phrase2.append(letter)
                                                elif len(phrase2) == 2:
                                                    if letter == "r":
                                                        phrase2.append(letter)
                                                elif len(phrase2) == 3:
                                                    if letter == "l":
                                                        phrase2.append(letter)
                                                elif len(phrase2) == 4:
                                                    if letter == "d":
                                                        phrase2.append(letter)
                                                else:
                                                    # print(phrase2)
                                                    if len(space) == 0:
                                                        if letter == " ":
                                                            space.append(letter)
                                                    else:
                                                        # print(space)
                                                        if len(comma) == 0:
                                                            if letter == ",":
                                                                comma.append(letter)
                                                        else:
                                                            if len(exclamation) == 0:
                                                                if letter == "!":
                                                                    exclamation.append(letter)
                                                            else:
                                                                if len(quote) == 0:
                                                                    if letter == '"':
                                                                        quote.append(letter)
                                                                else:
                                                                    finallyCode = ""
                                                                    finallyCode += "".join(printCode)
                                                                    finallyCode += brackets[0]
                                                                    finallyCode += "".join(quote)
                                                                    finallyCode += "".join(phrase1)
                                                                    finallyCode += "".join(comma)
                                                                    finallyCode += "".join(space)
                                                                    finallyCode += "".join(phrase2)
                                                                    finallyCode += "".join(exclamation)
                                                                    finallyCode += "".join(quote)
                                                                    finallyCode += brackets[-1]
                                                                    eval(finallyCode)
                                                                    break
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
    else:
        break
