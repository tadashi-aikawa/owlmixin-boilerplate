import re

from setuptools import setup, find_packages

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

APP_NAME = 'yourapp'

here = os.path.abspath(os.path.dirname(__file__))

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

def load_readme():
    with open(os.path.join(here, 'README.md')) as f:
        return f.read()


setup(
    name=APP_NAME,
    version=re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        open(f'{APP_NAME}/__init__.py').read()).group(1),
    description='Your app description.',
    long_description=load_readme(),
    license='MIT',
    author='your name',
    author_email='your email address',
    maintainer='your name',
    maintainer_email='your email address',
    url='http://yoursite',
    install_requires=requires,
    extras_require={'test': test_requirements},
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': [
            f'{APP_NAME} = {APP_NAME}.main:main'
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)
