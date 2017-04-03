from setuptools import setup
from setuptools import find_packages

REQUIREMENTS = [
  "thumbor==6.3.1",
  "google-cloud-storage==1.0.0",
  "google-auth==0.10.0"
]

setup(
  name="thumbor_cloud_storage",
  version="2.1.0",
  author="Pedro Gimenez",
  author_email="me@pedro.bz",
  description="Thumbor's Google Cloud Storage loader and result storage",
  url="https://github.com/pedrogimenez/thumbor-cloud-storage",
  license="MIT",
  include_package_data=True,
  packages=find_packages(),
  install_requires=REQUIREMENTS,
  zip_safe=False
)
