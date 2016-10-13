from setuptools import setup

setup(
    name="hasGeekInternshipSampleFlaskApp",
    version="1.0",
    author="Ashish Sareen",
    author_email="ashish.sareen@outlook.com",
    packages=["app"],
    include_package_data=True,
    license="LICENSE.txt",
    description=".",
    long_description=open("README.md").read(),
    install_requires=[
        'Flask>=0.11','Jinja2>=2.8'
    ],
)