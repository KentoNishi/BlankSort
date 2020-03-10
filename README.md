# [BlankSort](https://pypi.org/project/blanksort/)
The Python package for the BlankSort keyword extraction algorithm.

## Installation
Use the following command to install from TestPyPI:
```shell
pip install --upgrade blanksort
```

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

* `binary_path` [**optional**]
    * The path to the binary folder that contains `blanksort.database` and `stopwords-en.txt`. If not specified, the default binary files will be downloaded.
* `preloadVectors` [**optional keyword argument**]
    * A boolean (default `False`) that specifies if word vectors should be pre-loaded into memory.
* `saveGeneratedVectors` [**optional keyword argument**]
    * A boolean (default `False`) that specifies if word vectors generated on-the-fly should be saved to `blanksort.database`.


### Example 
```python
import blanksort
algo = blanksort.BlankSort()
keywords = algo.rank("[input text]")
```


## Binary Files

The BlankSort package requires several files, collectively referred to as "binaries".
| File name            | Description                                        |
|:---------------------|:---------------------------------------------------|
| `blanksort.database` | A database file created using [SQLiteDict](https://github.com/RaRe-Technologies/sqlitedict). The database contains word vectors and n-grams imported from [FastText](https://fasttext.cc/).
| `stopwords-en.txt`   | A text file containing a list of stop words for pre-processing. Each line should contain a single word. |

If the files are not found in the `binary_path`, the package will download the default binary folder from the latest version of `binaries.zip` attached to a release.