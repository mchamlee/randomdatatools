def flat_dict(the_dict):
    for key in the_dict:
        if isinstance(the_dict[key], dict):
            yield from flat_dict(the_dict[key])
        else:
            yield the_dict[key]


def list_replace(the_list, replace_what, replace_with):
    """Replaces char with char for all values in a list. If a dict is found as a value within
    the set pass to dict_replace to replace all keys and values [a].

    Args:
        the_list: The list on which to perform the replacement.
        replace_what: The char to replace
        replace_with: What to replace 'what' with.

    Returns:
        A list with the values replaced.
    """
    new_list = []
    for i in the_list:
        if isinstance(i, list):
            new_list.append(list_replace(i, replace_what, replace_with))
        elif isinstance(i, dict):
            new_list.append(dict_replace(i, replace_what, replace_with, 'a'))
        elif isinstance(i, str):
            new_list.append(i.replace(replace_what, replace_with))
        else:
            new_list.append(i)

    return new_list


# TODO: Refactor to class?
def dict_replace(the_dict, replace_what, replace_with, where_to_replace='a'):
    """Replaces char with char for keys, values, or both in a dictionary.

    Args:
        the_dict: The dictionary on which to perform the replacement.
        replace_what: The char to replace.
        replace_with: What to replace the 'what' with.
        where_to_replace: Replace on keys [k], values [v], or all [a]. Default to all [a].

    Returns:
        A dictionary with the values replaced.
    """
    def handle_replace(the_value, key_or_value, **kwargs):
        if isinstance(the_value, str):
            if kwargs['where_to_replace'] in [key_or_value, 'a']:
                return the_value.replace(kwargs['replace_what'], kwargs['replace_with'])
        return the_value

    replace_args = {
        'replace_what': replace_what,
        'replace_with': replace_with,
        'where_to_replace': where_to_replace
    }

    new_dict = {}

    for key in the_dict:
        if isinstance(the_dict[key], dict):
            new_dict[handle_replace(key, 'k', **replace_args)] = dict_replace(the_dict[key], replace_what, replace_with,
                                                                              where_to_replace)
        elif isinstance(the_dict[key], list):
            if where_to_replace in ('v', 'a'):
                new_dict[handle_replace(key, 'k', **replace_args)] = list_replace(the_dict[key], replace_what, replace_with)
            else:
                new_dict[handle_replace(key, 'k', **replace_args)] = the_dict[key]
        elif isinstance(the_dict[key], (set, tuple)):
            raise ValueError("Does not handle set or tuple.")
        else:
            new_dict[handle_replace(key, 'k', **replace_args)] = \
                handle_replace(the_dict[key], 'v', **replace_args)

    return new_dict
