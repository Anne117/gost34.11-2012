linealCoef = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
prime_polynome = [1, 1, 1, 0, 0, 0, 0, 1, 1]
nonlinear_coef = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240,
                  219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92,
                  239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11,
                  237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253,
                  58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21,
                  161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25,
                  61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168,
                  67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188,
                  220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130,
                  100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149,
                  59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27,
                  131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45,
                  43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230, 244, 180, 192,
                  209, 102, 175, 194, 57, 75, 99, 182]
tRearrangement = [0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19,
                  27, 35, 43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38,
                  46, 54, 62, 7, 15, 23, 31, 39, 47, 55, 63]
Crearrangent = [
    'b1085bda1ecadae9ebcb2f81c0657c1f2f6a76432e45d016714eb88d7585c4fc4b7ce09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507',
    '6fa3b58aa99d2f1a4fe39d460f70b5d7f3feea720a232b9861d55e0f16b501319ab5176b12d699585cb561c2db0aa7ca55dda21bd7cbcd56e679047021b19bb7',
    'f574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea7514b1297b7bd3e20fe490359eb1c1c93a376062db09c2b6f443867adb31991e96f50aba0ab2',
    'ef1fdfb3e81566d2f948e1a05d71e4dd488e857e335c3c7d9d721cad685e353fa9d72c82ed03d675d8b71333935203be3453eaa193e837f1220cbebc84e3d12e',
    '4bea6bacad4747999a3f410c6ca923637f151c1f1686104a359e35d7800fffbdbfcd1747253af5a3dfff00b723271a167a56a27ea9ea63f5601758fd7c6cfe57',
    'ae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e',
    'f4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c90992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493',
    '9b1f5b424d93c9a703e7aa020c6e41414eb7f8719c36de1e89b4443b4ddbc49af4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e',
    '378f5a541631229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d0984800a440bdbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb',
    'abbedea680056f52382ae548b2e4f3f38941e71cff8a78db1fffe18a1b3361039fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced',
    '7bcd9ed0efc889fb3002c6cd635afe94d8fa6bbbebab076120018021148466798a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd85d6bcaa4cd81f32d1b',
    '378ee767f11631bad21380b00449b17acda43c32bcdf1d77f82012d430219f9b5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720'
]


def multiply(x, y, p):
    ans = [0] * (len(x) - 1 + len(y))
    for i in range(len(x)):
        for j in range(len(y)):
            ans[i + j] = (int(ans[i + j]) + int(x[i]) * int(y[j])) % p
    return ans


def poly_division(x, y, p):
    obr = 1
    x = del_zeros(x.copy())
    i = 0
    while len(x) >= len(y):
        poly = multiply([obr * x[i]] + [0] * (len(x) - len(y)), y, p)
        x = del_zeros(sub(x, poly, p))
    return x


def del_zeros(x):
    while len(x) > 1 and x[0] == 0:
        x.pop(0)
    return x


def sub(x, y, p):
    if len(x) >= len(y):
        ans = x.copy()
        for i in range(1, 1 + len(y)):
            ans[-i] = (x[-i] - y[-i]) % p
        ans = del_zeros(ans)
        return ans
    else:
        ans = y.copy()
        for i in range(1, 1 + len(x)):
            ans[-i] = (x[-i] - ans[-i]) % p
        for j in range(0, len(y) - len(x)):
            ans[j] = (-ans[j]) % p
        ans = del_zeros(ans)
        return ans


def summ(x, y, p):
    if len(x) >= len(y):
        maxma = x
        minma = y
    else:
        maxma = y
        minma = x
    ans = [0] * len(maxma)
    for i in range(1, 1 + len(minma)):
        ans[-i] = (maxma[-i] + minma[-i]) % p
    for i in range(1 + len(minma), 1 + len(maxma)):
        ans[-i] = maxma[-i] % p
    return ans


def linearConversion(sixteenBytes):
    array_ch = StrToVec(sixteenBytes)
    summa = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(16):
        block = array_ch[i * 8: i * 8 + 8]
        coef = StrToVec(bin(linealCoef[i])[2:].zfill(8))
        multiplied = multiply(block, coef, 2)
        divided = poly_division(multiplied, prime_polynome, 2)
        summa = summ(divided, summa, 2)

    result = ''
    for i in range(len(summa)):
        result += str(summa[i] % 2)
    return result


