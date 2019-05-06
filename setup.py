# from aptk.__version__ import release
import sys

from setuptools import setup, find_packages, Command


class Version(Command):
    description = 'Outputs the current version of the package'
    user_options = []
    boolean_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from setuptools_scm import get_version

        print('Current version is: ' + get_version(root='.', relative_to=__file__))


sys.path.insert(0, 'sphinxcontrib')

long_desc = '''
This package contains tools for easy sphinx domain creation.
'''

setup(
    name='sphinxcontrib-domaintools',
    use_scm_version=True,
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
    install_requires=['Sphinx>=1.0', 'docutils'],
    setup_requires=['setuptools_scm'],
    cmdclass={
        'version': Version
    },
    namespace_packages=['sphinxcontrib'],
)
