from django.shortcuts import render
import random
from django.http import JsonResponse
from django.http import HttpResponse
from time import sleep
import socket

# Create your views here.
# Адрес IPv4:
def index(request):
    return render(request, 'main/index.html')

def index2(request):
    return render(request, 'main/index2.html')

def index3(request):
    return render(request, 'main/index3.html')

def index4(request):
    return render(request, 'main/index4.html')

def index5(request):
    return render(request, 'main/index5.html')

def index6(request):
    return render(request, 'main/index6.html')

def index7(request):
    return render(request, 'main/index7.html')

def get(request):
    host = (172, 20, 10, 4)  # IP-адрес вашего сервера
    port = 8081  # Порт для прослушивания входящих соединений
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('172.20.10.4', port))
    server_socket.listen(5)
    print('Listening on port', port)
    while True:
        client_socket, addr = server_socket.accept()
        received_data1 = client_socket.recv(1024).decode('utf-8')
        received_data2 = client_socket.recv(1024).decode('utf-8')
        received_data3 = client_socket.recv(1024).decode('utf-8')
        received_data4 = client_socket.recv(1024).decode('utf-8')
        print('Received data1:', received_data1)
        print('Received data2:', received_data2)
        print('Received data3:', received_data3)
        print('Received data4:', received_data4)
        data = {"num1" : received_data1,  "num2" : received_data2, "num3" : received_data3,  "num4" : received_data4}
        # Дальнейшая обработка полученных данных, например, сохранение в базу данных
        # Первое значение - это скорость передвижения, второе значение - это режим работы от компа либо от телефона
        client_socket.close()
        return JsonResponse(data)
def post1(request):
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.20.10.4', 8585))
    s.listen(0)

    while True:
        client, addr = s.accept()
        client.settimeout(5)
        while True:
            content = client.recv(1024)
            if len(content) == 0:
                break
            if str(content, 'utf-8') == '\r\n':
                continue
            else:
                print(str(content, 'utf-8'))
                if str(content, 'utf-8') == "on":
                    client.send(b'vp')
                time.sleep(1)
            return render(request, "main/index5.html")
            time.sleep(1)

        client.close()

def post2(request):
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.20.10.4', 8585))
    s.listen(0)

    while True:
        client, addr = s.accept()
        client.settimeout(5)
        while True:
            content = client.recv(1024)
            if len(content) == 0:
                break
            if str(content, 'utf-8') == '\r\n':
                continue
            else:
                print(str(content, 'utf-8'))
                if str(content, 'utf-8') == "on":
                    client.send(b'prav')
                time.sleep(1)
            time.sleep(1)
            return render(request, "main/index5.html")


        client.close()


def post3(request):
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.20.10.4', 8585))
    s.listen(0)

    while True:
        client, addr = s.accept()
        client.settimeout(5)
        while True:
            content = client.recv(1024)
            if len(content) == 0:
                break
            if str(content, 'utf-8') == '\r\n':
                continue
            else:
                print(str(content, 'utf-8'))
                if str(content, 'utf-8') == "on":
                    client.send(b'lev')
                time.sleep(1)
            time.sleep(1)
            return render(request, "main/index5.html")

        client.close()

def post4(request):
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.20.10.4', 8585))
    s.listen(0)

    while True:
        client, addr = s.accept()
        client.settimeout(5)
        while True:
            content = client.recv(1024)
            if len(content) == 0:
                break
            if str(content, 'utf-8') == '\r\n':
                continue
            else:
                print(str(content, 'utf-8'))
                if str(content, 'utf-8') == "on":
                    client.send(b'naz')
                time.sleep(1)
            time.sleep(1)
            return render(request, "main/index5.html")


        client.close()
