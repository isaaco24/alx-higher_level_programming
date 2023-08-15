#!/usr/bin/python3
<<<<<<< HEAD
# 4-new_in_list.py

=======
>>>>>>> fe40f12c50072cec7f9816acd694da886e059a83

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
<<<<<<< HEAD

=======
>>>>>>> fe40f12c50072cec7f9816acd694da886e059a83
