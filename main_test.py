from main import main


def test_positive(capsys, monkeypatch):
    inputs = iter([28, 52100])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Wir sind in der Lage, Ihnen einen Kredit anzubieten.\n'

def test_young(capsys, monkeypatch):
    inputs = iter([20, 135750])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Leider können wir Ihnen zur Zeit keinen Kredit anbieten.\n'


def test_income(capsys, monkeypatch):
    inputs = iter([68, 46500])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Leider können wir Ihnen zur Zeit keinen Kredit anbieten.\n'