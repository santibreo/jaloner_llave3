import re
import base64
from pathlib import Path
from binascii import Error
from itertools import product
from typing import Literal
from Crypto.Cipher import AES, Blowfish


#  images_dirpath = Path("images")
#  for imgpath in images_dirpath.iterdir():
#      with open(imgpath, "rb") as image_file:
#          data = base64.b64encode(image_file.read())
#          print(data.decode()[:300])
#          print("=" * 80)


poema = Path("./Chantal_Maillard_EL_PEZ.txt").read_text(encoding="utf-8")
poema_lines = []
vowels = "aeiou"
for line_raw in poema.splitlines():
    line = line_raw[line_raw.find("|") + 1 :].strip()
    if line and all(l == "-" for l in line):
        break
    if all(vowel in line for vowel in vowels):
        print(f"all vowels:: {line}")
    if len(line) in (16, 24, 32, 48, 64):
        print(f"{len(line):010d}:: {line}")
    poema_lines.append(line)


# AES explanation by example --------------------------------------------------
#  # This has been done by Jaloner
#  message = 'Youtube URL'
#  cipher = AES.new(key, AES.MODE_EAX, nonce=nnc)
#  ciphertext = cipher.encrypt(base64.b64encode(message.encode()))
#  b64_tgcode = base64.b64encode(ciphertext).decode()
#
#  # This has to be done by us
#  ciphertext = base64.b64decode(b64_tgcode.encode())
#  cipher = AES.new(key, AES.MODE_EAX, nonce=nnc)
#  base64.b64decode(cipher.decrypt(ciphertext)).decode('ISO-8859-2')


# Decrypt telegram message
b64_tgcode = open("llave3_codigo_telegram.txt").read().strip()
ciphertext = base64.b64decode(b64_tgcode.encode())
Algorithm = Literal["aes", "fish"]
DecipherMode = Literal[9, 1, 2, 3, 4, 5]
MODE_NAMES = {
    AES.MODE_EAX: "EAX",
    AES.MODE_ECB: "ECB",
    AES.MODE_CBC: "CBC",
    AES.MODE_CFB: "CFB",
    AES.MODE_OFB: "OFB",
}


