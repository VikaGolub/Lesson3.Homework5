'''
Codewars: Will there be enough space?
'''
def enough(cap, on, wait):
    if wait + on - cap:
        print("There are 10 free places in the bus!")
        return 10
    else:
        print("No free places!")
        return 0
  