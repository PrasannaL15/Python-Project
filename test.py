import subprocess


def test_wc():
    result = subprocess.run(['python', 'wc.py', 'test.txt'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Words: ' in result.stdout
    assert 'Lines: ' in result.stdout
    assert 'Characters: ' in result.stdout


def test_gron():
    result = subprocess.run(['python', 'gron.py', 'test.json'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert 'json' in result.stdout


def test_bulk_webp_converter():
    result = subprocess.run(
        ['python', 'bulk_webp_converter.py', '--webp', 'Images/'], capture_output=True, text=True)
    assert result.returncode == 0


if __name__ == '__main__':
    test_wc()
    test_gron()
    test_bulk_webp_converter()
