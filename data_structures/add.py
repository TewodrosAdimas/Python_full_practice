def addTwoNumbers( l1, l2):
    multiplier1 = multiplier2 = 1
    number1 = number2 = number = 0
    final_result = []

    for nums in l1:
        number = nums * multiplier1
        multiplier1 = multiplier1 * 10
        number1 = number1 + number

    for nums in l2:
        number = nums * multiplier2
        multiplier2 = multiplier2 * 10
        number2 = number2 + number

    result = int(number1) + int(number2)
    result = str(result)

    for num in result:
        num = int(num)
        final_result.append(num)

    final_result.reverse()
    print(final_result)

addTwoNumbers([2,4,3], [5,6,4])        
    