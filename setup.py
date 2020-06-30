import setuptools

setuptools.setup(
    name='rm',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
