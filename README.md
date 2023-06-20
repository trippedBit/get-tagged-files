# get-tagged-files
This script collects all files matching a given pattern, removes everything which matches filters and copies the remaining files into a given director.y
<br><br>
## License
Please see [LICENSE](LICENSE)
<br><br>
## Requirements
The versions given in the list are the ones used to develop get-tagged-files. Other versions might work too.
* Python 3.9.6
<br><br>
## Usage
```
get-tagged-files.py [-h] [-filterList [FILTERLIST ...]] [-targetDirectory TARGETDIRECTORY] searchPattern

positional arguments:
  searchPattern         Pattern to search files in combination with glob.glob

optional arguments:
  -h, --help            show this help message and exit
  -filterList [FILTERLIST ...]
                        List of strings to filter the found files
  -targetDirectory TARGETDIRECTORY
                        Target directory for the copy process, defaults to the current directory
```
<br><br>
## Example
```
python get-tagged-files.py -filterList filter1 filter2 -targetDirectory C:\\collectedFiles C:\\*.txt
```
### What it does
The example above creates a list with all files matching C:\\*.txt.<br>
All entries which contain the filter strings filter1 or filter2, e.g. C:\\myFileWithfilter1.txt, get removed from this list again.<br>
Every file in the remaining list gets finally copied into the target directory.
The target directory will be created if it does not exist yet.