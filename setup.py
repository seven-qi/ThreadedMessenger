try:
    from setuptools import setup 
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is a coding exc',
    'author': 'Jingwei Qi',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'seven.qi2011@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'threadedmessenger'
}

setup(**config)