# General purpose reusable utilities by JMT
#
# Version 1.0

GLOBAL_DEBUG_LEVEL = 10


def d_print(msg_to_print, msg_priority):
    """ Prints the supplied messgae if the provided priority
        is greater than or equal to the global constant
        GLOBAL_DEBUG_LEVEL
    """

    if msg_priority >= GLOBAL_DEBUG_LEVEL:
        print(msg_to_print)

def reverse_str(input_string):
    """ Return a reversed copy of the provided input_string
    """

    return input_string[::-1]
