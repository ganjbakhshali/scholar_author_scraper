from setuptools import setup, find_packages

setup(
    name='researcher_papers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scholarly',
    ],
    entry_points={
        'console_scripts': [
            'researcher-papers=researcher_papers.main:main',
        ],
    },
    author='Your Name',
    author_email='ganjbakhsh.ali@gmail.com',
    description='A package to fetch and save Google Scholar papers for a given researcher name',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ganjbakhshali/scholar_author_scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
