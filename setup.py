import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='fyers_apiv2',  
     version='2.0.5',
     author="Fyers-Tech",
     author_email="support@fyers.in",
     description="Fyers trading APIs.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/FyersDev/fyers-api-py",
     packages=setuptools.find_packages(),
     install_requires=[
                'requests==2.25.1',
                'tornado==6.1',
                'asyncio==3.4.3',
                'websockets==8.1',
                'websocket-client==1.2.1'
          ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
