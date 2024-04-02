"""import requests
query={'message':'sucess', "people":'1'}
response=requests.get("http://api.open-notify.org/astros.json",params=query)
print(response.json())
"""
"""
import socket

# Define the target server and port
host = '8.8.8.8'
port = 80

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysock.connect((host, port))

# Define the path of the page you want to fetch
path = 'https://www.engabaswarsame.com/'

# Send an HTTP GET request
cmd = f'GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and print the response
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()"""
import requests 
city=input("enter your city ")
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=59e7d034f534e6ac722cc8a96d02d1fa'
res=requests.get(url)
data=res.json()
print(data)
if res.status_code==200:
    temp=data['main']['temp']
    print("tempreture",temp)
    humidity=data['main']['humidity']
    print("tempreture",humidity)