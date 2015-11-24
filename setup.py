import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# grab version directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'librato_bg'))
from version import VERSION

long_description = '''
Provides an easy API to submit Librato metrics in a background thread.
'''

setup(
    name='librato_bg',
    version=VERSION,
    url='https://github.com/nyaruka/python-librato-bg',
    author='Nyaruka',
    author_email='code@nyaruka.com',
    maintainer='Nyaruka',
    maintainer_email='code@nyaruka.com',
    packages=['librato_bg'],
    license='MIT License',
    install_requires=[
        'librato-metrics',
    ],
    description=long_description,
    long_description=long_description
)
