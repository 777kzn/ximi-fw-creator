# Xiaomi Flashable Firmware Creator

Create flashable firmware `.zip` files from official Xiaomi, Redmi, and POCO ROMs (MIUI, HyperOS 1, HyperOS 2, and HyperOS 3+).

## Quick Start (Only 2 Commands!)

### Option 1: Install Directly

**1. Download & install everything:**

    pip install git+https://github.com/777kzn/ximi-fw-creator.git

**2. Create the flashable firmware zip:**

    python -m xiaomi_flashable_firmware_creator -F "C:\path\to\rom.zip"

---

### Option 2: Clone Repo & Run Directly

**1. Clone the repository:**

    git clone https://github.com/777kzn/ximi-fw-creator.git ; cd ximi-fw-creator

**2. Create the flashable firmware zip** *(automatically installs Python dependencies if missing)*:

    python create_firmware.py -F "C:\path\to\rom.zip"

---

## Supported Flags

| Flag | Long Option | Description |
| :--- | :--- | :--- |
| `-F` | `--firmware` | Create **normal Firmware** zip (most common) |
| `-N` | `--nonarb` | Create **non-ARB Firmware** zip |
| `-L` | `--firmwareless` | Create **Firmware-less ROM** zip |
| `-V` | `--vendor` | Create **Firmware + Vendor** zip |
| `-o` | `--output` | Specify custom output directory (optional) |

### Examples

    # Generate normal flashable firmware in the current directory
    python -m xiaomi_flashable_firmware_creator -F "C:\Downloads\codename_global-ota_full-OS3.0.302.0.WOJMIXM-user-16.0-4d30b0b284.zip"

    # Generate normal flashable firmware into a specific output folder
    python -m xiaomi_flashable_firmware_creator -F "C:\Downloads\rom.zip" -o "C:\Downloads"

    # Generate directly from a remote ROM URL without downloading the entire ROM zip
    python -m xiaomi_flashable_firmware_creator -F "https://example.com/rom.zip"

## Credits & License
Based on [xiaomi-flashable-firmware-creator.py](https://github.com/XiaomiFirmwareUpdater/xiaomi-flashable-firmware-creator.py) by [XiaomiFirmwareUpdater](https://github.com/XiaomiFirmwareUpdater). Licensed under GPL-3.0.
