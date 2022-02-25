def find_duplicate(nums):
    """ Faça o código aqui. """
    if not (nums):
        return False
    if (len(nums) < 2):
        return False
    for number in nums:
        if (type(number) == str or number < 0):
            return False
