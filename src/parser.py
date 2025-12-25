def parse_drill_file(path):
    tools = {}
    coordinates = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            # Tool definition (example: T01C0.8)
            if line.startswith("T") and "C" in line:
                tool, size = line.split("C")
                tools[tool] = float(size)

            # Coordinate line (example: X012345Y067890)
            elif line.startswith("X") and "Y" in line:
                x_part = line.split("Y")[0][1:]
                y_part = line.split("Y")[1]
                coordinates.append((x_part, y_part))

    return tools, coordinates
