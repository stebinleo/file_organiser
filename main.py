import os
import shutil

# File type categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".sh"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organise(folder):
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    if not files:
        print("❌ No files found!")
        return

    print(f"\n📂 Organising: {folder}")
    print(f"📄 Total files found: {len(files)}\n")

    summary = {}

    for filename in files:
        ext = os.path.splitext(filename)[1]
        category = get_category(ext)

        dest_folder = os.path.join(folder, category)
        os.makedirs(dest_folder, exist_ok=True)

        src = os.path.join(folder, filename)
        dest = os.path.join(dest_folder, filename)

        shutil.move(src, dest)
        print(f"✅ {filename} → {category}/")

        summary[category] = summary.get(category, 0) + 1

    print("\n📊 Summary:")
    for category, count in summary.items():
        print(f"  {category}: {count} file(s)")

    print("\n🎉 Done!")
    
# Run
folder = input("Enter folder path to organise: ")
organise(folder)
