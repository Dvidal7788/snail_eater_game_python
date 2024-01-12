from setuptools import setup, find_packages

setup(
    name='SnailEater',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'gunicorn',
        'numpy>=1.26'
    ],
    entry_points={
        'console_scripts': [
            'snail_eater=snail_eater:main',  # main logic is in snail_eater.py
        ],
    },
)
