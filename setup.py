from setuptools import setup, find_packages

setup(name='sputils',
      version='0.1',
      py_modules=["sputils"],
      description='SharePoint utils',
      long_description='functions to download and upload files from SharePoint',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: SharePoint Automation :: File Movement',
      ],
      keywords='upload download SharePoint files',
      url='http://github.com/whatscottcodes',
      author='SNelson',
      author_email='scott.nelsonjr@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown', 'Office365-REST-Python-Client'
      ],
      include_package_data=False,
      zip_safe=False)