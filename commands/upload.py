from commands.command import ICommand
from constants import end_msg
from tools.helper import parse_from_response_to_ip_and_port, send_pasv, open_connection_at, send_all_by, send_command
from tools.response_reader import read_response


class Upload(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        file_name = " ".join(args)
        ip_and_port = parse_from_response_to_ip_and_port(send_pasv(self.conn, self.encoding))

        send_command(self.conn, "stor " + file_name + end_msg, self.encoding, self.change_some_code)

        with open_connection_at(ip_and_port) as data_connection:
            response = read_response(self.conn, self.encoding, self.change_some_code)

            if response[0] != "1":
                print(response)
                return

            send_all_by(data_connection, file_name)

        print(read_response(self.conn, self.encoding, self.change_some_code))
