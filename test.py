import subprocess
import os
import shutil


def test_wc():
    result = subprocess.run(['python', 'wc.py', 'requirements.txt'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == '       3       8      31 requirements.txt\n'


def test_gron():
    result = subprocess.run(['python', 'gron.py', 'eg.json'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert 'json' in result.stdout


def test_bulk_webp_converter():
    def test_webp_images(images, output):

        for image in images:
            path = os.path.join(output, image).replace('\\', '/')
            print(path)
            print(os.path.abspath(path))
            assert os.path.exists(path) == True
            assert path.endswith('.webp')
        return True

    if os.path.exists('Images/Output'):
        shutil.rmtree('Images/Output')

    result = subprocess.run(
        ['python', 'bulk_webp_converter.py', '-f', 'webp', 'Images/'], capture_output=True, text=True)
    expected_Images = ['ID.webp', 'LinkedinLogo.webp']

    output_path = os.path.join('Images', 'Output').replace('\\', '/')
    assert result.returncode == 0
    assert test_webp_images(expected_Images, output_path) == True


if __name__ == '__main__':
    print(os.path.exists('Images'))
    test_wc()
    test_gron()
    test_bulk_webp_converter()
