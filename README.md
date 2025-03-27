# Arma2AMP Mod Line converter
For those that run ArmA on an Application Managemnt Panel (AMP) server, then you know the pain of getting the Mod ID's, saving them, then copying to AMP.
You may also know that the syntax for the Workshop Mod line and the Server Mod Line is different.
Well this App will solve all those problems.

1. Generate a Mod list using the Arma3 Launcher.
2. Export that Mod list to HTML, ensuring that you only export the in use mod list.
3. Open this app and browse to the location of the Arma3 Launcher exported HTML file, then select the HTML file.
4. Select what mod line syntax file you want to generate.
5. Click "Generate".
6. Browse to the same folder as the exported HTML, you should find some new text files, with the requested Mod line syntaxes.
7. Copy those lines into the appropriate areas in AMP.

Note: In AMP, some mods are so large that they timeout during workshop (update) downloading. If you get a timeout in the SteamCMD log for a file, ensure you add another copy of that mod ID to the Workshop download mod line. This App is unable to determine Mod sizes, or you connection speed, and therefore unable to automatically cater for this scenario.
