#!/bin/python
import argparse
import yaml


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fileName",
        help="the path to the file that you want to sort"
    )
    parser.add_argument(
        "--key",
        default="metadata.name",
        help="This changes the key you want to sort on from " +
        "metadata.name to whatever you choose, as long as its a valid key." +
        " Please note that if you enter an invalid key, it will simply" +
        " not sort the file."
    )
    parser.add_argument(
        "--out",
        default="",
        help="Write to a file rather than print in standard out. This will " +
        "overwrite existing files with the same name."
    )
    args = parser.parse_args()
    return args.fileName, args.key, args.out


def splitIntoFiles(fileName):
    yaml = ""
    with open(fileName) as file:
        yaml = file.read()
    return yaml.split("---")


def keyVal(data, key):
    key = key.split(".")
    check = data
    for i in range(len(key)):
        if i > 0:
            check = check[key[i-1]]
        if key[i] not in check:
            return False, ""

    return True, check[key[-1]]


def mapByKey(files, key):
    fileMap = {}
    countUnnamed = 0
    for file in files:
        if file != None and file != "\n":
            data = yaml.load(file)
            hasKey, keyName = keyVal(data, key)
            if hasKey:
                fileMap[keyName] = file
            else:
                fileMap[str(countUnnamed)] = file
                countUnnamed += 1
    return fileMap


def sortAndDumpYaml(fileMap):
    sortedKeys = sorted(fileMap)
    outfile = ""
    first = True
    for key in sortedKeys:
        if first:
            outfile = fileMap[key]
            first = False
        else:
            outfile = outfile + "---" + fileMap[key]
    return outfile


def main():
    fileName, key, out = getArgs()
    files = splitIntoFiles(fileName)
    fileMap = mapByKey(files, key)
    outfile = sortAndDumpYaml(fileMap)
    if out == "":
        print outfile
    else:
        f = open(out, "w")
        f.write(outfile)
        f.close()

if __name__ == "__main__":
    main()
