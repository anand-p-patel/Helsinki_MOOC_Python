#!/usr/bin/env python3

def file_extensions(filename):
    no_extensions = []
    extensions = {} #key is extension, value is list of files

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if "." not in line:
                no_extensions.append(line)
            else:
                parts = line.rsplit(".", 1)
                ext = parts[1]

                if ext in extensions:
                    extensions[ext].append(line)
                else:
                    extensions[ext] = [line]
    return (no_extensions, extensions)

def main():
    no_ext, exts = file_extensions("src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for ext in sorted(exts):
        print(f"{ext} {len(exts[ext])}")
    pass

if __name__ == "__main__":
    main()
