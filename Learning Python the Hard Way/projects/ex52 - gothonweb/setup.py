try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'PROJECT_DESC',
	'author': 'Noah Everly',
	'url': 'GIT_URL',
	'download_url': 'GIT_URL_DL',
	'author_email': 'williamneverly@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'PROJECT_NAME'
}


setup(**config)