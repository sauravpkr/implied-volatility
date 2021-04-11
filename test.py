# Schedule Library imported
import schedule
import time
x=5
# Functions setup
def sudo_placement():
	print("Get ready for Sudo Placement at Geeksforgeeks")

def good_luck():
	print("Good Luck for Test")

def work():
	print("Study and work hard")

def bedtime():
	print("It is bed time go rest")
	
def geeks():
	print("Shaurya says Geeksforgeeks")

# Task scheduling
# After every 10mins geeks() is called.
schedule.every(x).seconds.do(geeks)
schedule.every(7).seconds.do(geeks)

while True:

	# Checks whether a scheduled task
	# is pending to run or not
	schedule.run_pending()
	time.sleep(1)
