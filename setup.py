from setuptools import find_packages, setup

setup(
    name='mathbox',
    python_requires='>=3.8.0',
    version='0.0.5',
    description="A math toolbox.",
    author='freedeaths',
    author_email='register917@gmail.com',
    url='https://github.com/freedeaths/mathbox-py.git',
    #package_dir={'': 'mathbox'},
    packages=find_packages(exclude=["tests"]),
    #packages=['mathbox', 'mathbox/*'],
    install_requires=[],
    include_package_data=True,
    license="MIT",
    keywords=['math', 'data-processing'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
)