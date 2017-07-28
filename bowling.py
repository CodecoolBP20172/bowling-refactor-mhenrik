def score(game):
    """
    Counts the results of the bowling game.
    Args:
        param1: a string
    Returns:
        an integer
    """
    result = 0
    frame = 1
    in_first_half = True  # set if the round is ended in 1 or 2 frames
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last + get_value(game[i+1])  # score is 10 plus the next round's score
        else:
            result += get_value(game[i])  # if the round is has no 10 points
        if frame < 10 and game[i].lower() == 'x':  # in case of strike, the next 2 score is added to the scores
            result += get_value(game[i+1])
            in_first_half = True  # round is ended in 1 frame
            frame += 1
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])  # if spare on the second round
            else:
                result += get_value(game[i+2])
        if in_first_half:
            in_first_half = False  # begin new frame
        else:
            in_first_half = True
            frame += 1 
        last = get_value(game[i])  # to count if there is a spare
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
