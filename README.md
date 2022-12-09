# Keylogging
The repo contains 3 folders under the src folder.

## Loaders
Different variants to run the Python keylogger located in src/payload/python.
Each loader uses the Python exec() function.

## Obfuscator
Custom Python program used to obfuscate any payload in the src/payload folder.
To check the usage:

```bash
$ python main.py -h
usage: main.py [-h] -f FILE [-o] [-l]

Code Obfuscator

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to obfuscate
  -o, --option      Add entropies with comments[0] | assignments[1] | both[2], default both[2]
  -l, --lines       Add entropy lines numbers, default random[500,1000]
```

## Payloads
Different keyloggers developed in C++ and Python. \
C++ keyloggers:
1. GetAsyncKeyState
2. GetKeyboardState
3. Windows Hook (WH_KEYBOARD_LL)
4. GetRawInputData

Python keylogger:
1. Based on pynput library which relies on Windows Hook (WH_KEYBOARD_LL).
