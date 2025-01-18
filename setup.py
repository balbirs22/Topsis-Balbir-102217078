from setuptools import setup, find_packages

setup(
    name='Topsis-Balbir-102217078',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis_Balbir_102217078.topsis:main',
        ],
    },
    author='Balbir Bhatia',
    author_email='balbirs2204@gmail.com',
    description='''
        Topsis-Balbir-102217078 is a Python package for multi-criteria decision making using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method. This package enables users to easily apply TOPSIS analysis to datasets provided in CSV format. It is particularly useful for businesses and researchers in fields like supply chain management, engineering, and finance who need to rank alternatives based on multiple criteria.
        
        Key features include:
        - Easy integration with Pandas DataFrames.
        - Customizable weights and criteria impacts (positive or negative).
        - Automatic normalization and scoring of alternatives based on user-defined preferences.
        - Command line interface for quick analysis runs.
        
        With Topsis-Balbir-102217078, decision-makers can quantitatively evaluate and rank options, thereby facilitating more informed and objective decision-making processes.
    '''
)
