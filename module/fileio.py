def list_to_file(filepath: str, lines: list):
    with open(filepath, "w", encoding="UTF-8") as writefile:
        for line in lines:
            print(line)
            line = line + "\n"
            writefile.write(line)

