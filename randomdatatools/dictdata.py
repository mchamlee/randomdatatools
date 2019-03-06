def flat_dict(the_dict):
    for key in the_dict:
        if isinstance(the_dict[key], dict):
            yield from flat_dict(the_dict[key])
        else:
            yield the_dict[key]


# TODO: Cleanup dict_replace2, perhaps convert to class.
def dict_replace(the_dict, replace_what, replace_with, where_to_replace='a'):
    """Replaces char with char for keys, values, or both in a dictionary.

    Args:
        the_dict: The dictionary on which to perform the replacement.
        replace_what: The char to replace.
        replace_with: What to replace the 'what' with.
        where_to_replace: Replace on keys [k], values [v], or all [a]

    Returns:
        The dictionary with the values replaced.
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
            new_dict[handle_replace(key, 'k', **replace_args)] = dict_replace(the_dict[key], replace_what, replace_with, where_to_replace)
        else:
            new_dict[handle_replace(key, 'k', **replace_args)] = \
                handle_replace(the_dict[key], 'v', **replace_args)

    return new_dict
