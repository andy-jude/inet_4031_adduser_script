# INET4031 Add Users Script and User List Program.

## Program Description
This program allows you to automate adding multiple users to a Linux operating system.  Instead of manually adding each user to the operating system using the GUI or command-line prompt, this program takes in a list of users and adds them to the operating system. 

This program helps save time, reduce errors, and is easy to use.

In a typical workspace, a user would need to be added through the command line prompt by using commands like "adduser".  Once this command is run, the OS will ask a variety of questions, like what groups to add the user to, a password for the user, and contact information for the user.  If you are only adding one or two users, this is simple enough to do.  However, if you are an enterprise, this can be a tedious task without software to automate this process.

## Program User Operation
To run this program, you will need to create a list of users and add them to the "create-users.index" file.  Formatting for this can be found below.  It is highly recommended you do a "Dry Run" of this program before actually running it.  If a dry run is not completed, you may run into errors that cannot be fixed.  You can run a "Dry Run" by commenting out any OS imports that would interact with the operating system.  If the program runs well with the OS imports commented out, you should be good to go for a successful run!

### Input File Format
Each line in the input file is a new user.  The new user line should be formatted as follows:
 > username:password:LastName:FirstName:group1, group2

Multiple groups can be added to one user.  Each group must be separated by a ",".
If you'd like to skip adding a user temporarily, simply add a "#" before the username section.
If the user does not need to be added to any groups, use the "-" symbol in the groups field.

### Command Excuction
To run this code, copy this GitHub Repo to your computer.  Update the "create-users.input" file with the users you'd like to add.  To run this program, make sure it is marked as an executable file.  In a Linux OS, you can do this by running the following command:
> chmod +x create-users.py

Once this is marked as an executable file, you can run it using the following command:
> ./create-users.py < createusers.input


### "Dry Run"
A "Dry Run" is highly encouraged for this program.  Completing a dry run will allow you to test the program to make sure all functions are working as intended before committing to adding new users.  You can run a dry run of this program by commenting out all three of the "OS" imports and code in the "create-users.py" file.  Once the program is successfully running, uncomment out all the "OS" imports and code to add the users to your computer.
