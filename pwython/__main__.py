from random import choice
from re import sub
from subprocess import PIPE, Popen
from sys import argv, executable, stderr

from .responses import pronouns, reactions, remarks


def owoify(text):
    if type(text) == bytes:
        text = str(text)[2:-1].replace("\\n", "\n")

    text = sub("[rlv]", "w", text)
    text = sub("[RLV]", "W", text)
    text = sub("ee", "wee", text)

    return text


def main():
    process = Popen([executable] + argv[1:], stderr=PIPE)

    while process.poll() is None:
        for line in iter(process.stderr.readline, b""):
            if line == b"Traceback (most recent call last):\n":
                stderr.write(f"{choice(pronouns)}, {choice(remarks)} {choice(reactions)}\n")

            stderr.write(owoify(line))


if __name__ == "__main__":
    main()
