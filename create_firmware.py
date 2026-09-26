#!/usr/bin/env python3
"""Standalone runner for Xiaomi Flashable Firmware Creator.

Automatically installs required Python packages (protobuf, remotezip) if missing,
then runs Xiaomi Flashable Firmware Creator.
"""

import subprocess
import sys
from pathlib import Path


def ensure_dependencies():
    try:
        import google.protobuf  # noqa: F401
        import remotezip  # noqa: F401
    except ImportError:
        print("Installing required Python dependencies (protobuf, remotezip)...")
        req_file = Path(__file__).parent / "requirements.txt"
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])


if __name__ == "__main__":
    ensure_dependencies()
    from xiaomi_flashable_firmware_creator.xiaomi_flashable_firmware_creator import main

    main()
