import setuptools

setuptools.setup(
    name='funicularexpertmachine',
    version='0.0.2',
    author='Daniel Tait',
    author_email='tait.djk@gmail.com',
    install_requires=['numpy', 'scipy'],
    description='FEM solver for univariate PDEs',
    url='https://github.com/danieljtait/funicular-expert-machine',
    packages=setuptools.find_packages(exclude=('docs',)),
)
