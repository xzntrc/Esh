 <img src="https://media.discordapp.net/attachments/806836894846812160/927413649323204638/Banner.png?width=715&height=227">

## About
Eccentrici Shell (<i>abbrev.</i> ESH) is a small, universal shell, named after its creator - Eccentirici (Latin to mean Eccentrtic). ESH is currently developed in Python, offering simple editing, or an even simplier config.toml file for editing predifined settings. Did I mention that ESH is Free and Open Source? Well, it is!

## Installation
ESH consists of two branches; main and development - it is prefered that you use main.
#### Main:
```
git clone https://github.com/Eccentrici/Esh.git
cd Esh
pip install -r requirements.txt
sh install.sh
```
#### Development
```
git clone --branch development https://github.com/Eccentrici/Esh.git
cd Esh-development
pip install -r requirements.txt
sh install.sh
```
Next, close your terminal, and re-open it. You now should be able to run `esh`.<br>
<i>What if we installed ESH using ESH? 🤯</i>
## Usage
As more commands are added to ESH, they will be added here.

```
kd {path}
```
* Change (with a K) Directory.
	*  `path` is an optional parameter, if not met, it will stay in the current directory.
	*  `path` works with relative directories and absolute directories.
	*  `path` can include a tilde ( ~ ) always, if enabled in the [config](#config) (Example: `kd ~` or `kd ~/Downloads`).
```
pf {path}
```
* Print Files
	* `path` is an optional paramater, if not met, the content of the current working directory is returned.
	* `path` works with relative directories and absolute directories.
	* `pf` prints out all files with highligting - if enabled in the [config](#config).
		* Known Issue: if you use the current working directory, highligting will be applied. If you use a path there will be no highlighting. This is mainly due to my terrible code. 

## Config
A config file (config.toml) is included in the repository, without said config, ESH will not run. It is not required that you edit it, but it is required that there be one.
### Default Config:
```toml
title = "esh"
[colours]
enabled = true
files = "\033[91m" # Red
directories = "\033[93m" #  Yellow

[system]
homedir = ""
usetilde = false
```
* Colours:
	* Colours are accessed with `pf` among other commands.
	* Use ANSI escape code colours for changing colours ([on Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code#colors)).
	* Colours can be enabled/disabled by changing the `enabled` value. If disabled (a value of `false`), existing colour entries will be ignored.
	* Directories and Files have seperate colours in commands. For example, in `pf`.
* System:
	* `homedir` can be changed to reflect the directory that will be accesed with a tilde ( ~ ) - if enabled below. `homedir` will become deprecated - hopefully - in the next release, and replaced with automatic OS detection, unless you would like to use a custom directory.
	* `usetilde` is used to enable the usage of tildes ( ~ ). If enabled, tides will reflect the home directory, for example `kd ~` will change into the home directory.
## Notes
ESH is nothing special, it is merely a project that I have started to pass time this (Dec. 2021) Christmas break. I hope that I'll continue developing this as a sort of "achievement" for myself.

I like writing READMEs :))))))
