def cs_raindrops(number):
    result_str = ""
    rained = False
    print(number % 3)
    if number % 3 == 0:
        result_str += "Pling"
        rained = True
    if number % 5 == 0:
        result_str += "Plang"
        rained = True
    if number % 7 == 0:
        result_str += "Plong"
        rained = True

    if not rained:
        return str(number)

    return result_str
