'''
Codewars: Will there be enough space?
'''
def enough(cap, on, wait):
    if wait + on > cap:
        print("There are free places in the bus!")
        return wait + on - cap
    else:
        print("No free places!")
        return 0
  
