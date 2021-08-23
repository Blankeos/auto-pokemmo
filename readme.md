# 🦄 Python Automation for PokeMMO

These are just practice python bots I'm writing for the PokeMMO game.

Pokemon has always been a game that takes a lot of grinding. Most of the grinding you do are just repeatable tasks like walking around and pressing the same button over and over again. This is why I wrote a bot that could do stuff like hatching eggs for me, level up from wild pokemon, or just simply raise happiness points for my Pokemon while I do something else IRL.

## 🤖 The Bots

- [x] AutoBattler - Walks on the grass back and forth, spams 'A' key to use moves while in battle.
- [x] AutoWalker - Walks back and forth, for hatching eggs, raising happiness while walking.


## 🔧 How to use

These bots take a lot of setup to get up and running on your computer. I'm planning to write a GUI for these bots using TKinter some day.
But for now, the bots just run on console.

> I'll write better documentation on how to setup in the future

1. Go to the folder of the bot you want to use
2. Install dependencies in `requirements.txt`
> You can either create a virtual environment or just install them on your default python environment
3. Run `main.py`
4. Once ran, the bot will start firing inputs so make sure to put your focus on the game. 
> That also means you can't use the computer while the bot is running. (Very unintuitive, I know. But at least you don't have to do the mundane work anymore)

### For AutoBattler

> You need to make sure that you put your character's head on the `/images` folder.
> Replace these images
```
player_faceright.png
player_faceleft.png
```
> This is how the bot recognizes whether or not you're currently battling or looking for wild pokemon