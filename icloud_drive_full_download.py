from pyicloud import PyiCloudService
import os
import sys

# ================= CONFIG =================
APPLE_ID = "<your_apple_id>"
PASSWORD = "<your_password>"
DOWNLOAD_ROOT = "<your_download_directory>"  # e.g., "./iCloudDrive"
# =========================================


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_item(item, local_path):
    if item.type == "folder":
        os.makedirs(local_path, exist_ok=True)
        for child in item.get_children():
            download_item(child, os.path.join(local_path, child.name))
    else:
        if os.path.exists(local_path):
            return

        try:
            response = item.open(stream=True)
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            print(f"[OK] {local_path}")
        except Exception as e:
            print(f"[ERROR] {local_path} -> {e}")


def main():
    api = PyiCloudService(APPLE_ID, PASSWORD)

    # ===== 2FA =====
    if api.requires_2fa:
        print("2FA NEEDED")
        code = input("Enter 2FA Code: ").strip()
        if not api.validate_2fa_code(code):
            print("Wrong 2FA code")
            sys.exit(1)

    drive = api.drive
    root = drive.root

    ensure_dir(DOWNLOAD_ROOT)

    print("Starting download...\n")
    download_item(root, DOWNLOAD_ROOT)

    print("\nDone. All files are in folder:", DOWNLOAD_ROOT)


if __name__ == "__main__":
    main()
