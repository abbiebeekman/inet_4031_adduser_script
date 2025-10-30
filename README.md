# INET4031 Add Users Script and User List

## Program Description

The Add Users Script is designed to automate the process of adding multiple users to a Linux system using an input file. Normally, a system administrator must manually enter a series of commands such as adduser, passwd, and adduser <username> <group> to create new users, set their passwords, and assign them to groups. This script automates those same commands by reading user information from an input file and executing the appropriate system commands for each entry.

By automating this task, the script helps reduce manual typing, minimize human error, and speed up the process of onboarding new users in bulk. The script essentially takes care of performing the same operations an administrator would do manually, but in a batch, repeatable, and consistent manner.

## Program User Operation

The program reads user information line by line from an input file (redirected into the script’s standard input) and creates system accounts accordingly. Each line in the file represents a user to be created, along with their password, name information, and group memberships.

Before running the script, ensure it has executable permissions. During execution, the script will either print out what it would do (in a "dry run") or actually perform the commands to add users, depending on how it’s configured.

### Input File Format
Each line in the input file should contain five colon-separated fields, in the following format:
username:password:last_name:first_name:groups

Field descriptions:
- username — The desired login name for the new user.
- password — The user’s password (entered in plain text).
- last_name — The user’s last name.
- first_name — The user’s first name.
- groups — A comma-separated list of groups to which the user should be added. Use a dash (-) if the user should not be added to any additional groups.

Comments and blank lines:
- Any line beginning with a # character is treated as a comment and skipped.
- Blank lines or lines with missing fields (anything not containing exactly five colon-separated values) are ignored.

To skip a user:
Simply comment out their line by adding a # at the start of it.

To omit group assignment:
Use - in the groups field.

### Command Excuction
To run the script, ensure it is executable and that you have sufficient privileges (typically root or via sudo). Then, use the following command syntax:

`chmod +x create-users.py
./create-users.py < createusers.input`

The script reads from standard input, so it’s important to use input redirection (<) to feed in your user list file.

Behind the scenes, the script uses these Linux commands:
- `/usr/sbin/adduser` — to create the user account.
- `/usr/bin/passwd` — to set the user’s password.
- `/usr/sbin/adduser` <username> <group> — to add the user to one or more groups.

Each command is constructed dynamically from the input file fields and executed via os.system() calls (once uncommented for production use).

### "Dry Run"
When first testing the script, you should leave the os.system() calls commented out. In this "dry run" mode, the script will print out the commands it intends to execute rather than actually running them.

This allows you to:
- Verify that your input file is correctly formatted.
- Check the exact commands that would be executed on the system.
- Ensure there are no syntax or logic errors before performing real user creation.

Once you’re satisfied with the dry run output, you can uncomment the os.system(cmd) lines to enable actual execution of the commands.
