def compress(path_input, path_output):
    fr = open(path_input, mode="r")
    fw = open(path_output, mode="w")

    lines = fr.readlines()
    dimensions = [x for x in lines[0].split()]
    result = " ".join(dimensions) + "\n"

    for line in lines[1:]:
        char = "0"
        count = 0
        line_compressed = []
        for cc in line:
            if char == cc:
                count += 1
            else:
                char = cc
                line_compressed.append(str(count))
                count = 1
        result += " ".join(line_compressed) + "\n"

    fw.write(result)
    fr.close()
    fw.close()


compress("kompresia1.txt", "kompresia2.txt")
