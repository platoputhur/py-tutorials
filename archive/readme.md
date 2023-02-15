LAMBDA

setup lambda in aws with some basic function
then create a directory for lmbda package
check pip version > 19
install the required packages by the command below
```shell
pip install --platform manylinux2014_x86_64 --target ytinfo --implementation cp --python 3.9 --only-binary=:all: --upgrade pytube
```
cd into the package `ytinfo`
write the function as required, but the function name should be `lambda_handler`
`zip -r ytinfo.zip .` to zip the archive
