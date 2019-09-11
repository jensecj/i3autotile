import sys
import os
import subprocess
import time

import i3ipc


def get_socket():
    try:
        # just grab the socket from the running i3 process, this fixes
        # the issue with the envvar sometimes not being updated to the
        # correct socket after restarting i3 in-place
        cmd = subprocess.run(["i3", "--get-socketpath"], stdout=subprocess.PIPE)
        return str(cmd.stdout, "utf-8", "ignore").strip(), None
    except Exception as err:
        return None, err


def connect(socket):
    try:
        return i3ipc.Connection(socket_path=socket), None
    except Exception as err:
        return None, err


def on_window_focus(i3, _event):
    wnd = i3.get_tree().find_focused()

    # only split splittable windows (layout is splith/v)
    if not wnd or not wnd.rect or wnd.layout in ["stacked", "tabbed"]:
        return

    # split along the widest part of the window
    if wnd.rect.height > wnd.rect.width:
        i3.command("split vertical")
    else:
        i3.command("split horizontal")


def main():
    while True:
        time.sleep(1)

        socket, err = get_socket()
        if not socket:
            print(f"unable to find i3 socket: {err}")

        print(f"found i3 socket: {socket}")

        i3, err = connect(socket)

        if not i3:
            print(f"unable to connect to i3 socket: {err}")
            sys.exit(1)

        print("connected to socket")

        print("registering window focus hook")
        i3.on(i3ipc.Event.WINDOW_FOCUS, on_window_focus)

        try:
            i3.main()
        except Exception as err:
            print(f"ERROR: {err}")

        print("lost socket connection, retrying...")


if __name__ == "__main__":
    main()
