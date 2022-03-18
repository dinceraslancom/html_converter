from setuptools import setup, find_packages

requires = [
    'html5lib'
]

with open("README.rst", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name='html_converter',
    version='1.0.0',
    package_dir={'html_converter': 'html_converter'},
    author="Dincer Aslan",
    author_email="dinceraslan.com@gmail.com",
    description="HTML converter tool",
    long_description=readme,
    long_description_content_type='text/x-rst',
    url="https://github.com/dinceraslancom/html_converter",
    project_urls={
        'Source': 'https://github.com/dinceraslancom/html_converter',
    },
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.3",
)
