#!/usr/bin/python3

# INET4031
# Abbie Beekman
# Date Created: 10/26/2025
# Date Last Modified: 10/26/2025

# Importing modules:
# os – to execute system-level commands
# re – to use regular expressions for pattern matching
# sys – to read input from standard input
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Skip lines that begin with '#' (used for comments or metadata)
        match = re.match("^#", line)

        # Split the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

        # Skip lines that are comments or do not contain exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0]  # Username for the new account
        password = fields[1]  # Password to be set
        gecos = "%s %s,,," % (fields[3], fields[2])  # Full name and other info for GECOS field

        # Split the group field into a list of groups
        groups = fields[4].split(',')

        # Notify that account creation is starting
        print("==> Creating account for %s..." % (username))

        # Construct the command to add a user with disabled password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment to execute user creation command
        # print(cmd)
        # os.system(cmd)

        # Notify that password is being set
        print("==> Setting the password for %s..." % (username))

        # Construct the command to set the user's password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment to execute password setting command
        # print(cmd)
        # os.system(cmd)

        # Assign user to specified groups unless group is '-'
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print(cmd)
                # os.system(cmd)

# Entry point of the script
if __name__ == '__main__':
    main()

