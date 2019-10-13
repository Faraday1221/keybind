from setuptools import setup

setup(
    name="keybind",
    version="0.0.0",
    description="Prompt user to enter random keys",
    author="Jon Bruno",
    author_email="Faraday1221@gmail.com",
    url="https://github.com/Faraday1221/keybind",
    packages=["keybind"],
    install_requires=["numpy", "readchar"],
    license="MIT",
    long_description="",
    entry_points={
          'console_scripts': [
              'keybind = keybind.__main__'
          ]
    }
)