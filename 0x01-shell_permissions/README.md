0-iam_betty---> su betty = changes user
1-who_am_i---> whoami = prints the effective userid
2-groups---> groups = prints all the groups the current user is part of.
3-new_owner---> chown betty hello = changes the owner of the file
4-empty---> touch hello = creates an empty file
5-execute---> chmod u+x hello = adds execute permission to the owner
6-multiple_permissions---> chmod ug+x,o+r hello = adds execute permission to the owner and the group owner, and read permission to other users
7-everybody---> chmod ugo+x hello = adds execution permission to the owner, the group owner and the other users
8-James_Bond---> chmod 007 hello = script that changes permissions to 007
9-John_Doe---> chmod 753 hello = script that changes permissions to 753
10-mirror_permissions---> chmod --reference=olleh hello = Script that sets the file with the set of another file
11-directories_permissions---> chmod ugo+X * = adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
12-directory_permissions---> mkdir -m 751 dir_holberton = script that creates a directory called dir_holberton with permissions 751 in the working directory.
13-change_group---> chgrp holberton hello = changes the group owner
14-change_owner_and_group---> chgrp holberton hello = changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
15-symbolic_link_permissions---> chown -h betty:holberton _hello = changes the owner and the group owner of the file _hello to betty and holberton respectively.
16-if_only---> chown --from=guillaume betty hello = changes the owner of the file hello to betty only if it is owned by the user guillaume.
100-Star_Wars---> telnet towel.blinkenlights.nl = plays star wars episode iv
101-man_holberton---> .TH man 2 "04 May 2015" "0.32" "holberton man page" = file that contains a man page that looks exactly that the question of hollberton
.SH NAME
.B holberton
- become a full-stack software engineer.
.SH SYNOPSIS
holberton [STUDENTNAME]
.SH DESCRIPTION
Holberton School is a project-based alternative to college for the next generation of software engineers.
.SH OPTIONS
.B holberton
does not take any options. However, you can supply studentname.
.SH SEE ALSO
.I peerlearning(2), projectbased(2), fullstack(2), Betty(1)
.SH BUGS
No known bugs.
.SH AUTHOR
Julien Barbier, Sylvain Kalache, Sophie Barbier, Guillaume Salva, Kris Bredemeier, Julien Cyr, Alex Gautier and all the Holberton mentors
