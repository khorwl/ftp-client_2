from commands.command import ICommand
from constants import end_msg
from tools.helper import parse_from_response_to_ip_and_port, \
    send_pasv, open_connection_at, download_all_from
from tools.response_reader import read_response


class Ls(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        response_addr = send_pasv(self.conn, self.encoding)

        if response_addr[0][0] != "2":
            print(response_addr)
            return

        ip_and_port = parse_from_response_to_ip_and_port(response_addr)

        self.conn.sendall(('list' + end_msg).encode(self.encoding))

        with open_connection_at(ip_and_port) as data_connection:
            response = read_response(self.conn, self.encoding, self.change_some_code)

            print(response)

            if response[0] != "1":
                print(response)
                return

            print(download_all_from(data_connection, None).decode(self.encoding))

        print(read_response(self.conn, self.encoding, self.change_some_code))
