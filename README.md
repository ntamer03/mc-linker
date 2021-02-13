# Minecraft Linker

A command line utility to sync data between Minecraft game directories.

This is just a simple tool to easily setup new Minecraft game directories that have certain data synced using Windows symbolic links.

## Use Cases

This is made to allow you to keep mod sets in seperate game directories to allow you to have multiple modded versions or multiple mod sets accessable from your launcher, but sync servers, saves, and settings across all of those versions.

While this tool was designed for those use cases, there may be other uses for it.

## Plans

Right now this tool is written in Python to be run on Windows. It has almost no testing and I in no way expect it to work. That said, I do plan to keep working on this, so issues and PR's would be appreciated.

- Re-write in Java to better reflect the expected environments of users.
- Add (bad) Linux and Mac support.
- Support for custom directyories so every modded senario isn't hard coded.

## Usage

First install Python 3.8 and make sure it is in `$PATH` by going to `win > Search 'cmd'` and running ` python -v `.

Now download the repository either by using the github download button and extracting the `.zip` into a convientent folder, or using `git clone` into a convienent folder. To finish downloading the utility go to `win > Search 'cmd'` and `cd` to your install directory. Use `cd /D` if you chose to download the tool to a secondary drive. Now run `pip install -r requirments.txt` to download all of the required tools.

Finally go to `win > Search cmd` and select `run as administrator`. Currently creating the symbolic links in python requires administrator access. Now `cd` to your install directory using `/D` if you installed to a secondary drive, then run `python linker.py -h` to view the help and `python linker.py [source dir] [linked directory] [args]`. See below for an explination of the arguments.

### Aruments

- `source` - The directory that stores, for example, saves to be synced across other directories.
- `new` - The directory that will be used by the minecraft launcher and have symbolic links to sync to the `source` directory.
- `-b` - Todo
- `-c` - Todo
- `-i` - Todo
- `-l` - Todo
- `-m` - Todo
- `-r` - Todo
- `-s`, `-w` - Todo
- `--replays` - Todo
- `--schematics` - Todo
- `--server-resource-packs` - Todo
- `--shaders` - Todo
- `--ffmpeg` - Todo
- `--textures` - Todo
- `-o` - Todo
- `-p` - Todo
- `-v` - Verbose output.
