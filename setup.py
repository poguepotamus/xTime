#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name='xTime',
	version='0.1',
	author='Matthew Pogue',
	author_email='matthewpogue606@gmail.com',
	description='A small tool that converts a current csv file to a lined output, wither it be another csv file, or a formatted paragraph. This uses a formatted string gathered from the header of the csv file.',
	url='matthewpogue.com',
	packages=find_packages(),
	classifiers=(
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.6",
		"Operating System :: OS Independent",
	),
	install_requires=[
		'pyperclip',
		'tabulate',
	],
)