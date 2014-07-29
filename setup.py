from setuptools import setup

setup(
    name='foot-fixtures',
    version='1.0.0',
    author_email='hsharma1205@gmail.com',
	py_modules=['fixtures'],
    entry_points={
        'console_scripts': [
            'fixtures = fixtures:main',
        ],
    },
    url = 'https://github.com/supercr7/foot-fixtures',
	download_url = 'https://github.com/supercr7/foot-fixtures/tarball/1.3',
    install_requires=[
        'colorama==0.3.1'
    ],
    classifiers=[
      'Environment :: Console'
    ],
)


