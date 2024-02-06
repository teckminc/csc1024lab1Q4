import lab1q4
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('54.3\n67.12\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q4.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{3644.62}') != -1
    assert captured_stdout.strip().find(f'{122313.31}') != -1