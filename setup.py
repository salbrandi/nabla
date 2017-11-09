from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nabla',
    packages=find_packages(),
    version='0.1.0',
    author='Salvador Brandi',
    author_email='salbrandi@gmail.com',
    url='https://github.com/salbrandi/nabla',
    download_url='https://github.com/salbrandi/nabla/archive/0.1.tar.gz',
    py_modules=['transcript_string_matcher'],
    description='A Webservice for Scraping Transcripts out of Yabla Javascript Variables',
    long_description=long_description,
    install_requires = ['Click',
                        'flask',
                        'bs4',
                        'jinja2'],
    entry_points='''
        [console_scripts]
        nabla=nabla.click_commands:nabla
        ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='yabla transcript scrape html'
)
