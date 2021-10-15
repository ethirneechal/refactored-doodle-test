# just a test script
# CO: 15.10.21; LE: 15.10.21

import datetime

def print_weeknum():
	return datetime.datetime.now().isocalendar()[2]

if __name__ == "__main__":
	print('Hello folks! Below is this week number.')
	print_weeknum()

