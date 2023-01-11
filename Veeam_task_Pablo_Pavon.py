
#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import shutil
import sys
import logging
import time

class SynDirTool:

	def __init__(self,fromdir,todir):
		self.fromdir = fromdir
		self.todir = todir
 
	def synDir(self):
		self.__copyDir(self.fromdir,self.todir)
		 
	def __copyDir(self,fromdir,todir):
		self.__mkdir(todir)

		self.__deleteFile(self.fromdir,self.todir)

		for filename in os.listdir(fromdir):
			if filename.startswith('.'):
				continue
			fromfile = fromdir + os.sep + filename
			tofile = todir + os.sep + filename

			if os.path.isdir(fromfile):
				self.__copyDir(fromfile,tofile)
			else:
				self.__copyFile(fromfile,tofile)

	def __deleteFile(self,fromfile,tofile):
		
		for filename in os.listdir(tofile):		
			lista = os.listdir(fromfile)
			if not filename in lista:
				delete_file = os.path.join(tofile,filename)
				os.remove(delete_file)
				print(delete_file)
				logging.info("File %s ==> %s" %(" Deleted", delete_file))

 
	def __copyFile(self,fromfile,tofile):
		
		if not os.path.exists(tofile):		
			shutil.copy2(fromfile,tofile)
			logging.info("new %s ==> %s" %(" file", tofile))

		fromstat = os.stat(fromfile)
		tostat = os.stat(tofile)

		if int(fromstat.st_mtime) > int(tostat.st_mtime):
			shutil.copy2(fromfile,tofile)
			logging.info ("Update %s ==> %s" %("from file", tofile))

	def __mkdir(self,path):
				path=path.strip()
				path=path.rstrip(os.sep)
		
				isExists=os.path.exists(path)
		
				if not isExists:
					logging.info ('Directory successfully created=>'+path)
					os.makedirs(path)


if __name__ == '__main__':
	srcdir= input('Enter original file route: ')
	descdir= input('Enter destination route: ')
	tiempo_sincronizacion= input('Synchronization time: ')
	dirlog = input('Log file route: ')

	logging.basicConfig(filename=dirlog, level=logging.INFO)
	tool = SynDirTool(srcdir,descdir)
	try:
		while True:
			tool.synDir()
			time.sleep(int(tiempo_sincronizacion))
	except KeyboardInterrupt:
		print("Stopping the program due to Keyboard interrupt")