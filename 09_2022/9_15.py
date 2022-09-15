def nonConstructibleChange(coins):
	coins.sort()
	current_seen = 0
	for coin in coins:
		if coin > current_seen + 1:
			return current_seen + 1
		else:
			current_seen += coin
	
	return current_seen + 1

def commented(coins):
    # sort the coins in asc order
    # adding smaller coins first helps us find the lowest
    # unavialable change in a linear fashion
	coins.sort()
    # counter to start at 0 and stop whenever we reach amount
    # we can't construct
	current_seen = 0
    # loop over sorted coins
	for coin in coins:
        # if we can't make the next value with this coin,
        # return the next value
		if coin > current_seen + 1:
			return current_seen + 1
        # if not, add the coin and keep it moving
		else:
			current_seen += coin
	# if we made it all thre way through without hitting an error
    # we are out of coins! add one to the current value since
    # if would be impossible to have anything higher!
	return current_seen + 1