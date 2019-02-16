from getpass import getpass

from commands.command import ICommand
from constants import end_msg
from tools.helper import send_command
from tools.response_reader import read_response


class Login(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        print("user:")
        user_name = input()
        send_command(self.conn, "user {}".format(user_name) + end_msg, self.encoding, self.change_some_code)
        response = read_response(self.conn, self.encoding, self.change_some_code)

        if response[0] != "3":
            print(response)
            return

        password = getpass("Enter your password:")
        send_command(self.conn, "pass {}".format(password) + end_msg, self.encoding, self.change_some_code)
        print(read_response(self.conn, self.encoding, self.change_some_code))
