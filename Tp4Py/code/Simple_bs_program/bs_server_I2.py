import socket

host = ""
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

conn , addr = s.accept()

print('Un client vient de se co et son IP c\'est', addr, ".")

while True:
    
    try:
        data = conn.recv(1024)
        if not data: break
        if "meo" in data.decode() : conn.send("Meo à toi confrère.".encode())
        elif "waf" in data.decode() : conn.send("ptdr t ki".encode())
        elif not "waf" in data.decode() or not "meo" in data.decode : conn.send("Mes respects humble humain.".encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()