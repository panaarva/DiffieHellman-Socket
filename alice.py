import socket
import json
import random
from sympy import *

HOST = "127.0.0.1"
PORT = 12345


def random_prime_number():
    primes_numbers = [i for i in range(0,1000) if isprime(i)]
    return random.choice(primes_numbers)


def check_num(arr):
    out = []
    for i in arr:
        if i not in out:
            out.append(i)
        else:
            return False
    out.clear()
    return True


def primitive_root_module_prime_number(n):
    arr = []
    roots = []
    for i in range(1, n):
        for j in range(1, n):
            t = (pow(i, j)) % n
            arr.append(t)
        if check_num(arr):
            roots.append(i)
            break
        arr.clear()
    return roots[0]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        connection, address = s.accept()

        with connection:
            print("====== Diffie Hellman Algorithm Started ======\n")
            print("[Alice] Connected with bob by ", address)
            # random prime number
            p = 23  # random_prime_number()
            g = 5  # primitive_root_module_prime_number(p)
            a = 4  # random.randint(0, 1000)
            A = pow(g, a) % p
            print("[Alice] Choice private number: " + str(a))
            print("[Alice] Choice prime number: " + str(p))
            print("[Alice] Choice primitive root module p: " + str(g))
            print("[Alice] Calculate A = g^a mod p => A = " + str(A))
            info_send_bob = str({"p": p, "g": g, "A": A})
            print("[Alice] Alice send to bob P=" + str(p) + " G=" + str(g) + " A=" + str(A))
            connection.sendall(str.encode(info_send_bob))
            bob_info_recv = connection.recv(2048)
            bob_info = json.loads(bob_info_recv.decode('utf-8').replace("\'", "\""))
            B = bob_info["B"]
            print("[Alice] Alice receive from Bob " + str(bob_info))
            private_key = pow(B, a) % p
            print("[Alice] Calculate private_key = B^a mod p => private_key = " + str(private_key))
            print("\n====== Diffie Hellman Algorithm Finished ======\n")
