# i3autotile

Uses the i3 socket to register a hook which changes the direction a
window splits based on its widest part.

install: `python setup.py install`

run: `i3autotile`

It will try to reconnect to the socket when losing connection, with a
1 second delay. may run indefinitely.
