from setuptools import setup

setup(
	name="lambdo",
	description="Just lambdo it",
	version="4.4.4",
	install_requires=["boto3", "glob2", "PyYAML"],
	py_modules=["lambdo"],
	entry_points={"console_scripts": ["lambdo=lambdo:main"]}
)
