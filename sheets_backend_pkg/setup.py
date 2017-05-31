
from setuptools import setup

version = open('VERSION.txt').read()

setup(name='sheets_backend',
        version=version,
        description='backends for managing sheets objects',
        url='http://github.com/chuck1/sheets_backend',
        author='Charles Rymal',
        author_email='charlesrymal@gmail.com',
        license='MIT',
        packages=[
            'sheets_backend',
            'sheets_backend.sockets',
            'sheets_backend.tests',
            'sheets_backend.tests.conf',
            'sheets_backend.templates',
            ],
        zip_safe=False,
        scripts=[
                'bin/web_sheets_sheets_backend.py',
                ],
        package_data={'': ['*.service']},
        install_requires=[
            'jinja2',
            'modconf',
            'sheets']
            )

