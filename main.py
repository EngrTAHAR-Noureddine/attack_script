import os
import sys
import time
# import appscript


def run_forum_linux(url, main_path, file_path):
    command = 'cd ' + main_path + ' && python3 ' + file_path + " " + url #
    # appscript.app('Terminal').do_script(command)
    os.system("gnome-terminal --window -- bash -c '" + command + "; exec bash'")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_path = os.path.dirname(os.path.abspath(__file__))
    i = 0
    if len(sys.argv) > 0:
        base_url_get_password = sys.argv[1]
        base_url_add_users = sys.argv[2]
        while i < 10:
            try:
                run_forum_linux(base_url_get_password, main_path, 'send_passwords.py')
                run_forum_linux(base_url_add_users, main_path, 'add_users.py')
            except Exception as error:
                print("error : ", error)
                pass
            i = i + 1
            # time.sleep(500)
