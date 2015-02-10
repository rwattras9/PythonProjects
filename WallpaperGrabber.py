import os
import praw
from PIL import Image
import urllib.request
import imghdr
import sys
import subprocess

#define the user agent for the reddit query
r = praw.Reddit(user_agent="rick_in_da_bawks WallpaperGrabber test")

#
#define necessary variables
#
subreddits = ['spaceporn', 'wallpaper', 'earthporn'] #list subreddits to get wallpapers from
wallpaper_dir = 'C:\\Users\\rjw45_000\\Pictures\\Wallpapers'

#
#methods
#
# get the dimensions of the picture from the post title
def get_dimensions(title):
	dims = title.split('[')[1]
	dims = dims.split(']')[0]
	dims = dims.split('x')
	return dims

# check whether the necessary subreddit directory exists, make it if it doesn't
def check_dirs(dir):
	dir_full = os.path.join(wallpaper_dir, dir)
	if (os.path.exists(dir_full) == False):
		os.makedirs(dir_full)
	return dir_full

# show image and prompt user whether they want to set it or not
def prompt_and_show(file):
	subprocess.call(file, shell=True) # open the image
	# prompt user
	response = input("Opening the image. Want to add this one to your wallpapers? (Y/N) ")

	# make sure they enter a y or n
	while (response.lower() != "y" and response.lower() != "n" and response.lower() != 'quit'):
			response = input("Invalid input. Please enter Y or N: ")
			if (response.lower() == "n"):
				print ("Removing file: %s\n" % file)
				os.remove(file) # remove the file is they say no
			elif (response.lower() == "y"):
				sys.exit("Sounds good!")
			elif (response.lower() == 'quit'):
				sys.exit("\nSee ya later!")
	
	
#
#begin main program
#
print ("\nHi I'm the WallpaperGrabber!")

# iterate through subreddit list
for subreddit in subreddits:
	print ("\nCurrently grabbing wallpapers from /r/%s..." % subreddit)
	sub = r.get_subreddit(subreddit) #set the subreddit to get pictures from, in this case '/r/spaceporn'
	links = sub.get_hot() #get hot links

	#iterate through reddit links looking for one that meets:
	#   direct link to picture
	#   has resolution of at least 1920x1080
	while (True):
		submission = next(links) #grab the top one
		url = submission.url
		title = submission.title

		if "reddit" not in url and "gfycat" not in url:
			if "[" in title:
				dims = get_dimensions(title)
				if ('oc' in dims[0] or 'OC' in dims[0]):
					continue
				elif (int(dims[0]) >= 1920 and int(dims[1]) >= 1080):
					break
		
	print ("Downloading image: %s" % title)
	print ("Image url: %s\n" % url)

	# check that the necessary directory exists and download the file
	dir_full = check_dirs(subreddit)
	file = os.path.join(dir_full, title)
	urllib.request.urlretrieve(url, file)

	# get the type of image, and give the file the correct file type
	# then show the file to make sure it looks good
	image_type = imghdr.what(file)
	if (image_type):
		new_file = os.path.join(dir_full, title + '.' + image_type)
		if (os.path.exists(os.path.join(dir_full, new_file))):
			print ("We already have this Wallpaper!\n")
			os.remove(file)
		else:
			os.rename(file, new_file)
			prompt_and_show(new_file)
	else:
		print ("Unable to determine file type so I can't use grab this wallpaper, sorry.")
		os.remove(file)


	
