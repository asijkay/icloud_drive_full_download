# iCloud Drive Full Downloader (Python)

A Python script to download **all files and folders from iCloud Drive**, preserving the **original directory structure**, including **deeply nested folders (10+ levels)**.

This script is intended as a **workaround when Finder and iCloud.com fail** to download folders due to iCloud sync or backend issues.

---

## 🚀 Features

- ✅ Downloads **entire iCloud Drive**
- ✅ Preserves **original folder names & structure**
- ✅ Supports **deeply nested folders**
- ✅ **Resume support** (already-downloaded files are skipped)
- ✅ Handles **large files** using streamed downloads
- ✅ Works when Finder and iCloud Web UI are broken

---

## 📋 Requirements

- Python **3.8 or newer**
- macOS / Linux / Windows
- An iCloud account with **Two-Factor Authentication (2FA)**
- Sufficient local disk space to store iCloud Drive contents

---

## 📦 Installation

Install the required dependency:

```pip install pyicloud```

## Configuration

Edit the script and update the following variables:

```python
APPLE_ID = "your_icloud_email"
PASSWORD = "your_icloud_password"
DOWNLOAD_ROOT = "iCloud_Download"
```

### Security Warning

This script uses a **non-official, reverse-engineered API**.  
Use it at your own risk.  
Avoid using sensitive, work, or corporate Apple IDs.

---

## Usage

Run the script from your terminal:

```bash
python icloud_drive_full_download.py
```

If Two-Factor Authentication (2FA) is enabled, you will be prompted to enter the verification code sent to your trusted device.

---

## Output Structure

Downloaded files will be saved locally using the same structure as iCloud Drive:

```
iCloud_Download/
├── FolderA/
│   ├── SubFolder1/
│   │   └── SubFolder2/
│   │       └── file.ext
├── FolderB/
└── file.pdf
```

The directory hierarchy exactly matches your iCloud Drive, including deeply nested folders.

---

## Resume Support

If the script is interrupted due to:

- network failure  
- system sleep or reboot  
- manual termination  
- script crash  

Simply run the script again:

```bash
python icloud_drive_full_download.py
```

Already downloaded files will be skipped automatically, and the script will continue from where it stopped.

---

## Notes and Limitations

- This script does **not** download:
  - iCloud Photos
  - iPhone or iPad backups
  - iCloud Mail, Contacts, or Calendars
- Accounts with many small files may take a long time to complete
- Apple may temporarily apply rate limiting or throttling

---

## Troubleshooting

### Response object has no attribute read

This error occurs when treating a Response object as a file object.  
The script avoids this issue by using streamed downloads via iter_content.

---

### Folder downloads fail in Finder or iCloud.com

This is commonly caused by an iCloud backend synchronization issue.  
The script bypasses Finder’s sync engine and often succeeds when the Apple UI fails.

---

## Disclaimer

This project uses reverse-engineered iCloud APIs and is **not affiliated with or endorsed by Apple Inc.**

Use responsibly and entirely at your own risk.

---

## License

MIT License

---

## Acknowledgements

- pyicloud — reverse-engineered iCloud API access
