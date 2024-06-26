#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to execute a function safely
# demonstrates how to use a try ... except for exception handling


def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
