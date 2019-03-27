import sys
import os
import unittest
import glob
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from randomdatatools.xmldata import *


class TestXmlSplit(unittest.TestCase):
    xml_file_dir = "./test_files/"
    xml_file_small_path = xml_file_dir + "orderAuditList_small.xml"

    xml_file_small_split_000 = xml_file_dir + "orderAuditList_small_0000.xml"
    xml_file_small_split_001 = xml_file_dir + "orderAuditList_small_0001.xml"
    xml_file_small_split_002 = xml_file_dir + "orderAuditList_small_0002.xml"
    xml_file_small_split_003 = xml_file_dir + "orderAuditList_small_0003.xml"

    def test_small_default_split_positive(self):
        xml_split(self.xml_file_small_path, 'OrderAudit')

        self.assertTrue(os.path.isfile(self.xml_file_small_split_001))
        self.assertTrue(os.path.isfile(self.xml_file_small_split_002))
        self.assertTrue(os.path.isfile(self.xml_file_small_split_003))

        # Cleanup files when done
        os.remove(self.xml_file_small_split_001)
        os.remove(self.xml_file_small_split_002)
        os.remove(self.xml_file_small_split_003)

    def test_small_two_split_positive(self):
        xml_split(self.xml_file_small_path, 'OrderAudit', 2)

        self.assertTrue(os.path.isfile(self.xml_file_small_split_000))
        self.assertTrue(os.path.isfile(self.xml_file_small_split_001))

        # Cleanup files when done
        os.remove(self.xml_file_small_split_000)
        os.remove(self.xml_file_small_split_001)

