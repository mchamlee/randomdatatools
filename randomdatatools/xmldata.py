import sys
import glob
from xml.etree import ElementTree as ET


def xml_split(file_to_split, tag_to_split_on, splits_to_generate=0):
    """Splits an XML file into multiple files. Places output files in output subdirectory of input file location.

    Args:
        file_to_split: An open() file object of the file to split.
        tag_to_split_on: Tag/element within the XML to split on. Should be a top-level tag, just under the root.
        splits_to_generate: Number of files (splits) to generate. If not specified, will split each found
            tag_to_split_on into it's own file.

    Raises:
        FileNotFoundError: file_to_split was not found.
    """
    pass


def xml_combine(files_to_combine, tag_to_combine_on):
    """COmbines multiple XML files into one. PLaces output file in output subdirectory of input file location.

    Args:
        files_to_combine: An glob() file object of the files to combine.
        tag_to_combine_on: Tag/element within the XML to combine on. Ideally a top-level tag, just under the root.

    Raises:
        FileNotFoundError: No files found in the glob object.
    """
    pass
