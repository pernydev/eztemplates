# look for when files are changed and recompile them.
from compiler import compile_templates
import os
import hashlib
import time

def listen():
    hash = ""
    while True:
        files = os.listdir('templates')
        hashes = []
        for f in files:
            with open('templates/' + f, 'r') as f:
                hashes.append(hashlib.sha256(f.read().encode("utf-8")).hexdigest())
        # let's now get the hash of the hashes
        new_hash = hashlib.sha256(''.join(hashes).encode("utf-8")).hexdigest()
        if new_hash != hash:
            hash = new_hash
            print("Changes detected, recompiling...")
            compile_templates()
        
        time.sleep(3)
        
        


if __name__ == '__main__':
    print("Listening for changes...")
    listen()
