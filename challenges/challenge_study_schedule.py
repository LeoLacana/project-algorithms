from cmath import log


def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    # for period in permanence_period:
    #     if not all([type(period[0]) == int, type(period[1]) == int, type(target_time) == int]):
    #         return None
    #     else:
    #         if (period[0] <= target_time <= period[1]):
    #             counter += 1
    # return counter
    try:
        for period in permanence_period:
            if (period[0] <= target_time <= period[1]):
                    counter += 1
    except TypeError:
        return None
    return counter
