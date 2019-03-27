import os
from pathlib import Path
import glob
from xml.etree import ElementTree as ET


def xml_split(file_to_split, tag_to_split_on, splits_to_generate=0):
    """Splits an XML file into multiple files. Places output files in output subdirectory of input file location.

    Args:
        file_to_split: Path to the file to split.
        tag_to_split_on: Tag/element within the XML to split on. Should be a top-level tag, just under the root.
        splits_to_generate: Number of files (splits) to generate, distribution round robin. If not specified, will
            split each found tag_to_split_on into it's own file.

    """
    # Quickly open and close file to capture file name/path
    input_file = open(file_to_split)
    input_file_name = input_file.name.replace(Path(input_file.name).name, Path(input_file.name).stem)
    input_file.close()

    split_tag = tag_to_split_on
    num_files = splits_to_generate

    context = ET.iterparse(file_to_split, events=('end',))

    if num_files == 0:
        index = 0
        for event, elem in context:
            if elem.tag == split_tag:
                index += 1
                with open(input_file_name + '_' + str(index).rjust(4, '0') + '.xml', 'wb') as f:
                    f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
                    f.write(ET.tostring(elem))
    else:
        xml_element_tree_list = [None for i in range(num_files)]

        tree_num = 0
        for event, elem in context:
            if elem.tag == split_tag:
                if xml_element_tree_list[tree_num] is None:
                    xml_element_tree_list[tree_num] = ET.Element('XMLELEMENT')
                    xml_element_tree_list[tree_num].extend(elem.iter(split_tag))
                else:
                    xml_element_tree_list[tree_num].extend(elem.iter(split_tag))

                if tree_num >= (num_files - 1):
                    tree_num = 0
                else:
                    tree_num += 1

        for file_num in range(num_files):
            if xml_element_tree_list[file_num] is not None:
                with open(input_file_name + '_' + str(file_num).rjust(4, '0') + '.xml', 'wb') as f:
                    f.write(ET.tostring(xml_element_tree_list[file_num]))


def xml_combine(files_to_combine, tag_to_combine_on):
    """Combines multiple XML files into one. Places output file in output subdirectory of input file location.

    Args:
        files_to_combine: Path containing the files to combine.
        tag_to_combine_on: Tag/element within the XML to combine on. Ideally a top-level tag, just under the root.

    """
    tag_to_find = ".//" + tag_to_combine_on
    xml_files = glob.glob(files_to_combine + "/*.xml")
    xml_element_tree = ET.Element('XMLELEMENT')

    # See if output subdir exists, and if not create it
    if not os.path.exists(files_to_combine + "/output"):
        os.makedirs(files_to_combine + "/output")

    for xml_file in xml_files:
        data = ET.parse(xml_file).getroot()
        if data.tag != tag_to_combine_on:
            data = ET.parse(xml_file).find(tag_to_find)

        xml_element_tree.append(data)

    if xml_element_tree is not None:
        output_file = open(files_to_combine + "/output/output.xml", 'wb')
        output_file.write(ET.tostring(xml_element_tree))
