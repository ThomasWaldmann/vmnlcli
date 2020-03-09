"""
setup for vmnlcli package
"""

from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()
    # remove header, but have one \n before first headline
    start = long_description.find('# vmnlcli')
    assert start >= 0
    long_description = '\n' + long_description[start:]


setup(
    name='vmnlcli',
    version='0.2.0',
    url='http://github.com/thomaswaldmann/velomobielnl/',
    license='MIT',
    author='Thomas Waldmann',
    author_email='twaldmann@thinkmo.de',
    description='command line interface for some dutch velomobile websites',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="velomobile odometer cli velomobiel.nl intercitybike.nl welmers.net",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'vmnlcli = vmnlcli:main',
        ]
    },
    platforms='any',
    setup_requires=[],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
