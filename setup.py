#!/usr/bin/env python3

from setuptools import setup

if __name__ == '__main__':
	setup(name='qthelpers',
		version='0.1',
		description='Libraries to build qt applications',
		long_description="""""",
		author='Raul Rodrigo Segura',
		author_email='raurodse@gmail.com',
		maintainer='Raul Rodrigo Segura',
		maintainer_email='raurodse@gmail.com',
		keywords=['software',''],
		url='https://github.com/edupals/python-edupals-qt',
		license='GPL',
		platforms='UNIX',
		packages = ['edupals.qt'],
		package_dir = {'edupals.qt':'src'}
	)
