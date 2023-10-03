from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hkm_amd/__init__.py
from hkm_amd import __version__ as version

setup(
	name="hkm_amd",
	version=version,
	description="Hare Krishna Mandir Ahmedabad",
	author="HKM Ahmedabad",
	author_email="ugsd08@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
