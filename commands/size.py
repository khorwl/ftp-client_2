from commands.command import ICommand
from constants import end_msg
from tools.helper import send_command
from tools.response_reader import read_response


class Size(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, file_name):
        send_command(self.conn, "size {}".format(file_name) + end_msg, self.encoding, self.change_some_code)

        size = self.get_file_size()

        return size

    def get_file_size(self):
        response = read_response(self.conn, self.encoding, self.change_some_code)[:-2].split()

        if response[0][0] == "2":
            return response[1]
        else:
            print(" ".join(response), end="\n\n")
            return None
