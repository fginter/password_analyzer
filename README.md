# password_analyzer

Code for analyzing leaked passwords. A project with A&K. This will hardly be useful to anyone else. But you never know. ;)

# Prerequisites

To run the whole thing, you need simstring. Grab it from GitHub https://github.com/chokkan/simstring

When installing the Python bindings, you should have swig and you should call `./prepare.sh --swig`

# Running (on epsilon at least)

```
./index_vocab.sh
cat /usr/share/ParseBank/PasswordData/orig/78k-all-passwords.txt | python lookup_matches.py
```
