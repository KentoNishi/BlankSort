# [BlankSort](https://test.pypi.org/project/blanksort/)
The prerelease Python package for the BlankSort keyword extraction algorithm.

<!--
![Upload Python Package](https://github.com/KentoNishi/BlankSort-Prerelease/workflows/Upload%20Python%20Package/badge.svg)
-->

## Installation
Use the following command to install from TestPyPI:
```shell
pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --upgrade blanksort
```
The package will be available on PyPI in the near future.

## Usage

BlankSort can be imported like any other Python package:
```python
import blanksort
```
After importing, you can create a `BlankSort` object.
```python
algo = blanksort.BlankSort()
```
Alternatively, you can use the following code to create the `BlankSort` object.
```python
from BlankSort import *
algo = BlankSort()
```
The `BlankSort` constructor accepts the following arguments:

* binary_path [**optional**]
    * The path to the binary folder that contains `blanksort.database` and `stopwords-en.txt`. If not specified, the default binary files will be downloaded.
* preloadVectors [**optional keyword argument**]
    * A boolean (default `False`) that specifies if word vectors should be pre-loaded into memory.
* preloadVectors [**optional keyword argument**]
    * A boolean (default `False`) that specifies if word vectors generated on-the-fly should be saved to `blanksort.database`.

### Example 
```python
import blanksort
algo = blanksort.BlankSort()
keywords = algo.rank("[input text]")
```