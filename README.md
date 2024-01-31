<h1 align="center">Collatz encryption tool</h1>

This script is a *proof of concept*. Utilizing _**collatz iteration**_, this CLI tool can encrypt and decrypt ASCII files with or without a custom passkey.

## Table of Contents

[Installing](#installing)
* [On Linux](#on-linux)
* [On Windows](#on-windows)
* [Uninstalling on Linux](#uninstalling-on-linux)

[Usage](#usage)
* [Flag usage](#flag-usage)

[Concept](#concept)
## Installing

### On Linux

Run the provided `install.sh` script. Give the install script execute permissions by running `chmod +x ./install.sh` in the current directory.

### On Windows

On Windows run `python3 colcipher.py` through PowerShell in the current directory.

### Uninstalling on Linux

Run `sudo ~/.local/share/colcipher/uninstall.sh`

-----

## Usage

Simplest way to use colcipher is to encode text directly by running
```
colcipher "Some text"
```
This will output `889 26 388 13 287 87 15 14 53 23` and exit.

-----

### Flag usage

Available options are:
```text
-t, --text        Reads text from next command-line argument as input
-f, --file        Takes input from file and outputs to file
-o, --output      Output to file and choose file name
-e, --encrypt     Encrypt input
-d, --decrypt     Decrypt input
-k, --key         Choose custom key for encryption or decryption
-s                Output to console instead of file.
-h, --help        Print this text and exit
```

Flags can be used in any order.

The `-t`, `-f`, `-o` and `-k` options all require second arguments right after them, otherwise their usage is invalid and will result in unwanted behaviour.

Examples:

```bash
colcipher -t "Some text."
colcipher -f input.txt -o encoded.txt
colcipher -t "Custom key test" -k 293569
``` 

> **_NOTE:_**
If a custom passkey is not provided, one is derived from the sum of the ASCII values of the plaintext itself and is inserted as the first number in the ciphertext.
If a custom passkey is provided, it is not saved in the ciphertext.

The `-e`, `-d`, `-s` and `-h` flags are standalone flags requiring no additional arguments. These are basically switches for customizing the behaviour and handling of input and output.

Examples:

```bash
colcipher -d -t "889 26 388 13 287 87 15 14 53 23" -o decoded.txt
colcipher -d -f encoded.txt -s
colcipher -e -f ~./somedir/plain.txt -s
colcipher --help
```

-----

# Concept

The encoding/encryption algorithm works by generating numbers using the iterative function from the famous [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), the **key**, whether custom or derived from the plaintext, is the starting number from which iteration starts. 

When iteration reaches the 4, 2, 1 loop, the algorithm moves to the next number and continues iterating, thus generating numbers to work with.

Using these numbers, the tool *finds numbers whose remainder after dividing by 128* ***is the ASCII value of our given plaintext character*** and records **how many collatz iterations it took** to get to that number from the starting number. After finding the first number for our first character, the iteration counter is reset to `0` and counting begins again until our second number is found. This is repeated until our entire plaintext is exhausted. **The collection of number of iterations it takes to get to each correct number is the final ciphertext**. 

