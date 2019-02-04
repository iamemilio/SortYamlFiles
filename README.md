# SortYamlFiles
This tool lets you sort kubernetes yaml files by the key of your choosing.

## Pre-Reqs
Make sure you have python 2 and pyYaml.
PYYaml can be installed like this:

```bash
pip install --user pyYaml
```

## Usage
When you run the file, it will print the results to standard out. By default, it will sort each file by its metadata.name. However, you may set the `--key` option to change this behavior.

```
usage: ./sortYaml.py [-h] [--key KEY] [--out OUT] fileName

positional arguments:
  fileName    the path to the file that you want to sort

optional arguments:
  -h, --help  show this help message and exit
  --key KEY   This changes the key you want to sort on from metadata.name to
              whatever you choose, as long as its a valid key. Please note
              that if you enter an invalid key, it will simply not sort the
              file.
  --out OUT   Write to a file rather than print in standard out. This will
              overwrite existing files with the same name.
```
