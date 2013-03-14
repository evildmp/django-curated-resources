import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-curated-resources',
    version = '0.1',
    packages = ['curated_resources'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Curated Resources manages and publishes information about available resources for training, development, documentation, and so on',
    long_description = README,
    url = 'https://github.com/evildmp/django-curated-resources/',
    author = 'Daniele Procida',
    author_email = 'daniele@vurt.org',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)