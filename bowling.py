def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last + get_value(game[i+1])
        else:
            result += get_value(game[i])
        if frame < 10 and game[i].lower() == 'x':
            result += get_value(game[i+1])
            in_first_half = True
            frame += 1
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])
            else:
                result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        #if game[i].lower() == 'x':
        #    in_first_half = True
        #    frame += 1
    return result


def get_value(char):
    """
    Gets the value from the string
    Args:
        param1: a string
    Returns:
        an integer
    """
    try:
        return int(char)
    except:
        if char.lower() == 'x' or char == '/':
            return 10
        elif char == '-':
            return 0
        else:
            raise ValueError()

#score("11111111112222222222") #30)
score("5/X1------------3/11") #26)
score("1/35XXX458/X3/23")     #160)