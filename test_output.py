import pytest
def test_output(capsys):
    print("hello")
    out, err = capsys.readouterr()
    assert out == "hello\n"