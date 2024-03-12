from setuptools import setup, find_packages

setup(
    name='free_proxy_verifyer',
    version='1.0.0',
    author='Mominur Rahman',
    author_email='mominurr518@email.com',
    description='A simple package to verify working proxies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mominurr/free_proxy_verifyer',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
