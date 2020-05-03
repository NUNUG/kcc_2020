# Kids Code Camp 2020 - Python
This is where you will find the source code and materials for the Python game, Gobbler.

## About the game

### Description


### GamePlay


## About the software

### The software stack
The software stack is what we call the list of software technologies and libraries we use to build a system.  Here is the stack that I used for Ultimate Fiction.  They are all free except for Rytmik:

- `Python 3.x` programming interpeter and runtime libraries
- `Visual Studio Code` code editgor
- `PyGame` game framework
- `Tiled` map editor
- `pyTMX` library for working with Tiled maps
- `Paint.NET` for graphics
- `Audacity` for sound
- `Rytmik` for music (not free - you could try Magix Music Maker Free instead)

### Installation Instructions for the MonoGame Class
If you just want to work through the class and write the code, you can follow these simpler installation instructions.

- Download and install Visual Studio 2019 Community Edition for your platform.  Be sure to install .NET Core 3.x support when it asks which components you want.
- Download and install MonoGame 3.7.1.


### Installation instructions for making your own games.
If you want to work through the class but also want to try making your own games at the end, you will need the coding tools listed in the section above but you will also need a few more programs to make your own game assets (graphics and sound).

- Download and install Visual Studio 2019 Community Edition for your platform.  Be sure to install .NET Core 3.x support when it asks which components you want.
- Download and install MonoGame 3.7.1.
- Download the latest version of Paint.NET.  Be careful when doing this.  The paint.net web site is FULL of tricky "Download now!" ads that you don't want to click.  Use this direct link ONLY for safety. `https://www.dotpdn.com/files/paint.net.4.2.10.install.zip`
- Install Paint.Net.  From your browser, find the downloaded file in the bottom of the window (Try Ctrl-J if it's not there).  If you still can't find it, try going to your downloads folder and find the paint.net.4.2.10.install.zip file.  Open the zip file and run the .EXE installer file that's inside of it.
- Download and install the latest version of Tiled map editor (`mapeditor.org`).
- Download and install the latest version of Audacity audio editor (`audacityteam.org`).

For this game, you will use the source code that I provide at GitHub.  To make your own games, you can create a new game using a MonoGame Template.
- First install the templates from the command line like this:
```
dotnet new --install MonoGame.Templates.CSharp
```
- When you are ready, you can see the templates like this:
```
dotnet new --list | FIND "MonoGame"
```

On my machine, these are the templates that were installed.
```
Description                                                 Short Name
----------------------------------------------------------------------
MonoGame Android Application                                mgandroid
MonoGame Cross-Platform Desktop Application (OpenGL)        mgdesktopgl
MonoGame iPhone/iPad Application                            mgios
MonoGame Windows Universal Application (CoreApp)            mguwpcore
MonoGame Windows Universal Application (XAML)               mguwpxaml
MonoGame Windows Desktop Application (Windows DirectX)      mgwindowsdx
MonoGame NetStandard Library                                mgnetstandard
MonoGame Pipeline Extension                                 mgpipeline
MonoGame Shared Library Project                             mgshared
```

For the class, we are using the mgdesktopgl template because it will run on both Mac and Windows.  If you want to make a game just for Windows, you can use the mgwindowsdx template.  If you want to make a mobile game, try the gmandroid or mgios templates.

To create a new empty game:
- Open a command line or terminal
- Create a new directory for your game
- Inside the game directory, run this command to create a new game project.

```
dotnet new <template-short-name> -o <game-name>
```

For example, to create the game for our class, I used this command line:
```
dotnet new mgdesktopgl -o fiction
```
You should now have a new folder with a .csproj file in it.  Your directory structure should look like this:

```
<game-root-directory>
	<mygame-project-directory>
		mygame.csproj
```

You can now open the mygame.csproj file in Visual Studio.  Save the solution file in the game root directory, one level up from the .csproj file.

Create a directory in the root direcotry called `assets`.  Inside it, create `graphics`, `sounds` and `tiles` folders.

It should all look like this:

```
<game-root-directory>
	mygame.sln
	<assets>
		<graphics>
		<sounds>
		<tiles>
	<mygame-project-directory>
		mygame.csproj
```

You could also start with the "step 1" state of the Ultimate Fiction game.  It is effectivel an empty project.  You could also use the directory structure as a guide to verify that you did everything correctly when creating your own new game.

## About the Class

The class comprises 3 aspects.
- There are instructional videos for you to watch.  There are videos for setting everything up, videos for the game building and possibly some supplemental videos.
- There is source code for each step along the way that has been typed out for you.  If you don't want to type it, use the source code.  If you mess something up and don't know where the problem is, use the source code to figure it out.
- There is a RESET program.  This is a convenient way to switch between each of the steps in the instructional videos.  If you ever have a problem typing out the code, you can use the RESET program to move to the next step, or to the previous step so you can try again.

### Instructional Videos

I have produced the following vieos (subject to last-minute change):
- Windows setup instructions
- Mac setup instructions
- Tiled instructional video
- Paint.NET instructional video
- Audacity instructional video
- RESET program instructional video
- Game Coding instructional video

### Getting Help

TODO: Write me.