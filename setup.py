from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="papermerge-meta-plugin-ard-zdf-deutschlandradio",
    version="1.0.0",
    author="Eugen Ciur",
    author_email="eugen@papermerge.com",
    include_package_data=True,
    url="https://github.com/papermerge/papermerge-meta-plugin-ard-zdf-deutschlandradio",  # noqa
    description="metadata extractor plugin for ARD ZDF Rundfunkbeiträge data extraction.",  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0 License",
    keywords="metadata, papermerge, plugin, receipts",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
