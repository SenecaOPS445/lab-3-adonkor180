#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: adonkor

import subprocess

def free_space():
    
    result = subprocess.run("df -h / | awk 'NR==2 {print $4}'", shell=True, capture_output=True, text=True)
    
    
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
