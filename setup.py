import re

from setuptools import setup

APP_NAME = 'yourapp'

requires = [
    'owlmixin',
    'fn',
    'docopt',
    "requests"
]
extras = {
    'test': ['pytest']
}

setup(
    name=APP_NAME,
    version=re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        open(f'{APP_NAME}/__init__.py').read()).group(1),
    install_requires=requires,
    test_requires=extras['test'],
    extras_require=extras,
    entry_points={
        'console_scripts': [
            f'{APP_NAME} = {APP_NAME}.main:main'
        ],
    },
)
