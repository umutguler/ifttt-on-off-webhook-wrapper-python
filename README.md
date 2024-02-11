## IFTTT On-Off Event Wrapper Python

This repo is a wrapper that allows on/off commands to be done with the [IFTTT-Webhook Library](https://github.com/DrGFreeman/IFTTT-Webhook)

## Use Cases

I've personally used it to control my studio speakers/monitors that have individual switches on the back. So I hooked them up to TP-LINK Tapo Smart Plugs.

This script allows me to integrate to IFTTT's Webhook feature, and send an on or off event

It can be triggered in anyway you wish. I personally mapped a macro key or G-Key on my Logitech keyboard to run the command.

## How to Run

1. A `.env` file is needed to execute, or override by passing parameters instead in the source code.

   - Rename the `.env.template` to `.env`
   - Replace the values for the variables inside
2. You can manually call it with Python, but it's easier if you just build it to an executable in your OS you want it to run on.

   - `pyinstaller --onefile .\main.py --name [ExecutableName]`
