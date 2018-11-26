'''
Helper script that clones/pulls user repositories to grab the latest code.
'''

import os
import shutil

users = ['tomflannaghan']  # list of github user accounts.

# Path of the maze installation that we want to import into.
maze_installation = '/home/flannt/maze'

for user in users:
    if not os.path.exists(user):
        cmd = "git clone git://github.com/{}/maze {}".format(user, user)
    else:
        cmd = "cd {} && git pull".format(user)
    print(cmd)
    os.system(cmd)

if maze_installation is not None:
    os.makedirs(os.path.join(maze_installation, 'users'), exist_ok=True)
    for user in users:
        shutil.copyfile(os.path.join(user, "goodies.py"),
                        os.path.join(maze_installation, 'users', '{}.py'.format(user)))
