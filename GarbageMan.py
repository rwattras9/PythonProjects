import os, time, datetime, sys

#declare variables
dir_list = ["C:\\Users\\rjw45_000\\Downloads"] #edit list here for directories to run this on
time_now = time.time()
count = 0

#methods

###
#start the program
###
print ("\nHi, I'm the Garbage Man! I'm here to clean up old files. Enter 'Quit' at anytime and I'll stop cleaning.")
num_months = input("How many months makes a file 'old'? ")

# make sure they enter a number for num_months
while True:
	try:
		if (num_months.lower() == 'quit'):
			sys.exit("See ya later!")
		else:
			num_months = int(num_months)
			break
	except ValueError:
		num_months = input("Invalid input. Please enter a number: ")

# compute amount of time to check against with inputted value
amount_of_time = (time_now - 60*60*24*31*num_months) #subtract number of months from now

#iterate through directory and check for items that haven't been updated in the amount of time specified
for dir in dir_list:
	print ("Currently looking at: %s" % dir)
	items = os.listdir(dir)  #list everything in current directory
	#iterate through all files in current directory
	for file in items:
		file = os.path.join(dir, file)  #turn the file into the full path to the file
		#if the file is older than the inputted 'oldness', also ignore subdirectories
		if (os.path.getmtime(file) < amount_of_time and os.path.isdir(file) == False):
			count += 1  #update count of old files
			print ("\nThis file is old: %s" % os.path.join(dir, file))
			response = input("Do you want me to remove this file?(Y/N) ")
			#make sure they input yes or no
			while (response.lower() != "y" and response.lower() != "n" and response.lower() != 'quit'):
				response = input("Invalid input. Please enter Y or N: ")
			if (response.lower() == "y"):
				print ("Removing file: %s\n" % os.path.join(dir, file))
				os.remove(file) # remove the file is they say yes
			elif (response.lower() == 'quit'):
				sys.exit("\nSee ya later!")

#if we get to the end and old file count is still zero, end the program
if (count == 0):
	#print ("\nNo old files to clean up! See ya later!")
	done = input("\nNo old files to clean up! See ya later! Press enter to finish.")
	exit

