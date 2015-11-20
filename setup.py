from setuptools import setup, find_packages

def _is_requirement(line):
    """Returns whether the line is a valid package requirement."""
    line = line.strip()
    return line and not line.startswith("#")

def _read_requirements(filename):
    """Parses a file for pip installation requirements."""
    with open(filename) as requirements_file:
        contents = requirements_file.read()
    return [line.strip() for line in contents.splitlines() if _is_requirement(line)]

# Don't import module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'librato_bg'))
from version import VERSION

setup(
    name='librato_bg',
    version=VERSION,
    license="BSD",

    install_requires=_read_requirements("requirements/base.txt"),
    tests_require=_read_requirements("requirements/tests.txt"),

    description="Background submitter for Librato events.",
    long_description=open('README.md').read(),

    author='Nyaruka Ltd',
    author_email='code@nyaruka.com',

    url='http://github.com/nyaruka/python-librato-bg',

    include_package_data=True,

    packages=find_packages(),

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
