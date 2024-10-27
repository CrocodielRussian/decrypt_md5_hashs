import hashlib
import random
import string

telephones = []

def generate_salt(lenght = 3):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(lenght))
def crypt_hashs(salt, hash_func):
    with open("crack.txt", "r") as fl:
        for line in fl:
            telephones.append(line.replace("\n", ""))
    with open(f"{hash_func}.txt", "a") as fl:
        for i in range(len(telephones)):
            
            if hash_func == "sha256":
                m = hashlib.sha256()
            elif hash_func == "md5":
                m = hashlib.md5()
            elif hash_func == "sha1":
                m = hashlib.sha1()
            elif "sha512":
                m = hashlib.sha512()
            elif "sha384":
                m = hashlib.sha384()
            s_concat = telephones[i]+salt
            # print(s_concat)
            m.update(s_concat.encode())
            # print(m.hexdigest())
            if(hash_func != "blake2b"):
                fl.write(f"{m.hexdigest()}\n")
            else:
                fl.write(f"$BLAKE2${m.hexdigest()}\n")
if __name__ == "__main__":
    hash_func = input("Какую хеш-функцию вы хотите использовать для шифрования: ").strip() or "sha256"
    salt = generate_salt()
    crypt_hashs(salt, hash_func)