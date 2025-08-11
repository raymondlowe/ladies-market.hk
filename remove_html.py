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

        import re
        basename = os.path.basename(filename)
        # Special case: preserve .html in google-site-verification files
        if basename.startswith("google") and basename.endswith(".html"):
            lines = text.strip().splitlines()
            if len(lines) == 1 and re.match(r"^google-site-verification: google.*\.html$", lines[0]):
                print(f"Special case: preserving .html in {filename}")
                # Do not modify text
                continue

        # Only remove .htm/.html from href attributes ending with double quotes
        def remove_html_from_href(match):
            url = match.group(1)
            url = re.sub(r"(\.html|\.htm)$", "", url)
            return f'href="{url}"'

        new_text = re.sub(r'href="([^"]*?\.(?:html|htm))"', remove_html_from_href, text)

        with open(filename, "w", encoding="utf-8") as f:
            print("Write file", filename)
            f.write(new_text)
    except:
        print("failed ", filename)