def decipher(
    algorithm: Algorithm,
    key: bytes,
    mode: DecipherMode = AES.MODE_EAX,
    nonce: bytes = b"1" * 16,
    iv: bytes = b"1",
) -> str:
    """Decrypts Jaloner ciphertext using specific algorithm and decryption
    configuration.

    Supported algorithms: 'aes', 'blowfish'
    Supported modes: AES.MODE_EAX, AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB
    """
    global ciphertext

    # Short keys are filled with null bytes
    if algorithm == "aes" and len(key) not in (16, 24, 32):
        ceil = abs(-len(key) // 16) * 16
        key += b"\x00" * (ceil - len(key))

    algo = AES if algorithm == "aes" else Blowfish
    if mode == AES.MODE_EAX:
        if algorithm == "aes" and len(key) not in (16, 24, 32):
            ceil = abs(-len(key) // 16) * 16
            key += b"\x00" * (ceil - len(key))
        cipher_init = 0
        cipher = algo.new(key, mode=mode, nonce=nonce)
    elif mode == AES.MODE_ECB:
        cipher_init = 0
        cipher = algo.new(key, mode=mode)
    elif mode in {AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB}:
        cipher_init = algo.block_size
        cipher = algo.new(key, mode=mode, iv=ciphertext[: algo.block_size])
    else:
        raise ValueError(f"Mode {mode!r} is not a valid decription mode")
    #  deciphertext = cipher.decrypt(ciphertext[cipher_init:])
    deciphertext = cipher.decrypt(b64_tgcode.encode()[cipher_init:])
    #  url = base64.b64decode(deciphertext).decode("ISO-8859-2")
    url = deciphertext.decode("ISO-8859-2")
    return url


def prRed(skk):
    return "\033[91m {}\033[00m".format(skk)


def prBlue(skk):
    return "\033[93m {}\033[00m".format(skk)


def prGreen(skk):
    return "\033[92m {}\033[00m".format(skk)


nncs = [
    #  b"Jaloner",
    #  b"jaloner",
    #  b"jal66",
    #  b"jal-66",
    #  b"55",
    #  b"cincuentaycinco",
    #  b"cincuenta y cinco",
    #  bytes([55]),
    #  b"oner",
    #  b"55oner",
    #  b"55 oner",
    #  b"55-oner",
    #  b"tanoner",
    #  b"tan oner",
    #  b"tan-oner",
    #  b"adios",
    #  "adiós".encode("latin-1"),
    #  b"boqueando",
    #  b"Boqueando",
    #  b"infinito",
    #  b"Infinito",
    #  b"impotencia",
    #  b"Impotencia",
    #  b"oblongo",
    #  b"Oblongo",
    #  b"abismo",
    #  b"Abismo",
    #  b"sentido",
    #  b"Sentido",
    #  b"superficie",
    #  b"Superficie",
    #  b"infinito",
    #  b"Infinito",
    #  b"palabra",
    #  b"Palabra",
    #  b"sagitario",
    #  b"Sagitario",
    #  b"aries",
    #  b"Aries",
    #  "bondad de espíritu".encode("latin-1"),
    #  "voluntad de sentido".encode("latin-1"),
    #  b"55277446687",
    "GGSÄÄción".encode("latin-1"),
    "GGSÄÄción:".encode("latin-1"),
]
keys = [
    b"realmente soy yo",
    #  r"¿realmentesoyyo?".encode("latin-1"),
    #  b"pasado un cometa",
    #  b"descodificadores",
    #  b"Pez en la orilla",
    #  b"pez en la orilla",
    #  r"¿que es lo real?".encode("latin-1"),
    #  r"¿qué es lo real?".encode("latin-1"),
    #  b"autoconocimiento",
    #  b"la clave secreta",
    #  b"caos no esquemas",
    #  b"reinodeloscielos",
    #  b"muchsimavergenza",
    #  b"sujeto a cambios",
    #  b"palabra infinito",
    #  b"conmigo Infinito",
    #  b"conmigo infinito",
    #  b"sientes Infinito",
    #  b"sientes infinito",
    #  b"Decir superficie",
    #  b"decir superficie",
    #  b"ver las palabras",
    #  b"creo en ascender",
    #  b"servidor tumbado",
    #  b"si el escupitajo",
    #  b"decir impotencia",
    #  b"tiempo es aurora",
    #  b"tiempo es Aurora",
    #  b"momento es ahora",
    #  b"miyo en sollozos",
    #  b"cincuentaycinco1",
    #  b"Jal sesentayseis",
    #  b"Jal-sesentayseis",
    #  b"jal sesentayseis",
    #  b"jal-sesentayseis",
    #  b"desprovisto oner",
    #  b"desprovisto-oner",
]


kwargs_iterables = {
    (AES.MODE_EAX,): [
        {"key": k, "nonce": n} for k, n in product(keys + nncs, nncs + keys)
    ],
    (AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB): [
        {"key": k} for k in keys + nncs
    ],
}

counter, found_counter, nice_counter = 0, 0, 0
solutions = []
for algo in ("aes", "blowfish"):
    for modes, kwargs_iterable in kwargs_iterables.items():
        for mode in modes:
            msg_base = (
                f"{prBlue('algo')}={algo:<8} {prBlue('mode')}={MODE_NAMES[mode]} "
            )
            for kwargs in kwargs_iterable:
                counter += 1
                msg_prefix = msg_base + ", ".join(
                    (f"{prBlue(x)}={y.decode('latin-1')}" for x, y in kwargs.items())
                )
                msg_visible = re.sub(r"\x1b\[\d{2}m", "", msg_prefix)
                msg_prefix += " " * (75 - len(msg_visible)) + "==>"
                try:
                    message = decipher(algorithm=algo, mode=mode, **kwargs)
                except (KeyError, Error) as error:
                    continue
                except ValueError as error:
                    print(msg_prefix + " " + str(error), end="\n")
                    continue
                else:
                    if not message.isascii():
                        solutions.append(f"0:{msg_prefix} {prRed('Ugly')}: {message!r}")
                    else:
                        solutions.append(
                            f"1:{msg_prefix} {prGreen('Nice')}: {message!r}"
                        )
                        nice_counter += 1
                    found_counter += 1

# Save results
solutions = sorted(solutions)
Path("results.txt").write_text(
    "\n".join(map(lambda x: re.sub(r"\x1b\[\d{2}m", "", x[2:]), solutions))
)
print(*[x[2:] for x in solutions], sep="\n")
print("=" * 80)
found_perc, nice_perc = found_counter / counter, nice_counter / counter
print(f"{counter: 4d} trials: {found_perc:.2%} found || {nice_perc:.2%} nice")
