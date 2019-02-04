#!/bin/python
import argparse
import yaml


def splitIntoFiles(fileName):
    yaml = ""
    with open(fileName) as file:
        yaml = file.read()
    return yaml.split("---")


def mapByName(files):
    fileMap = {}
    countUnnamed = 0
    for file in files:
        data = yaml.load(file)
        name = ""
        if "metadata" in data:
            if "name" in data["metadata"]:
                name = data["metadata"]["name"]
        if name == "":
            name = str(countUnnamed)
            countUnnamed += 1
        fileMap[name] = file
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
            outfile = outfile + "\n---\n" + fileMap[key]
    return outfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", help="the path to the file that you want to sort")
    args = parser.parse_args()
    fileName = args.fileName
    files = splitIntoFiles(fileName)
    fileMap = mapByName(files)
    outfile = sortAndDumpYaml(fileMap)
    print ""
    print outfile


if __name__ == "__main__":
    main()
