iCloud Drive Full Downloader (Python)

This script downloads all files and folders from iCloud Drive, preserving the full nested folder structure (tested with deeply nested folders, 10+ levels).

It is designed as a workaround when Finder and iCloud.com fail to download folders.

Features

✅ Downloads entire iCloud Drive

✅ Preserves original folder names & structure

✅ Supports deeply nested folders

✅ Resume support (already downloaded files are skipped)

✅ Handles large files via streaming

✅ Works even when Finder / iCloud web UI is broken

Requirements

Python 3.8+

macOS, Linux, or Windows

An iCloud account with 2FA enabled

Sufficient local disk space

Installation

Install the required library:

pip install pyicloud

Configuration

Edit the script and set your credentials:

APPLE_ID = "your_icloud_email"
PASSWORD = "your_icloud_password"
DOWNLOAD_ROOT = "iCloud_Download"


⚠️ Security note
This uses a non-official library.
Use at your own risk and avoid corporate / sensitive accounts.

Usage

Run the script:

python icloud_drive_full_download.py


If Two-Factor Authentication is enabled, you will be prompted to enter the verification code.

Output Structure

The downloaded files will appear in:

iCloud_Download/
├── FolderA/
│   ├── SubFolder1/
│   │   └── SubFolder2/
│   │       └── file.ext
├── FolderB/
└── file.pdf


The structure matches iCloud Drive exactly.

Resume Support

If the script:

crashes

is interrupted

loses internet connection

Simply run it again:

python icloud_drive_full_download.py


Existing files will be skipped automatically, and the download will continue.

Notes & Limitations

This script does NOT download:

iCloud Photos

iPhone backups

iCloud Mail or Contacts

Large accounts with many small files may take a long time

Apple may temporarily throttle requests

Troubleshooting
'Response' object has no attribute 'read'

This is already handled in the script by using streamed downloads (iter_content).

Folder appears stuck or empty

This is usually an Apple iCloud backend issue

The script bypasses Finder sync and often succeeds where the UI fails

Disclaimer

This project uses reverse-engineered APIs and is not affiliated with Apple.

Use responsibly.

License

MIT License
