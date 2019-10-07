
def high_score(current_score: int, file_name: str):
    with open(file_name, "r") as f:
        content = f.read()
    
    num = int(content.strip())

    if current_score > num:
        with open(file_name, "w") as f:
            f.write(str(current_score))


high_score(98, "high_score.txt")