from setuptools import setup

setup(
    name="ccwc",
    description="Word count",
    version="1.0.0",
    py_modules=['ccwc'],
    author="Sumanth Thota",
    author_email="sumanththota7@gmail.com",
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'ccwc = ccwc:main',
        ]
    }
)