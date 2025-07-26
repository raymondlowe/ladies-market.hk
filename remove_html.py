import os
import shutil



# Remove .private and .github folders in current directory if they exist
for folder in ['.private', '.github']:
    folder_path = os.path.join(os.getcwd(), folder)
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted {folder} folder: {folder_path}")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Failed to delete {folder} folder: {e}")

filenames = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.htm'):
            filenames.append(os.path.join(root, file))

print(f"Found {len(filenames)} html files in current directory")
print(*filenames, sep="\n")

for filename in filenames:
    try:
        print("Read file", filename)
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        if ".htm" in text:
            print("Found .htm or .html in", filename)

            text = text.replace(".html", "")
            text = text.replace(".htm", "")

        with open(filename, "w", encoding="utf-8") as f:
            print("Write file", filename)
            f.write(text)
    except:
        print("failed ", filename)

