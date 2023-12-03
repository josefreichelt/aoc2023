def read_file_as_list(filename):
    with open(filename) as f:
        content = f.readlines()
    content = filter(None,[x.strip() for x in content])
    return list(content)
