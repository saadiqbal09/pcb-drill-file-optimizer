from dataclasses import dataclass

@dataclass
class DrillPoint:
    x: float
    y: float
    tool: str


def parse_drill_file(path):
    tools = {}
    points = []
    current_tool = None

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("T") and "C" in line:
                tool, size = line.split("C")
                tools[tool] = float(size)

            elif line.startswith("T") and "C" not in line:
                current_tool = line

            elif line.startswith("X") and "Y" in line:
                x = float(line.split("Y")[0][1:]) / 1000
                y = float(line.split("Y")[1]) / 1000
                points.append(DrillPoint(x, y, current_tool))

    return tools, points
