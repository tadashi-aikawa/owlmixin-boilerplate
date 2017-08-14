from setuptools import setup

requires = [
    'owlmixin',
    'fn',
    'docopt',
]
extras = {
    'test': ['pytest']
}

setup(
    name='yourapp',
    install_requires=requires,
    test_requires=extras['test'],
    extras_require=extras,
)