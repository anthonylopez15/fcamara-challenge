def convert_to_dict(data):
    output = []
    if data:
        for item in data:
            ordered_dict = item._asdict()
            obj = dict(ordered_dict)
            output.append(obj)
    return output
