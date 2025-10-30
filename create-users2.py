#!/usr/bin/python3

# INET4031
# Abbie Beekman
# Date Created: 10/26/2025
# Date Last Modified: 10/29/2025

# Importing modules:
# os – to execute system-level commands
# re – to use regular expressions for pattern matching
# sys – to read input from standard input
import os
import re
import sys


def main():
    # Prompt the user for dry-run mode
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().lower()

    # Determine whether we’re in dry-run mode
    dry_mode = (dry_run == 'y')

    for line in sys.stdin:
        # Skip blank lines
        if not line.strip():
            continue

        # Detect comment lines
        match = re.match("^#", line)

        # Split line into fields
        fields = line.strip().split(':')

        # Check for skipped lines or invalid data
        if match:
            if dry_mode:
                print(f"[DRY-RUN] Skipped comment line: {line.strip()}")
            continue

        if len(fields) != 5:
            if dry_mode:
                print(f"[DRY-RUN][ERROR] Invalid line (expected 5 fields, got {len(fields)}): {line.strip()}")
            continue

        # Extract user information
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Notify that account creation is starting
        print(f"==> Creating account for {username}...")

        # Build adduser command
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_mode:
            print(f"[DRY-RUN] Would run: {cmd}")
        else:
            os.system(cmd)

        # Notify password setting
        print(f"==> Setting the password for {username}...")

        # Build password command
        cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_mode:
            print(f"[DRY-RUN] Would run: {cmd}")
        else:
            os.system(cmd)

        # Assign groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"

                if dry_mode:
                    print(f"[DRY-RUN] Would run: {cmd}")
                else:
                    os.system(cmd)


# Entry point of the script
if __name__ == '__main__':
    main()

