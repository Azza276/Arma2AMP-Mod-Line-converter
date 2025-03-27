def generate_mod_line(file_path):
    return extract_mod_lines(file_path, '?id=', '"', '\n')

def extract_mod_lines(file_path, start_marker, end_marker, line_suffix):
    newlist = ''
    with open(file_path) as f:
        for line in f:
            if start_marker in line:
                start_index = line.find(start_marker) + len(start_marker)
                end_index = line.find(end_marker, start_index)
                if end_index != -1:
                    mod_id = line[start_index:end_index]
                    newlist += mod_id + line_suffix
    return newlist