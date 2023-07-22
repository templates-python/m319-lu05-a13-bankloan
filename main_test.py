from main import main


def test_bar(capsys, monkeypatch):
    inputs = iter([3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'The number is positive.\n'
