import sys
import ipaddress
import keyboard
import socket
import os
from os import system,name
from colorama import init
from colorama import Fore, Back,Style
import platform
import subprocess


init(autoreset=True)


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


if __name__ == "__main__":
    clear_screen()

print(Fore.GREEN + "Pingovator v.1.1 от 13.03.2023\n")


def testlink():
    number = 1
    while number >0 and number <7:



        print("Проверка доступности портов:")
        print(
            "1. Сбербанк \n2. Банк Открытие \n3. Платформа ОФД \n4. Сертификаты Ingenico\n5. Ввести свои данные\n6. Выход")
        print()
        number = int(input("Выберите значение:"))
        clear_screen()


        if number == 1:
            print()
            print("Проверка начата. Дождитесь завершения...")
            print()
            print("Основной")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 670))
            port = ("IP 194.54.14.89, port 670 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 700))
            port = ("IP 194.54.14.89, port 700 (Транзакции + сверка итогов)")

            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 740))
            port = ("IP 194.54.14.89, port 740 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 666))
            port = ("IP 194.54.14.89, port 666 (Удаленная загрузка)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 650))
            port = ("IP 194.54.14.89, port 650 (Мониторинг)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.89', 690))
            port = ("IP 194.54.14.89, port 690 (Отправка логов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Резервный")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 670))
            port = ("IP 194.54.15.25, port 670 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 700))
            port = ("IP 194.54.15.25, port 700 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 740))
            port = ("IP 194.54.15.25, port 740 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 666))
            port = ("IP 194.54.15.25, port 666 (Удаленная загрузка)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 650))
            port = ("IP 194.54.15.25, port 650 (Мониторинг)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.25', 690))
            port = ("IP 194.54.15.25, port 690 (Отправка логов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Резервный")

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 670))
            port = ("IP 194.54.14.162, port 670 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 700))
            port = ("IP 194.54.14.162, port 700 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 740))
            port = ("IP 194.54.14.162, port 740 (Транзакции + сверка итогов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 666))
            port = ("IP 194.54.14.162, port 666 (Удаленная загрузка)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 650))
            port = ("IP 194.54.14.162, port 650 (Мониторинг)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.162', 690))
            port = ("IP 194.54.14.162, port 690 (Отправка логов)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Тестовый")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.24', 668))
            port = ("IP 194.54.14.24, port 668 (Транзакции)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.24', 666))
            port = ("IP 194.54.14.24, port 666 (Удаленная загрузка)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.14.24', 650))
            port = ("IP 194.54.14.24, port 650 (Мониторинг)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("UPOS 2.0")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('185.157.96.41', 80))
            port = ("IP 185.157.96.41, port 80 (Основной)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('194.54.15.98', 80))
            port = ("IP 194.54.15.98, port 80 (Основной)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('185.157.96.24', 80))
            port = ("IP 185.157.96.24, port 80 (Основной)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()
            print()
            print("Проверка завершена.\n")

            #keyboard.read_key()

        if number == 2:
            print()
            print("Проверка начата. Дождитесь завершения...")
            print()
            print("Сервера TMS ЕКП")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.148', 8001))
            port = ("IP 91.197.176.148, port 8001 (Verifone/Pax)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.148', 8002))
            port = ("IP 91.197.176.148, port 8002 (Ingenico)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #result = sock.connect_ex(('91.197.176.108', 8003))
            #port = ("IP 91.197.176.108, port 8003 (NEXGO)")
            #if result == 0:
            #    print(Fore.GREEN + "Открыт:", port)
            #else:
            #    print(Fore.RED + "Закрыт:", port)
            #sock.close()
            print()

            print("Процессинг (Загрузка ключей, транзакции)")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.117', 443))
            port = ("IP 91.197.176.117, port 443 (БО - TID на 2,4. Единый на все терминалы)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.109', 443))
            port = ("IP 91.197.176.109, port 443 (ББ - TID на Y,W. Verifone, Pax)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.110', 443))
            port = ("IP 91.197.176.110, port 443 (ББ - TID на Y,W. Ingenico)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.197.176.111', 443))
            port = ("IP 91.197.176.111, port 443 (ББ - TID на Y,W. NEXGO)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Проверка завершена.\n")
            print()
            #keyboard.read_key()

        if number == 3:
            print()
            print("Проверка начата. Дождитесь завершения...\n")
            print("Хосты платформы ОФД")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('185.170.204.91', 21101))
            port = ("IP 185.170.204.91, port 21101 (Данные для регистрации ККТ и отправки чеков)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('185.170.204.91', 21102))
            port = ("IP 185.170.204.91, port 21102 (Данные для работы ИСМ по маркировке (по ФФД 1.2)")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Проверка завершена.\n")

            #keyboard.read_key()

        if number == 4:

            print()
            print("Проверка начата. Дождитесь завершения...\n")
            print("Сертификаты Ingenico")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('91.208.214.91', 12050))
            port = ("IP 91.208.214.91, port 12050")
            if result == 0:
                print(Fore.GREEN + "Открыт:", port)
            else:
                print(Fore.RED + "Закрыт:", port)
            sock.close()

            print()
            print("Проверка завершена.\n")
            print()
            #keyboard.read_key()


        if number == 5:
            if __name__ == "__main__":

                sock = socket.socket()
                try:

                    server_ip = input("Введите IP-адрес сервера (например, 192.168.0.3): ")
                    Ipport = int(input("Введите IP порт:"))
                    port = (server_ip, Ipport)
                    print()
                    print("Проверка начата. Дождитесь завершения...\n")
                    sock.connect((server_ip, Ipport))
                    print(Fore.GREEN + "Открыт:", port)

                except Exception as err:
                    print(Fore.RED + "Закрыт:", port)
                finally:
                    sock.close()
            print()
            print("Проверка завершена.\n")


            #print()
            #Ipadr = ipaddress.ip_address(input("Введите IP адрес:"))
            #Ipport = int(input("Введите IP порт:"))
            #print(Ipadr, Ipport)
            #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #result = sock.connect_ex(('91.208.214.91', Ipport))
            #port = (Ipadr, Ipport)
            #if result == 0:
                #print(Fore.GREEN + "Открыт:", port)
            #else:
                #print(Fore.RED + "Закрыт:", port)
            #sock.close()
            #print()
            #print("Проверка завершена.\nДля продолжения нажмите любую клавишу...")
            #print()
            #keyboard.read_key()

        if number == 6:
            sys.exit()

        #else:
    if number < 1 or number > 6:
        print(Fore.RED +"\nНе подходит условиям выбора\n")
        testlink()

testlink()



