"""Solutions for freeCodeCamp intermediate algorithm scripting 
challenges."""


def sum_all(range_list):
    """Return the sum of the two numbers in range_list and all 
  	numbers between them."""

    return sum([i for i in range(min(range_list),
                                 max(range_list)+1)])


def diff_array(list1, list2):
    """Return a new list with any items only found in one of list1 or list2, but not both. 
    In other words, return the symmetric difference of the two lists."""

    return list(set(list1).symmetric_difference(set(list2)))
