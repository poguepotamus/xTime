#!/usr/bin/python

# A program to join files

import os, sys, re
import pyperclip

def getFileData(filename):
	header == None

	with open(filename) as inputFile:
		for line in inputFile:
			if header == None:
				header = line

def getFiles(path, extensions=None, filterKeys=None, trimKeys=None):

	# Create an empty file set to return
	files = []

	# Listing through each filestring
	stringFiles = os.listdir(path)
	for fileString in stringFiles:

		# Splitting the file by its extention and septerating it into easily workable parts
		file = fileString.rsplit('.', 1)
		file[0] = file[0].split('_')
		for part in file[0]:
			part = part.strip()
		if re.search(r'\([0-9]+\)', file[0][-1][-3:]):
			file[0][-1] = file[0][-1][:-3].strip()

		# If the file didn't have an extention, then we don't keep it.
		if len(file) == 1:
			continue

		### EXTENSIONS #########################################################
		if extensions is not None:

			# Checking the file extension directly
			# If the extension is not in our extensions list, then we continue out of the main loop
			if file[-1] not in extensions:
				continue

		### FILTER KEYS ########################################################
		if filterKeys is not None:

			# Setting a flag to check when we break out of the loop. Since were
			#  in a nested loop, we can't break out of the main loop without
			#  this flag
			exitLoop = False

			# Iterating through all the keys in the filename to see if they are
			#  in our filter keys
			for key in file[0]:

				# If the key is in our filterKeys
				if key in filterKeys:

					# Set our flag, and we have enough information to exit the loop
					exitLoop = True
					break

			# Checking the flag we set earlier
			if exitLoop:
				# We don't want this file, but we still want to check the rest of the files
				continue

		### TRIM KEYS ##########################################################
		if trimKeys is not None:

			# For each key in our filename
			for key in trimKeys:

				file[0] = trimKey(file[0], key)

		### OUTPUT #############################################################
		# Appending a dictionary to files
		files.append( {
			'filename':          fileString,
			'programName':       file[0][0],
			'year':              file[0][1],
			'month':             file[0][2],
			'date':              file[0][3],
			'time':              file[0][4],
			'sessionID':         file[0][-2],
			'participantName':   file[0][-1],
			'extention':         file[1],
		} )

	return files

def trimKey(trimList, key):
	return [value for value in trimList if value != key]

def printFiles(path):
	for file in getFiles(path, filterKeys = FILTER_KEYS, trimKeys = TRIM_KEYS):
		for key, value in file.items():
			if key == 'filename':
				print(f'\n{value}')
			print(f'    {key} | {value}')

class TimeCopy():
	def __init__(self, arguments):
		self._setup_setupHelp()

		self.inputFile = None
		self.outputFile = None

		self._setup_getArguments(arguments)

	def _setup_setupHelp(self):
		self.helpMessage = (
			'This is the help message:\n'
			'	on multiple lines?'
		)

	def _setup_getArguments(self, arguments):

		### Input file
		try:
			self.inputFile = arguments[1]
		except IndexError:
			self.printHelp()
			exit()

		### Tags
		outputFileTags = ['-o', '--output', '--outputFile']

		while len(arguments) > 2:
			### TAGS ###########################################################
			if arguments[2][0] == '-':

				### Output file ########
				if arguments[2] in outputFileTags:
					self.outputFile = arguments[3]
					del arguments[3]

				### Unknown tag ########
				else:
					try:
						raise Exception(f'Unknown argument [{arguments[2]} {arguments[3]}].')
					except IndexError:
						raise Exception(f'Unknown argument [{arguments[2]}].')
					exit()


				del arguments[2]



			### ARGUMENTS ######################################################

	def printHelp(self):
		print(self.helpMessage)

	def _getFileContent(self, inputFile=None):
		# Default arguments
		if inputFile is None:
			inputFile = self.inputFile

		### Getting file contents
		header = None
		inputFileContentsList = []
		# Collecting the file information and storing it in a list
		with open(inputFile, 'r') as inputFileContents:
			for line in inputFileContents:
				# Handling the header
				if header = None:
					header = [key.strip() for key in key.split(',')]
					continue

				# If the header already exists
				inputFileContentsList.append([key.strip() for key in key.split(',')])

		# Taking the file contents and storing it in a dictionary like format (almost like a table
		inputFileTable = []
		for line in inputFileContentsList:
			inputFileTable.append(dict(zip(header, line)))

		# Returning this list of dictionaries
		return inputFileTable

	def _printToFile(self, outputFile=None):
		# Default arguments
		if outputFile is None:
			outputFile = self.outputFile

		# Printing to the outputFile


	def execute(self):

		# Finding input file and reading it in
		self.fileContents = self._getFileContent()

		# Printing to outputFile is requested
		if self.outputFile is not None:
			self._printToFile()

		header = None
		with open(self.inputFile, 'r') as inputFile:
			for line in inputFile:




		raise NotImplementedError('TimeCopy.execute() is not implemented :(')



def main():
	_ = TimeCopy(sys.argv)
	_.execute()


if __name__ == '__main__':
	main()