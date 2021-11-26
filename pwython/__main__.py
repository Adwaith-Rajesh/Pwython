from random import choice, randint
from re import sub, split, findall
from string import ascii_letters
from subprocess import PIPE, Popen
from sys import argv, executable, stderr

from .responses import pronouns, reactions, remarks


def owoify(text):
    if type(text) == bytes:
        text = str(text)[2:-1].replace("\\n", "\n")

    text = sub("[rlv]", "w", text)
    text = sub("[RLV]", "W", text)
    text = sub("ee", "wee", text)

    # This is to convert the string into a array whilst maintaining whitespace
    words = split(r"\s+", text)
    whitespace = findall(r"\s+", text)

    text = [None] * (len(words) + len(whitespace))
    text[::2], text[1::2] = words, whitespace

    # Random stutter
    for idx, word in enumerate(text):
        if len(word) > 0:
            if word[0] in ascii_letters and word[0].lower() not in "aeiouw":
                if randint(1, 10) == 1:
                    text[idx] = f"{word[0]}-{word}"

    text = "".join(text)

    return text


def main():
    process = Popen([executable] + argv[1:], stderr=PIPE)
    error = False
    while process.poll() is None:
        for line in iter(process.stderr.readline, b""):
            if line == b"Traceback (most recent call last):\n":
                error = True
                # Easter egg :)
                if randint(1, 10) == 1:
                    stderr.write(f"{choice(pronouns)}, {choice(remarks)}, you sussy baka {choice(reactions)}\n")
                else:
                    stderr.write(f"{choice(pronouns)}, {choice(remarks)} {choice(reactions)}\n")

            stderr.write(owoify(line))

    return 1 if error else 0

if __name__ == "__main__":
    raise SystemExit(main())
