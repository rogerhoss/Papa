from setuptools import setup, find_packages

setup(
    name         = 'Papa',
    version      = '1.0',
    packages     = find_packages(),
    package_data = {'Papa': ['resources/*.txt']},
    entry_points = {'scrapy': ['settings = Papa.settings']},
)
