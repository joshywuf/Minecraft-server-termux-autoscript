<div align="center">

```
 __  __  ____       ____ _     ___
|  \/  |/ ___|     / ___| |   |_ _|
| |\/| |\___ \ ___| |   | |    | |
| |  | | ___) |___| |___| |___ | |
|_|  |_|____/     \____|_____|___|
```

# ⛏️ Minecraft Server Termux Autoscript

**Install a fully configured Minecraft server on your Android phone with one script.**

![Platform](https://img.shields.io/badge/platform-Termux%20(Android)-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Python](https://img.shields.io/badge/python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Minecraft](https://img.shields.io/badge/minecraft-26.3-62B47A?style=for-the-badge)
![Crossplay](https://img.shields.io/badge/Java%20%2B%20Bedrock-crossplay-FFB000?style=for-the-badge)

</div>

---

## ✨ What is this?

`ms-cli.py` sets up everything for you in Termux: it installs Java, downloads my pre-configured Minecraft server, lets you name your server folder, and tells you how to start it. No manual setup, no editing config files.

## 🚀 Features

- 📦 **One script install**: updates Termux and installs Java, `wget`, `nano` and `git` automatically
- 🎮 **Java + Bedrock crossplay**: friends on PC and phone can join the same server
- 🏷️ **Name your own server folder** during setup
- 📶 **Offline and LAN ready**: play on your local network without extra accounts
- 🌍 **Play with friends online** using port forwarding or a virtual IP (see below)
- 🧾 **Built-in command cheat sheet** for whitelist, bans, world management and more

> ⚠️ **Version:** this server is configured for Minecraft **26.3 only**.

## 📋 Requirements

| Requirement | Details |
|---|---|
| 📱 Device | Android phone or tablet |
| 💻 App | [Termux](https://github.com/termux/termux-app/releases) (download from GitHub or F-Droid) |
| 💾 Storage | Several GB free |
| 🧠 RAM | 3 GB or more recommended |
| 🌐 Internet | Needed for the install only |

## 📥 Installation

Open Termux and run these commands:

```bash
pkg install -y python curl
curl -fsSLO https://raw.githubusercontent.com/joshywuf/Minecraft-server-termux-autoscript/main/ms-cli.py
python ms-cli.py
```

The script will:

1. 🔄 Run `pkg update && pkg upgrade -y`
2. ☕ Install Java (`openjdk-25`), `wget` and `nano`
3. 📂 Download the configured server with `git clone`
4. ✏️ Ask you to **name your server folder**
5. ✅ Show you how to start it

## ▶️ Starting the server

After the script finishes (replace `myserver` with the name you chose):

```bash
cd myserver
./start.sh
```

To stop it, type `stop` in the server console.

## 🌐 Playing with friends

### 🏠 Same Wi-Fi (LAN)
Connect your friends to the same Wi-Fi as your phone, then join using your phone's local IP address. Find it with:

```bash
ifconfig
```

### 🔌 Port forwarding
Forward the server's port on your router to your phone's local IP, then share your public IP.

| Edition | Default port | Protocol |
|---|---|---|
| Java | `25565` | TCP |
| Bedrock | `19132` | UDP |

> Check the server's config files if you changed the ports. Many mobile data connections do not allow port forwarding, so use the option below if it doesn't work.

### 🛡️ NordVPN Meshnet (easiest)
No router settings needed. Meshnet gives every device a virtual IP so you and your friends can connect as if you were on the same network.

1. Install NordVPN and turn on **Meshnet** on your phone and your friends' devices
2. Link the devices together
3. Join the server using the **Meshnet IP** of the phone running the server

Other virtual-network tools such as Tailscale or ZeroTier work the same way if you prefer them.

## 🕹️ Server commands

Type these in the server console (no `/` needed).

<details>
<summary><b>📋 Whitelist</b></summary>

| Command | What it does |
|---|---|
| `whitelist on` / `whitelist off` | Turn the whitelist on or off |
| `whitelist add <player>` | Allow a player |
| `whitelist remove <player>` | Remove a player |
| `whitelist list` | Show whitelisted players |
| `whitelist reload` | Reload `whitelist.json` |

</details>

<details>
<summary><b>🔨 Bans and kicks</b></summary>

| Command | What it does |
|---|---|
| `ban <player> [reason]` | Ban a player |
| `ban-ip <ip or player> [reason]` | Ban an IP address |
| `pardon <player>` | Unban a player |
| `pardon-ip <ip>` | Unban an IP |
| `banlist players` / `banlist ips` | Show bans |
| `kick <player> [reason]` | Kick a player |

</details>

<details>
<summary><b>👑 Operators</b></summary>

| Command | What it does |
|---|---|
| `op <player>` | Give operator permissions |
| `deop <player>` | Remove operator permissions |

</details>

<details>
<summary><b>🌍 World</b></summary>

| Command | What it does |
|---|---|
| `save-all` | Save the world now |
| `save-off` / `save-on` | Pause or resume autosave (useful for backups) |
| `seed` | Show the world seed |
| `setworldspawn` | Set world spawn |
| `time set day` / `time set night` | Change the time |
| `weather clear` / `weather rain` | Change the weather |
| `difficulty <peaceful/easy/normal/hard>` | Change difficulty |
| `gamemode <mode> <player>` | Change a player's game mode |

**Reset or change the world:** stop the server, then either edit `level-name` in `server.properties` or delete the world folder to generate a new one.

</details>

<details>
<summary><b>⚙️ General</b></summary>

| Command | What it does |
|---|---|
| `list` | Show online players |
| `say <message>` | Broadcast a message |
| `stop` | Save and stop the server |

</details>

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `Unable to locate package openjdk-25` | Run `pkg update`, then `pkg search openjdk` to see the available versions |
| `git: command not found` | Run `pkg install git -y` |
| `./start.sh: Permission denied` | Run `chmod +x start.sh` |
| Server gets killed in the background | Keep Termux open, run `termux-wake-lock`, and disable battery optimization for Termux |
| Friends can't connect | Check you are on the same network or Meshnet, and that the ports above are correct |

## 📄 Disclaimer

This project is not affiliated with, endorsed by, or associated with Mojang Studios or Microsoft. Minecraft is a trademark of Mojang Studios. The server runs in offline mode, so use it on private networks with people you trust.

---

<div align="center">

Made with ☕ by [joshywuf](https://github.com/joshywuf)

⭐ **Star this repo if it helped you!**

</div>
