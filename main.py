
# random function to test
# intentionally contains error, lets fix it via GH

def say_my_name(file:str) -> None:
    with open(file, "r") as f:
        file_lines = f.readlines()
        for row in file_lines:
            if row.startswith(" - "):
                print(f"Hello {row.split(' ')[2]}")

say_my_name("readme.md")