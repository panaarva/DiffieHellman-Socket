import socket
import random
import json

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    alice_info_recv = s.recv(2048)
    alice_info = json.loads(alice_info_recv.decode('utf-8').replace("\'", "\""))
    print("[Bob] Bod receive from alice " + str(alice_info))
    g = alice_info["g"]
    p = alice_info["p"]
    A = alice_info["A"]
    b = 3  # random.randint(0, 1000)
    B = pow(g, b) % p
    print("[Bob] Choice private number " + str(b))
    print("[Bob] Calculate B = g^b mod p => B = " + str(B))
    info_send_alice = str({"B": B})
    print("[Bob] Bob send to Alice B = " + str(B))
    s.sendall(str.encode(info_send_alice))
    private_key = pow(A, b) % p
    print("[Bob] Calculate private_key = A^b mod p => private_key = " + str(private_key))
