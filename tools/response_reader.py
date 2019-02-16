from constants import end_msg


def is_code(code):
    try:
        code = int(code)
        return 99 < code < 600
    except ValueError:
        return False


def is_end_response(line):
    if len(line) < 4:
        return False
    return line[3] == ' ' and is_code(line[:3])


def read_line(reader, encoding, change_ff_code):
    line = ''
    while not line.endswith(end_msg):
        if change_ff_code:
            line += reader.recv(1).replace(b"\xff\xff", b"\xff").decode("cp1251")
        else:
            line += reader.recv(1).decode(encoding)

    return line


def read_response(reader, encoding, change_ff_code):
    response = ''
    last_line = read_line(reader, encoding, change_ff_code)
    response += last_line

    while not (is_end_response(last_line)):
        last_line = read_line(reader, encoding, change_ff_code)
        response += last_line

    return response
