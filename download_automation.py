#There is no Unicorn,
#There is no Toothfairy,
#There is no Programming gf.

import os
import re
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler

path = 'C:/Users/Administrator/Downloads'

run = 1

print("--------------File Management Automation Running----------------")


#function to move the files
def move(path):
	os.chdir(path)
	entries = os.listdir()

	#to create the required directories, if it doesn't exist
	dir_list_name = ['Images', 'Videos', 'Audios', 'Documents']
	dir_list_flag = [0,0,0,0]

	for entry in entries:
		if entry == 'Images':
			dir_list_flag[0] = 1
		if entry == 'Videos':
			dir_list_flag[1] = 1
		if entry == 'Audios':
			dir_list_flag[2] = 1
		if entry == 'Documents':
			dir_list_flag[3] = 1

	for i in range(4):
		if dir_list_flag[i] == 0:
			os.mkdir(dir_list_name[i])


	for entry in entries:

		copying = True
		size1 = -1

		#to not to transfer file while its being copied.
		while copying:
			size = os.path.getsize(entry)
			if size == size1:
				break
			else:
				size1 = os.path.getsize(entry)
				time.sleep(1)

		if re.match('.*.jpg|.*.png|.*.tif|.*.gif|.*.jpeg|.*.JPG|.*.JPEG', entry):
			os.rename(entry, 'Images/' + entry)
		if re.match('.*.pdf|.*.csv|.*.doc|.*.docx|.*.ppt|.*.txt|.*.zip', entry):
			os.rename(entry, 'Documents/' + entry)
		if re.match('.*.mp3|.*.wav', entry):
			os.rename(entry, 'Audios/' + entry)
		if re.match('.*.mp4|.*.wmv', entry):
			os.rename(entry, 'Videos/' + entry)


#setting up watchdog on_modified
class handler(FileSystemEventHandler):
	i = 1
	def on_modified(self, event):
		move(path)


event_handler = handler()
observer = Observer()
observer.schedule(event_handler, path, recursive = True)
observer.start()

try:
	while run:
		time.sleep(100)
		move(path)
except KeyboardInterrupt:
	observer.stop()
	observer.join()