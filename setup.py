from distutils.core import setup

setup(
    name='PyChain',
    version='0.0.1',
    packages=['chain'],
    author='Marsel Mavletkulov',
    author_email='marselester@ya.ru',
    url='https://github.com/marselester/pychain',
    description='Python API client for Chain.com',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests>=1.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
