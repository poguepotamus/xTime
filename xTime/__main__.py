#!/usr/bin/python

# A program to join files

import os, sys, re
import pyperclip
from tabulate import tabulate

class TimeCopy():
	def __init__(self, arguments):
		self._setup_setupHelp()

		self._inputFile = 'Toggl_time_entries_2018-09-10_to_2018-09-16.csv'
		self._format = "{Start date}\t{Client} - {Project}\t{Task}\t{Description}\t\t{Amount (USD)}"
		self._copyToClipboard = False
		self._outputFile = None
		self._printToTerminal = False
		self._printLineCount = False

		self._setup_getArguments(arguments)

		self.formattedContent = self._getFileContent

	def _setup_setupHelp(self):
		self.helpMessage = (
			'This is the help message:\n'
			'	on multiple lines?'
		)

	def _setup_getArguments(self, arguments):

		### Input file #################
		try:
			self._inputFile = arguments[1]
		except IndexError:
			self.printHelp()
			exit()
		del arguments[0:2]

		### Predefined Tags ############
		outputFileTags       =  ['-o', '--output', '--outputFile']
		copyToClipboardTags  =  ['-c', '--copy', '--clipboard']
		formattingTag        =  ['-f', '--formatting', '--format']
		printToTerminalTags  =  ['-p', '--print']
		linesTag             =  ['-l', '--lines', '--lineCount']

		### Setting tags from arguments #
		while len(arguments) > 0:
			### TAGS ###########################################################
			# Output files #############
			if arguments[0] in outputFileTags:
				self._outputFiles = arguments[1]
				del arguments[1]


			# Formatting ###############
			if arguments[0] in formattingTag:
				self._format = arguments[1]
				del arguments[1]


			# Copy to clipboard ########
			elif arguments[0] in copyToClipboardTags:
				self._copyToClipboard = True


			# Print to terminal ########
			elif arguments[0] in printToTerminalTags:
				self._printToTerminal = True


			# Output lines count #######
			elif arguments[0] in linesTag:
				self._printLineCount = True


			# Unknown tags #############
			else:
				try:
					raise Exception(f'Unknown argument [{arguments[0]} {arguments[1]}].')
				except IndexError:
					raise Exception(f'Unknown argument [{arguments[0]}].')
				exit()


			# Removing tag itself ######
			del arguments[0]

	def _getFileContent(self, inputFile=None):
		# Default arguments
		if inputFile is None:
			inputFile = self._inputFile

		### Getting file contents
		header = None
		inputFileContentsList = []
		# Collecting the file information and storing it in a list
		with open(inputFile, 'r') as inputFileContents:
			for line in inputFileContents:
				# Handling the header
				if header == None:
					header = [key.strip() for key in line.split(',')]
					continue

				# If the header already exists
				inputFileContentsList.append([key.strip() for key in line.split(',')])

		# Taking the file contents and storing it in a dictionary like format (almost like a table
		inputFileTable = []
		for line in inputFileContentsList:
			inputFileTable.append(dict(zip(header, line)))

		# Returning this list of dictionaries
		return inputFileTable

	def _writeToFile(self, outputFile=None):
		# Default arguments
		if outputFile is None:
			outputFile = self.outputFile

		# Printing to the outputFile
		self.printFormattedContent()

	def _getFormattedContent(self):
		# Go through each line in the input file and format it
		outputContent = []
		try:
			for line in self.fileContents:
				outputContent.append( self._format.format(**line) + '\n' )
		except KeyError as error:
			print(f'FATAL ERROR: [{error}] is not a valid key in input format.')

		return outputContent

	def printHelp(self):
		print(self.helpMessage)

	def printFormattedContent(self):
		print(self._formattedContent)

	def execute(self):
		print()

		# Finding input file and reading it in
		self.fileContents = self._getFileContent()

		# Getting the correct formatted content
		self._formattedContent = self._getFormattedContent()

		# Printing line count if requested
		if self._printLineCount:
			print(f'{len(self._formattedContent)} lines were created.')

		# Printing to the terminal if requested
		if self._printToTerminal:
			# print(type(self._formattedContent))
			print(tabulate([line.split('\t') for line in self._formattedContent]))

		# Printing to outputFile is requested
		if self._outputFile is not None:
			self._printToFile()
			print(f'Output written to {self._outputFile} successfully.')

		# Copying to clipboard if requested
		if self._copyToClipboard:
			pyperclip.copy(''.join(str(line) for line in self._formattedContent))
			print('Output copied successfully.')

		print()

def main():
	_ = TimeCopy(sys.argv)
	_.execute()


if __name__ == '__main__':
	main()