#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print an integer
# demonstrates how to use a try ... except for exception handling


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
