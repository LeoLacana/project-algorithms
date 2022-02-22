from cmath import log


def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    try:
        for period in permanence_period:
            if (period[0] <= target_time <= period[1]):
                    counter += 1
    except TypeError:
        return None
    return counter
