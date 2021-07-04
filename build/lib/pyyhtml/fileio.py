def write_list_to_file(filepath: str, content: list):
    with open(filepath, "w", encoding="UTF-8") as writefile:
        writefile.write("<!doctype html>\n")
        for line in content:
            writefile.write(line + "\n")