import os
import argparse

def vprint(msg):
    if verbose:
        print(msg)

def link(srcPath, dstPath):
    vprint("Linking " + dstPath + " to " + srcPath + "...")
    try:
        os.symlink(srcPath, dstPath)
    except FileExistsError:
        vprint("Linking failed. " + dstPath + " Probably already exists. Deleting it.")
        os.rmdir(dstPath)
        vprint("Linking " + dstPath + " to " + srcPath + "...")
        os.symlink(srcPath, dstPath)





## A ~B ~C D E F G ~I J K ~L ~M N ~O ~P Q ~R ~S T U ~V ~W X Y Z
parser = argparse.ArgumentParser(description='Create symbolic links between critical minecraft folders.')
### CONST ARGS
parser.add_argument("source",
    help="Path to the base .minecraft folder where, for example, worlds will be synced.")
parser.add_argument("new",
    help="Path to un-initiated .minecraft folder to-be. depending on what is chossen to sync, this folder will recivie various symlinks.")

### Folder syncs
parser.add_argument("-b", "--backups", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("-c", "--config", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("-i", "--screenshots", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("-l", "--logs", action="store_true", default=False,
    help="Add symbolic link to logs. Recommended not to use.")
parser.add_argument("-m", "--mods", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("-r", "--resources", "--resourcepacks", action="store_true", default=False,
    help="Add symbolic link to resource packs. NOT compatible with old texturepacks")
parser.add_argument("-s", "-w", "--worlds", "--saves", action="store_true", default=False,
    help="Add symbolic link to worlds.")
# Long format / rare
parser.add_argument("--replays", action="store_true", default=False,
    help="Add symbolic link to repaly folders for those using replay mod.")
parser.add_argument("--schematics", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("--server-resource-packs", "--server-packs", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("--shaders", "--shaderpacks", action="store_true", default=False,
    help="Add symbolic link to worlds.")
# Unimplemetend
parser.add_argument("--ffmpeg", action="store_true", default=False,
    help="Add symbolic link to ffmpeg. NOT IMPLEMENTED!")
parser.add_argument("--textures", "--texturepacks", action="store_true", default=False,
    help="Untested. ¯\_(ツ)_/¯")

### File syncs
parser.add_argument("-o", "--options", action="store_true", default=False,
    help="Add symbolic link to worlds.")
parser.add_argument("-p", "--servers", action="store_true", default=False,
    help="Add symbolic link to worlds.")

### Extras
parser.add_argument("-v", "--verbose", action="store_true", default=False,
    help="Enable extra outputs.")

args = parser.parse_args()



verbose = args.verbose

src = args.source
dst = args.new

if not src.endswith("\\"):
    vprint("Source doesn't end with '\\'. Adding now...")
    src = src + "\\"

if not dst.endswith("\\"):
    vprint("Destination doesn't end with '\\'. Adding now...")
    dst = dst + "\\"

backups = args.backups
config = args.config
screenshots = args.screenshots
logs = args.logs
mods = args.mods
resources = args.resources
saves = args.worlds
replays = args.replays
schematics = args.schematics
server_packs = args.server_resource_packs
shaders = args.shaders
ffmpeg = args.ffmpeg
textures = args.textures
options = args.options
servers = args.servers

backupsPath = dst + "backups"
configPath = dst + "config"
screenshotsPath = dst + "screenshots"
logsPath = dst + "logs"
modsPath = dst + "mods"
resourcesPath = dst + "resourcepacks"
savesPath = dst + "saves"
replayRecordingPath = dst + "replay_recordings"
replayVideosPath = dst + "replay_videos"
schematicsPath = dst + "schematics"
server_packsPath = dst + "server-resource-packs"
shadersPath = dst + "shaderpacks"
ffmpegPath = dst + "ffmpeg"
texturesPath = dst + "texturepacks"
optionsPath = dst + "options.txt"
serversPath = dst + "servers.dat"

srcBackupsPath = src + "backups"
srcConfigPath = src + "config"
srcScreenshotsPath = src + "screenshots"
srcLogsPath = src + "logs"
srcModsPath = src + "mods"
srcResourcesPath = src + "resourcepacks"
srcSavesPath = src + "saves"
srcReplayRecordingPath = src + "replay_recordings"
srcReplayVideosPath = src + "replay_videos"
srcSchematicsPath = src + "schematics"
srcServer_packsPath = src + "server-resource-packs"
srcShadersPath = src + "shaderpacks"
srcFfmpegPath = src + "ffmpeg"
srcTexturesPath = src + "texturepacks"
srcOptionsPath = src + "options.txt"
srcServersPath = src + "servers.dat"

if backups:
    link(srcBackupsPath, backupsPath)

if config:
    link(srcConfigPath, configPath)

if screenshots:
    link(srcConfigPath, screenshotsPath)

if logs:
    link(srcLogsPath, logsPath)

if mods:
    link(srcModsPath, modsPath)

if resources:
    link(srcResourcesPath, resourcesPath)

if saves:
    link(srcSavesPath, savesPath)

if replays:
    link(srcReplayRecordingPath, replayRecordingPath)
    link(srcReplayVideosPath, replayVideosPath)

if schematics:
    link(srcSchematicsPath, schematicsPath)

if server_packs:
    link(srcServer_packsPath, server_packsPath)

if shaders:
    link(srcShadersPath, shadersPath)

if ffmpeg:
    link(srcFfmpegPath, ffmpegPath)

if textures:
    link(srcTexturesPath, texturesPath)

if options:
    link(srcOptionsPath, optionsPath)

if servers:
    link(srcServersPath, serversPath)
