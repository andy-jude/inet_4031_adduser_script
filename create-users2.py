#!/usr/bin/python3

# INET4031
# Andy Jude
# Created: 3/20/25
# Last Modified: 3/20/25

import os #Allows the program to interact with the operating system, which will allow us to create a new user.
import re #Allows us to search and check if a string contains a pattern.
import sys #Allows us to use command line operations within our code.


def main():
    DryRun = input("Would you like to run this program in dry-run mode? (y/n):  ").lower()
    if DryRun == 'y':
        print("This program is running in dry-run mode.  Changes will not be made to the operating system during this time.")
    elif DryRun == 'n':
        print("This program is running in normal mode.  All changes will be made to the operating system.  Please proceed with caution")
    else:
        print("Not a valid entry.  Please restart the program and try again")
        quit()

    #More info on the "open" command:  https://www.w3schools.com/python/ref_func_open.asp
    file = open("create-users.input", "r")

    for line in file:
        #This will check to see if the line starts with "#".  If it does, it will skip the line since it is meant to be ignored.
        #We can use "#" in front of our lines in our create-users.input file if we want to temporarily skip adding that user for now.  Think of a comment in Python code, we just want to skip it for now.
        match = re.match("^#",line)

        #Splits the lines in the create-users.input file whenever a ":" is present.  
        #This allows us to split it into separate items, like a name, username, password, and group.
        fields = line.strip().split(':')

        #The if statement below is checking to make sure at least five components are passed in to create the user and that we want to create the user by making sure there is no "#" at the beginning of the text in the create-users.index file.
        #If 5 components are not passed in, we know we do not have enough information to create the user.  
        #If the if statement below is true, we will continue running the program.  If not, the program will skip adding this user.
        #The if statement relies on the previous two lines to determine if we should be adding this user or skipping them and to determine if the user has enough info to be added to the system.
        #It is doing that to make sure the program is receiving good information and is error handling.  If wrong information is passed in, it could create a bad user or cause the program to crash, which is obviously not good.
        if match or len(fields) != 5:
            if DryRun == 'y':
                print("Skipping adding user due to insufficient information or user requested skipping the user")
            continue

        #Now that the data is split up, we can extract it and use the data to create the user.  The first item in the list is the username, the second is the password, and the third is other information needed to create the user.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splitting is being completed to see what groups the users will need to belong to.  Each group for the user is separated by a "," in the create-users.input file.
        groups = fields[4].split(',')

        #Print statement to confirm the account is successfully being created.
        print("==> Creating account for %s..." % (username))
        
        #The new user is being created.  Information is being passed through to the OS.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #The following statement below is commented out to prevent accidental creation of a new user if you are not ready.  Please only uncomment this command if you are ready to create a new user and have done a test run in the past.
        if DryRun == 'y':
            print(cmd)
        else:
            os.system(cmd)

        #The following print statement confirms the password is being set for the user being processed.
        print("==> Setting the password for %s..." % (username))
        #The line below is creating the password for the user.  It is passing in what was sent through the create-users.index file as the user's password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #The following lines should be uncommented once you are certain the code is running properly and you are ready to add the new user.  Once you have run a test run of the program, please uncomment the following lines of code to have it execute.
        if DryRun == 'y':
            print(cmd)       
        else:
            os.system(cmd)

        for group in groups:
            #"-" is a placeholder if the user should not be assigned to any group.  If there is not a "-" in the user's group settings, they will be assigned to the correct group(s) below.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                if DryRun == "y":
                    print(cmd)
                else:
                    os.system(cmd)              

if __name__ == '__main__':
    main()
