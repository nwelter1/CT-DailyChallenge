# Imagine you have several glass balls and are in an n-story building. 
# If you throw a ball out the window below a certain floor, it will not break. 
# If you are above or at that certain floor, it will break. Write a function 
# to find the floor where the balls begin breaking -- in the minimum possible 
# amount of attempts/throws.
# You will not see the input for the floor where balls begin breaking, but it 
# will be a part of a pre-existing function that you will call at each throw 
# (ie. you can call the function with the current floor and get True if the ball 
# breaks, False if not). Starter code below:

def floorCheck(floor, threshold = 42):
    return floor >= threshold

# O(log n) Time | O(1) Space
def findBreakFloor(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        cracked = floorCheck(mid)
        floor_below_cracked = floorCheck(mid-1)
        if cracked and not floor_below_cracked:
            return mid
        elif not cracked:
            low = mid + 1
        elif cracked:
            high = mid - 1
    return "Never Found a floor!"
# Commented Version
def findBreakFloor(n):
	# low and hi pointer for bin search
    low = 0
    high = n
	# binary search
    while low <= high:
		# find mid point
        mid = (low + high) // 2
		# check whether or not the marble cracks on this floor
        cracked = floorCheck(mid)
		# look if the floor below cracks or not
        floor_below_cracked = floorCheck(mid-1)
		# if curr floor cracks and floor below doesn't
		# return this floor
        if cracked and not floor_below_cracked:
            return mid
		# if this floor does not crack, we gotta go up
        elif not cracked:
            low = mid + 1
		# if we are cracked, we gotta go down
        elif cracked:
            high = mid - 1
    return "Never Found a floor!"
    
findBreakFloor(100)