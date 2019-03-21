import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from randomdatatools.dictdata import *


class TestDictReplace(unittest.TestCase):
    test_dict = {
        'numeric-element1': 1,
        'numeric-element2': 2,
        'alpha-element1': {
            'alpha-sub-element1': 'ab-cd',
            'numeric-sub-element1': 3
        },
        'alpha-element2': 'ef-gh',
        'alpha-element3': {
            'numeric-sub-element2': 4,
            'alpha-sub-element2': {
                'numeric-sub-sub-element1': 5,
                'alpha-sub-sub-element1': 'ij-kl',
                'alpha-sub-sub-element2': 'mn-op'
            }
        }}

    test_dict_list = {
        'numeric-element1': 1,
        'numeric-element2': 2,
        'alpha-element1': {
            'alpha-sub-element1': ['ab-cd', 'qr-st-uv', 'wxy-z'],
            'numeric-sub-element1': 3
        },
        'alpha-element2': 'ef-gh',
        'alpha-element3': {
            'numeric-sub-element2': 4,
            'alpha-sub-element2': {
                'numeric-sub-sub-element1': 5,
                'alpha-sub-sub-element1': 'ij-kl',
                'alpha-sub-sub-element2': 'mn-op'
            }
        }}

    result_dict_replace_with_underscores_all = {
        'numeric_element1': 1,
        'numeric_element2': 2,
        'alpha_element1': {
            'alpha_sub_element1': 'ab_cd',
            'numeric_sub_element1': 3
        },
        'alpha_element2': 'ef_gh',
        'alpha_element3': {
            'numeric_sub_element2': 4,
            'alpha_sub_element2': {
                'numeric_sub_sub_element1': 5,
                'alpha_sub_sub_element1': 'ij_kl',
                'alpha_sub_sub_element2': 'mn_op'
            }
        }}

    result_dict_replace_with_underscores_keys = {
        'numeric_element1': 1,
        'numeric_element2': 2,
        'alpha_element1': {
            'alpha_sub_element1': 'ab-cd',
            'numeric_sub_element1': 3
        },
        'alpha_element2': 'ef-gh',
        'alpha_element3': {
            'numeric_sub_element2': 4,
            'alpha_sub_element2': {
                'numeric_sub_sub_element1': 5,
                'alpha_sub_sub_element1': 'ij-kl',
                'alpha_sub_sub_element2': 'mn-op'
            }
        }}

    result_dict_replace_with_underscores_values = {
        'numeric-element1': 1,
        'numeric-element2': 2,
        'alpha-element1': {
            'alpha-sub-element1': 'ab_cd',
            'numeric-sub-element1': 3
        },
        'alpha-element2': 'ef_gh',
        'alpha-element3': {
            'numeric-sub-element2': 4,
            'alpha-sub-element2': {
                'numeric-sub-sub-element1': 5,
                'alpha-sub-sub-element1': 'ij_kl',
                'alpha-sub-sub-element2': 'mn_op'
            }
        }}

    result_dict_replace_numeric_with_number_all = {
        'number-element1': 1,
        'number-element2': 2,
        'alpha-element1': {
            'alpha-sub-element1': 'ab-cd',
            'number-sub-element1': 3
        },
        'alpha-element2': 'ef-gh',
        'alpha-element3': {
            'number-sub-element2': 4,
            'alpha-sub-element2': {
                'number-sub-sub-element1': 5,
                'alpha-sub-sub-element1': 'ij-kl',
                'alpha-sub-sub-element2': 'mn-op'
            }
        }}

    result_dict_list_replace_hyphen_with_underscore_values = {
        'numeric-element1': 1,
        'numeric-element2': 2,
        'alpha-element1': {
            'alpha-sub-element1': ['ab_cd', 'qr_st_uv', 'wxy_z'],
            'numeric-sub-element1': 3
        },
        'alpha-element2': 'ef_gh',
        'alpha-element3': {
            'numeric-sub-element2': 4,
            'alpha-sub-element2': {
                'numeric-sub-sub-element1': 5,
                'alpha-sub-sub-element1': 'ij_kl',
                'alpha-sub-sub-element2': 'mn_op'
            }
        }}

    result_dict_list_replace_hyphen_with_underscore_all = {
        'numeric_element1': 1,
        'numeric_element2': 2,
        'alpha_element1': {
            'alpha_sub_element1': ['ab_cd', 'qr_st_uv', 'wxy_z'],
            'numeric_sub_element1': 3
        },
        'alpha_element2': 'ef_gh',
        'alpha_element3': {
            'numeric_sub_element2': 4,
            'alpha_sub_element2': {
                'numeric_sub_sub_element1': 5,
                'alpha_sub_sub_element1': 'ij_kl',
                'alpha_sub_sub_element2': 'mn_op'
            }
        }}

    def test_replace_all_dash_underscore_positive(self):
        self.assertEqual(dict_replace(self.test_dict, '-', '_'),
                         self.result_dict_replace_with_underscores_all)

    def test_replace_keys_dash_underscore_positive(self):
        self.assertEqual(dict_replace(self.test_dict, '-', '_', 'k'),
                         self.result_dict_replace_with_underscores_keys)

    def test_replace_values_dash_underscore_positive(self):
        self.assertEqual(dict_replace(self.test_dict, '-', '_', 'v'),
                         self.result_dict_replace_with_underscores_values)

    def test_replace_all_numeric_number_positive(self):
        self.assertEqual(dict_replace(self.test_dict, 'numeric', 'number'),
                         self.result_dict_replace_numeric_with_number_all)

    def test_replace_values_hyphen_underscore_with_list_positive(self):
        self.assertEqual(dict_replace(self.test_dict_list, '-', '_', 'v'),
                         self.result_dict_list_replace_hyphen_with_underscore_values)

    def test_replace_all_hyphen_underscore_with_list_positive(self):
        self.assertEqual(dict_replace(self.test_dict_list, '-', '_'),
                         self.result_dict_list_replace_hyphen_with_underscore_all)
