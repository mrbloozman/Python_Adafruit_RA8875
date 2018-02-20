from setuptools import setup, find_packages
setup(
    name="Python_Adafruit_RA8875",
    version="0.1",
    packages=find_packages(),
    # scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=['Python_Adafruit_RA8875_h>=0.1'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Mark Schwartz",
    author_email="mrbloozman@gmail.com",
    description="This is a port to Python of the Adafruit_RA8875 Arduino library",
    license="BSD",
    # keywords="hello world example examples",
    # url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://www.github.com/mrbloozman/Python_Adafruit_RA8875",
    }

    # could also include long_description, download_url, classifiers, etc.
)