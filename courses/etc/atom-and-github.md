# Atom and GitHub

## What is Atom?
[Atom](http://atom.io) is a text editor. Meaning all it really does is allow you to edit text files. This sounds limiting but if you've ever been frustrated waiting a few minutes for Word to open just so you can see a paragraph of text, you already understand why people use text editors. Or if you copied and pasted from something into a Word document and then had to spend a few minutes fixing formatting, font size, etc, you also know why text editors are great tools.


## Why use Atom
You already know about writing directly on GitHub and in Dillinger. Many of you write in Word and then copy and paste to one of these platforms. It works fine. What's the point of another method?

### Speed
Text editors like Atom are super fast, and they do everything you need for this course that Word can do, like Word counts and Spell check. They are also faster in the sense you can see your and your colleagues' posts, and make new posts, WAY MORE EASILY.


### Markdown Preview
Especially when learning Markdown, it's nice to see if you're using the right codes. With Atom, you don't need to use an external tool like Dillinger. You can also preview your Markdown as you write through the menu `Packages`->`Markdown Preview`->`Toggle Preview`.

If you need syntax help, remember the [cheat sheet](https://www.markdownguide.org/cheat-sheet).


### Integrated posting
You're all used to posting work on UNM Learn or maybe elsewhere, but it's always easier when your writing tool and publication platform can talk to each other. Atom and GitHub can be paired together so you can immediately post your work to GitHub without having to cut and paste text or drag and drop files.


## Connecting Atom to GitHub
There are a few steps to get connected that you only have to do once. Essentially, you'll be making a copy of our repository on your own computer.
- In Atom, open the Command Palette window by selecting `View` -> `Toggle Command Palette`
- Type in `Clone`, and pick the first option, `Github: Clone`
- In the `Clone from` prompt, enter `https://github.com/unm-historiography/2021-fall.git`
- You can see that you must specify a directory where all the files from our repository will be copied. You can pick any directory on your computer, or just accept the default (recommended).
- Press the `Clone` button
- At this point, GitHub wants to make sure that you are authorized to make changes in our repository. So Atom will tell you to visit `github.atom.io/login` and log in with your GitHub credentials. Then you'll get the special code/token from GitHub that you need to relay to Atom. You've all done this sort of thing before.
- Once you're connected to GitHub, you will see all the folders and files from our repository on the left Project pane.
- You're done connecting and you never have to do any of these steps again.

## Creating a new file
When you want to write a new reflection, right-click on the folder to which you want to add your file, and Click `New File` (or you can just highlight the folder and Press A). Name your file according to the usual conventions (all lower case, with a `.md` extension).

## Writing
It's just text! So fast!! So Easy!!! Remember you can preview your Markdown as you write through the menu `Packages`->`Markdown Preview`->`Toggle Preview`. Save often.

## Posting
When you're ready to commit your file to our repository, you're just a few clicks away.

- Click the `Git` link/label (NOT GITHUB) in the lower right of your Atom window.

- Double-click your file from the `Unchanged Changes` tab. You see it moves to the `Staged Changes` pane.

- In the text box that has a grayed out `Commit message`, enter a description of your changes (like `create file`).

- Click the big blue `Commit to main` button.

- Click the small `Push` link on the bottom of the Atom window. You're done!

If you're paranoid like me, you can double check that your post is in our repository at GitHub. But unless you got some weird error message, it will be there.
