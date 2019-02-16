import re
import socket

from constants import end_msg
from tools.get_progress_bar import get_progress_bar
from tools.response_reader import read_response
from tools.timer import Timer


def from_string_to_command_and_args(string):
    if not isinstance(string, str):
        return None
    return string.split()


def send_pasv(s, encoding):
    s.sendall(("pasv" + end_msg).encode(encoding))
    return read_response(s, encoding, False)


def write_bytes_to_file(filename, bytes_):
    with open(filename, 'wb') as file:
        file.write(bytes_)


def open_connection_at(address):
    s = socket.socket()
    s.connect(address)

    return s


def parse_from_response_to_ip_and_port(addr):
    address_regexp_4 = re.compile("\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3}", re.M)
    result = address_regexp_4.search(addr)

    if result is not None:
        tokens = result.group(0).split(',')

        return '.'.join(tokens[0:4]), int(tokens[4]) * 256 + int(tokens[5])

    return None


def compute_download_percentage(file_size, download_size):
    if file_size == 0:
        return None

    return (download_size / file_size) * 100


def download_all_from(conn, file_size):
    data = bytearray()

    timer = Timer()
    while True:
        part = conn.recv(1024 * 16)  # 16KB
        if len(part) == 0:
            break

        data.extend(part)

        if file_size is None:
            print('\r' + str(len(data) / timer.elapsed / 1024) + " KB/s", end='')
        else:
            progress_bar = get_progress_bar(compute_download_percentage(file_size, len(data)))
            if progress_bar is None:
                continue
            print('\r' + progress_bar + ' ' + str(len(data) / timer.elapsed / 1024) + " KB/s", end='')

    print('', end="\n\n")

    return bytes(data)


def send_all_by(conn, file_name):
    conn.send(open(file_name, "rb").read())


def send_command(conn, string, encoding, change_some_code):
    if change_some_code:
        conn.sendall(string.encode("cp1251").replace(b"\xff", b"\xff\xff"))

    else:
        conn.sendall(string.encode(encoding))
