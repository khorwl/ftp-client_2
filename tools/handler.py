from commands.cd import Cd
from commands.delete import Delete
from commands.download import Download
from commands.help import Help
from commands.login import Login
from commands.ls import Ls
from commands.mkdir import Mkdir
from commands.pwd import PWD
from commands.quit import Quit
from commands.upload import Upload
from tools.helper import from_string_to_command_and_args


class Handler:

    def __init__(self, s, encoding, change_ff_code):
        self.s = s
        self.flag = change_ff_code
        self.encoding = encoding
        self.name_to_command = {"cd": Cd(self.s, encoding, self.flag), "delete": Delete(self.s, encoding, self.flag),
                                "download": Download(self.s, encoding, self.flag), "help": Help(self.s, encoding, self.flag),
                                "login": Login(self.s, encoding, self.flag), "ls": Ls(self.s, encoding, self.flag),
                                "mkdir": Mkdir(self.s, encoding, self.flag), "pwd": PWD(self.s, encoding, self.flag),
                                "quit": Quit(self.s, encoding, self.flag), "?": Help(self.s, encoding, self.flag),
                                "upload": Upload(self.s, encoding, self.flag)}

    def execute_command_by_string(self, str):

        comm_and_args = from_string_to_command_and_args(str)
        command_name = comm_and_args[0].lower()

        if command_name in self.name_to_command:
            command = self.name_to_command[command_name]

            if len(comm_and_args) > 1:
                command.execute_command(comm_and_args[1:])
            else:
                command.execute_command(None)
        else:
            print("unknown command", end="\n\n")
