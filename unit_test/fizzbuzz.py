def answer(num):
    if type(num) == int:
        output = ""
        if num > 0 and num % 3 == 0:
            output += "Fizz"
        if num > 0 and num % 5 == 0:
            output += "Buzz"
        return output if output != "" else num

