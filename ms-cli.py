#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/joshywuf/Minecraft-server-termux-autoscript.git"
REPO_DIR = "Minecraft-server-termux-autoscript"  # folder git clone creates
INNER_DIR = "minecraft"                          # folder inside the repo to rename

STEPS = [
    "pkg update && pkg upgrade -y",
    "pkg install openjdk-25 wget nano -y",
    "pkg install git -y",  # needed for git clone
]

SERVER_COMMANDS = """
Server console commands (type these in the server console, no slash needed):

  Whitelist
    whitelist on / whitelist off        turn the whitelist on or off
    whitelist add <player>              allow a player
    whitelist remove <player>           remove a player
    whitelist list                      show whitelisted players
    whitelist reload                    reload whitelist.json

  Bans and kicks
    ban <player> [reason]               ban a player
    ban-ip <ip|player> [reason]         ban an IP
    pardon <player>                     unban a player
    pardon-ip <ip>                      unban an IP
    banlist players / banlist ips       show bans
    kick <player> [reason]              kick a player

  Operators
    op <player>                         give operator
    deop <player>                       remove operator

  World
    save-all                            save the world now
    save-off / save-on                  pause or resume autosave (use for backups)
    seed                                show the world seed
    setworldspawn                       set world spawn to your position
    time set day / time set night
    weather clear / weather rain
    difficulty <peaceful|easy|normal|hard>
    gamemode <survival|creative|adventure|spectator> <player>

  General
    list                                show online players
    say <message>                       broadcast a message
    stop                                save and stop the server

  To change or reset the world: stop the server, then edit "level-name" in
  server.properties, or delete the world folder to generate a new one.
"""


def run(cmd, **kwargs):
    return subprocess.run(cmd, shell=True, **kwargs)


def run_steps():
    total = len(STEPS)
    for i, cmd in enumerate(STEPS, 1):
        print(f"\n[{i}/{total}] {cmd}")
        if run(cmd).returncode != 0:
            print(f"\nStep {i} failed. Fix it and run the script again.")
            sys.exit(1)


def clone_and_rename():
    print("\nDownloading server files...")
    if Path(REPO_DIR).exists():
        shutil.rmtree(REPO_DIR)
    if run(f"git clone {REPO_URL}").returncode != 0:
        print("Download failed. Check your internet and try again.")
        sys.exit(1)

    while True:
        name = input("\nName of your server folder: ").strip()
        if not name or "/" in name:
            print("Enter a valid name (no slashes).")
        elif Path(name).exists():
            print(f"'{name}' already exists. Pick another name.")
        else:
            break

    repo = Path(REPO_DIR)
    inner = repo / INNER_DIR
    target = Path(name)

    if inner.is_dir():
        shutil.move(str(inner), str(target))
        shutil.rmtree(repo)  # remove the leftover clone wrapper
    else:
        repo.rename(target)

    start = target / "start.sh"
    if start.exists():
        start.chmod(0o755)
    return target


def main():
    run_steps()
    target = clone_and_rename()
    os.chdir(target)  # we are now inside the renamed folder
    print(f"\nServer folder ready: {Path.cwd()}")
    print("\nTo start the server, run:")
    print(f"  cd {target.name}")
    print("  ./start.sh")
    print(SERVER_COMMANDS)


if __name__ == "__main__":
    main()