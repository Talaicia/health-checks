#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")	
    pass
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything is fine.")
    sys.exit(0)
main()
