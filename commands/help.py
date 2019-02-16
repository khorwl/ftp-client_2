from commands.command import ICommand


class Help(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        print("""
сd       <filename>  - Переход в каталог filename или на папку выше(..).
delete   <filename>  - Удаление файла filename.
download <filename>  - Скачивание файла с именем filename.
login                - Регистрация пользователя с указанием пароля. 
ls                   - Возврат списка файлов каталога.
mkdir    <dir_name>  - Cоздание каталога directory_name.
help                 - Вывод списка команд, принимаемых сервером.
pwd                  - Возврат текущего каталога.
quit                 - Отключение соединения.
upload  <file_name>  - Отправляет file_name на сервер.
""")
