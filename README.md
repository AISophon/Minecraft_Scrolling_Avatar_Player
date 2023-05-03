# Minecraft_Scrolling_Avatar_Player
A Python script used to display Minecraft player avatars and corresponding IDs.

Intended for use in server promotional videos to display a list of members.

The method used to implement this is by generating characters corresponding to the ID in the image file, and moving and drawing the character avatars on the screen. The corresponding character ID is displayed below the image. The program adds a new character every 600 milliseconds, and removes the character from the list when their position exceeds the screen height. Characters' positions and states are constantly updated and drawn on the screen in the main loop of the program. The program uses Pygame's timer and event handling mechanism.

**English** | [中文](https://github.com/AISophon/Minecraft_Scrolling_Avatar_Player/blob/master/README_cn.md)

## Precautions:
- This software is independently developed by AISophon (QQ:`2498946652`)

- If you need to reprint/modify it, you need to obtain the consent of the author AISophon (QQ:`2498946652`). Violators will be held liable!

- The software is only tested on `Windows 11 Home Chinese Version 22H2`.

- If other systems/modified systems are used, the author AISophon (QQ:`2498946652`) cannot guarantee successful operation.

- The author AISophon (QQ:`2498946652`) is not responsible for the losses caused to hardware/software if other systems/modified systems are used!

## Tutorial:
1. Download `MSAP.zip`.

2. Unzip `MSAP.zip`.

3. Open the `MSAP` folder.

4. Open the `id.txt` TXT document in the `MSAP` folder.

5. Enter the server player ID, separated by line breaks, as follows:

   `AISophon`

   `Homo`

   **Note**: Do not start with a line break and do not have blank lines in the middle.

6. Save the `id.txt` TXT document.

7. Open the `skin` folder.

8. Put the corresponding player avatar (in PNG format) in it. For example, if there is a player named `AISophon` in the `id.txt` TXT document, put a 32*32 PNG image named `AISophon.png` in the `skin` folder.

   **Note**: If the player does not have a skin, the program will automatically use `default.png` to complete it. Please do not delete `default.png`!

9. Go back to the `MSAP` folder.

10. Run the `Minecraft_Scrolling_Avatar_Player.exe` application.

11. A window will pop up with the results.

## Confidential
If you like it, please give this repository a star~

If you have better ideas, feel free to submit a PR or issue.
