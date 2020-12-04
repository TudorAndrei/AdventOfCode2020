

def read_file(path, lines=True):
    with open(path) as f:
        if lines:
            return [line.rstrip('\n') for line in f]
        else:
            return list(f)
