"""Misc Tools and wrappers"""
__version__ = '0.0.5'

from setuptools import setup, find_packages
from thundersnow import ioutil


requirements = list(ioutil.iterlines('requirements.txt'))



setup(
    name='thundersnow',
    version=__version__,
    url='https://github.com/dillonhicks/thundersnows',
    license='Apache License Version 2.0',
    author='Dillon Hicks',
    author_email='dillon@dillonhicks.io',
    description='ThuderSnow',
    long_description=__doc__,
    package_dir={'': '.'},
    namespace_packages=[],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
