from sample import sample_print

def test_sample(capsys):
    # run "poetry run pytest" on parent dir 
    sample_print()
    out, _ = capsys.readouterr()
    assert out == "sample!\n"