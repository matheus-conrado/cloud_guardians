
def remove_keys_and_values(the_dict, entries=0):
    if entries == 0:
        return the_dict
    else:
        for key in entries:
            if key in the_dict:
                del the_dict[key]
        return the_dict