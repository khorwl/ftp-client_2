import socket

from commands.command import ICommand
from commands.size import Size
from constants import end_msg
from tools.get_ip import get_ip
from tools.helper import parse_from_response_to_ip_and_port, send_pasv, open_connection_at, \
    write_bytes_to_file, download_all_from, send_command
from tools.response_reader import read_response


class Download(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)
        self.size_command = Size(s, self.encoding, self.change_some_code)

    def execute_command(self, args):
        file_name = " ".join(args)

        file_size = self.size_command.execute_command(file_name)

        if file_size is None:
            return

        mode = input("Which mode use? (active, passive)")

        if mode == 'passive':
            print('Executing at passive mode')
            ip_and_port = parse_from_response_to_ip_and_port(send_pasv(self.conn, self.encoding))

            send_command(self.conn, "retr {}".format(file_name) + end_msg, self.encoding, self.change_some_code)

            with open_connection_at(ip_and_port) as data_connection:
                response = read_response(self.conn, self.encoding, self.change_some_code)

                if response[0] != "1":
                    print(response)
                    return

                write_bytes_to_file(file_name, download_all_from(data_connection, int(file_size)))

            print(read_response(self.conn, self.encoding, self.change_some_code))
        else:
            print('Executing at active mode')

            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(("0.0.0.0", 0))
            ip = get_ip()
            port = int(server_socket.getsockname()[1]).to_bytes(2, byteorder='big')

            send_command(self.conn, f"port {ip[0]},{ip[1]},{ip[2]},{ip[3]},{port[0]},{port[1]}", self.encoding, self.change_some_code)
            response = read_response(self.conn, self.encoding, self.change_some_code)

            if response[0] != '1':
                print(response)
                return

            server_socket.listen(1)

            con, addr = server_socket.accept()

            write_bytes_to_file(file_name, download_all_from(con, int(file_size)))
