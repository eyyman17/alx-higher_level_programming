#!/usr/bin/python3

def safe_print_division(a, b): 
    try:
        r = 0
        r = a / b
    except ZeroDivisionError:
        r = None
        return None
    finally:
        if r == None:
            print("Inside result: None")
            return None
        else:
            print("Inside result: {:.1f}".format(r))
            return r
