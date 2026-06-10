# slashphabet [description]
Simple and secret-oriented encoding method built on Python.

## what's slashphabet?
Read the description again. Alright, jokes aside, it's a simple encoding method built for secrets, especially ARGs (wink wink), that uses just 5 characters - `[`, `]`, `\`, `/`, and `.`.

Slashphabet is awful for saving storage as it, instead of shortening, makes each character be from 3 to 8 times longer.

It does NOT change digits or special characters - only letters. Y'know, slash**phabet**. Like an alphabet, but slashes.

It was made with Python 3.14.

For a Linux build, hell no. Coming from a Linux user. Just use the raw script, it's right there, god dammit.

# questions that will probably be asked
## what are possible use cases, since it doesnt save storage?
ARGs, secrets, just anything outside of saving storage, to be completely honest.

## what libraries does it use?
It only uses the `sleep` function from `time`, so there are no additional dependencies except for the `slashdata.py` file.

## i'm a linux user, what do i do?
```bash
cd ~/path/to/slash.py
python3 slash.py
```
That's it. Replace `~/path/to/slash.py` with your actual path, obviously.

## slash.py doesn't work. what's the issue?
You probably didn't download `slashdata.py` next to it. `slashdata.py` contains all the letter definitions, so it is required.

## was this inspired by brainfuck?
Yes, it was.

## is there any copyright?
I mean, I don't care. Maybe mention it in the media you're using my thingy on, but it's not necessary, really.
