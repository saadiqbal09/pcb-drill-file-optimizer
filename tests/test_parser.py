from src.parser import parse_drill_file

def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.drl"
    file_path.write_text("")

    tools, points = parse_drill_file(file_path)

    assert tools == {}
    assert points == []