def StrToVec(string):
    return [int(i) for i in string]


def xor_str(roundKey, initializationVector):
    roundKey = str(roundKey)
    initializationVector = str(initializationVector)
    resultText = ''
    for i in range(len(initializationVector)):
        tempNumber = str((int(initializationVector[i]) + int(roundKey[i])) % 2)
        resultText += tempNumber
    return resultText


def NonLinealTransformation(byte):
    number = int(byte, 2)
    pn = nonlinear_coef[number]
    binaryString = bin(pn)[2:].zfill(8)
    return binaryString


def S(openBlock):
    temp = [openBlock[i:i + 8] for i in range(0, len(openBlock), 8)]
    result = ''
    for i in range(len(temp)):
        result += NonLinealTransformation(temp[i])
    return result


def VecToStr(vec):
    vec_ch = vec.copy()
    if type(vec_ch[0]) == int:
        vec_ch = [str(i) for i in vec_ch]
    return ''.join(vec_ch)


def byteSwap(bytes, tPermutation):
    result = ''
    bytesArr = [bytes[i:i + 8] for i in range(0, 512, 8)]
    for i in range(len(tPermutation)):
        result += bytesArr[tPermutation[i]]
    return result


def L(message):
    result = ''
    for blockStart in range(0, len(message), 64):
        block = message[blockStart:blockStart + 64]
        resultSi = linearConversion(block)
        shifted_block = block[8:] + block[:8]  # Циклический сдвиг влево на 8 байт
        result += resultSi + shifted_block
    return result


def functionCompression(h_temp, m):
    # m - 512 бит, h - 512 бит
    K = '0' * 512

    Key = L(
        byteSwap(S(xor_str(K, m)), tRearrangement))
    for i in range(len(Crearrangent) - 1):
        nextKey = L(
            byteSwap(S(xor_str(Key, bin(int(Crearrangent[i], 16))[2:])),
                     tRearrangement))
        Key = L(
            byteSwap(S(xor_str(nextKey, Key)), tRearrangement))
    nextKey = L(
        byteSwap(S(xor_str(Key, bin(int(Crearrangent[-1], 16))[2:])),
                 tRearrangement))
    Key = xor_str(nextKey, Key)
    return xor_str(xor_str(Key, h_temp), m)


def vectorTransformation(N, s, m):
    N = bin((int(N, 2) + 512) % 512)[2:]
    s = bin((int(s, 2) + int(m, 2)) % 512)[2:]
    while len(N) < 512:
        N = '0' + N
    while len(s) < 512:
        s = '0' + s


def hashFunction(M_engine, keyLength):
    if keyLength not in ['512', '256']:
        print('Введено неверное значение ключа')
        exit()
    h_temp = '0' * 512 if keyLength == '512' else '00000001' * 64
    N, sigma = '0' * 512, '0' * 512
    # Обработка каждого 512-битного блока входных данных
    while len(M_engine) >= 512:
        m = M_engine[-512:]  # Получаем последний блок
        M_engine = M_engine[:-512]  # Удаляем последний блок из M_engine
        h_temp = functionCompression(h_temp, m)
        vectorTransformation(N, sigma, m)
    # Добавление padding к последнему блоку данных
    m = '0' * (511 - len(M_engine)) + "1" + M_engine
    h_temp = functionCompression(h_temp, m)
    vectorTransformation(N, sigma, m)
    # Последние преобразования
    h_temp = functionCompression(functionCompression(h_temp, N), sigma)
    # Обрезаем хеш, если требуется 256-битная длина
    return hex(int(h_temp[:256] if keyLength == '256' else h_temp, 2))[2:]


def read_word_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


def main():
    while True:
        print('Введите название файла')
        word_file_path = str(input())
        word_binary_data = read_word_file(word_file_path)
        file_string = ''.join(format(byte, '08b') for byte in word_binary_data)
        print('Выберите длину ключа: 512 или 256')
        keyLength = input()
        print(
            f'Результат преобразования файла {word_file_path} в хеш-код длиной {keyLength} равен: {hashFunction(file_string, keyLength)}')
        print('Продолжить работу? да/нет')
        inp1 = input()
        if inp1 != 'да' or inp1 == 'нет':
            break


if __name__ == '__main__':
    main()
