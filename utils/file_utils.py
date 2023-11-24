def get_size(size):
    units = ['Bytes', 'KB', 'MB', 'GB']
    for i in range(len(units)):
        if size < 1024:
            size_str = '%.f' % size + units[i]
            return size_str
        size = size / 1024
