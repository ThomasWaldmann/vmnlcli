from setuptools import setup


with open("README.md") as f:
    long_description = f.read()
    # remove header, but have one \n before first headline
    start = long_description.find("# vmnlcli")
    assert start >= 0
    long_description = "\n" + long_description[start:]


setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
)
