# from aptk.__version__ import release
import sys, os

from setuptools import setup, find_packages

long_desc = '''
This package contains tools for easy sphinx domain creation.
'''

try:
    sys.path.insert(0, 'sphinxcontrib')
    import domaintools
except ImportError as e:
    import logging
    logging.warning("Unable to import domaintools module.", exc_info=e)
    class domaintools:
        __version__ = "unknown"

requires = ['Sphinx>=1.0', 'docutils']

setup(
    name='sphinxcontrib-domaintools',
    version=domaintools.__version__,
    url='http://bitbucket.org/klorenz/sphinxcontrib-domaintools',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-domaintools',
    license='BSD',
    author='Kay-Uwe (Kiwi) Lorenz',
    author_email='kiwi@franka.dyndns.org',
    description='Sphinx extension for easy domain creation.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
