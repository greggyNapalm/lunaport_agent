import os
import re
from setuptools import setup, find_packages


base_path = os.path.dirname(__file__)

# Get the version (borrowed from SQLAlchemy)
fp = open(os.path.join(base_path, 'lunaport_agent', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'",
                     re.S).match(fp.read()).group(1)
fp.close()

setup(
    name='lunaport_agent',
    version=VERSION,
    author='Gregory Komissarov',
    author_email='gregory.komissarovv@gmail.com',
    description='Daemon with HTTP interface that manages load tools(yandex.tank)',
    license='Apache License, Version 2.0',
    url='https://github.com/greggyNapalm/lunaport_agent',
    keywords=['load', 'lunaport', 'yandex.tank', 'api'],
    packages=[
        'lunaport_agent',
    ],
    zip_safe=False,
    install_requires=[
       #'requests==1.2.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
