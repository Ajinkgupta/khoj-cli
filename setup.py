from setuptools import setup, find_packages

setup(
    name='khoj-cli',
    version='1.0',
    packages=find_packages(),
  install_requires=[
        'requests',
        'colorama',
        'beautifulsoup4'
    ],
   entry_points={
    'console_scripts': [
        'khoj = khoj.khoj:main'
    ]
},


    author='Ajink Gupta',
    author_email='guptaajink21@gmail.com',
    description='CLI tool for searching using Khoj',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ajinkgupta/khoj-cli',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
