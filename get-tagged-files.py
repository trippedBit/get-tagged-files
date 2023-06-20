import argparse
import glob
import os
import shutil

argParser = argparse.ArgumentParser()
argParser.add_argument("searchPattern",
                       type=str,
                       help="Pattern to search files in combination with glob.glob")
argParser.add_argument("-filterList",
                       nargs="*",
                       help="List of strings to filter the found files")
argParser.add_argument("-targetDirectory",
                       default=os.getcwd(),
                       type=str,
                       help="Target directory for the copy process, defaults to the current directory")

progArgs = argParser.parse_args()
print("Used arguments are:")
print(progArgs.searchPattern,
      progArgs.filterList,
      progArgs.targetDirectory)
print("")

# Get the matching files as list
fileList: list = glob.glob(progArgs.searchPattern,
                           recursive=True)

# Search for files which do NOT contain the filters
containsFilter: bool = False
remainingFiles: list = []
for file in fileList:
    containsFilter = False
    for filter in progArgs.filterList:
        if filter in file:
            containsFilter = True
            break
    if containsFilter is False:
        remainingFiles.append(file)  # The file does not contain any filter string, add to result list

print(remainingFiles)

# Create target directory if it does not exist
if not os.path.exists(progArgs.targetDirectory):
    os.makedirs(progArgs.targetDirectory)

# Copy all files into target directory
for file in remainingFiles:
    shutil.copy(file,
                progArgs.targetDirectory)
