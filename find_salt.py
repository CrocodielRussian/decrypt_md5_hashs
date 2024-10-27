import pandas as pd
import subprocess


def decrypt_hashs():
    input_file = input("Введите название файла с хешами: ").strip() or "hashs.txt"
    output_file = input("Введите название файла с расшифровываными хешами: ").strip() or "output.txt"

    command = ['hashcat', '-m', '0', '-a', '3', input_file, 'mask.hcmask', '-o', output_file]
    subprocess.call(command)

    dc = {}
    with open(output_file, "r") as fl:
        for line in fl:
            f = line.split(":")
            dc.update({f[0] : int(f[1].replace("\n", ""))})
    nums = list(dc.values())

    num = []
    with open("tel.txt", "r") as fl:
        for tel in fl:
            num.append(int(tel))


    f = [[] for _ in range(len(num))]
    for i in range(len(num)):
        for num1 in nums:
            f[i].append(num1 - num[i])

    all_f = set(f[0])
    for i in range(1, len(f)):
        all_f = all_f.intersection(set(f[i]))
    check = [False for _ in range(len(num))]

    sl = 0
    for salt in all_f:
        for i in range(0, len(nums)):
            if (nums[i] - salt) in num:
                check[num.index(nums[i] - salt)] = True
            if all(check):
                print(f"true {salt}")
                sl = salt
                break
        if(sl != 0):
            break

    with open("crack.txt", "w") as fl:
        for i in range(0, len(nums)):
            fl.write(f"{nums[i] - sl}\n")
decrypt_hashs()