import subprocess
import os
import shutil
from difflib import Differ

def my_diff(expected, actual):
    d = Differ()
    comparison = list(d.compare(expected.split(), actual.split()))
    print(''.join(comparison))
    

def run_cat(command):
    cat = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE)
    return cat

def run_command(command,stdin=None):
    result = subprocess.run(command.split(' '), capture_output=True, text=True, stdin=stdin)
    return result



def test_wc(inputFile,outputFile,stdInOutputFile):
    result = run_command('python prog/wc.py '+inputFile)
    d = Differ()
    assert result.returncode == 0
    with open(outputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            my_diff(expected_output, result.stdout)
        assert result.stdout == expected_output     
    cat_output = run_cat('cat '+inputFile)
    result = run_command('python prog/wc.py',stdin=cat_output.stdout)
    
    with open(stdInOutputFile,'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            my_diff(expected_output, result.stdout)  
            
        assert result.stdout == expected_output

def test_gron():
    result = subprocess.run(['python', 'prog/gron.py', 'eg.json'],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert 'json' in result.stdout


def test_bulk_webp_converter():
    def test_webp_images(images, output):

        for image in images:
            path = os.path.join(output, image).replace('\\', '/')
            
            assert os.path.exists(path) == True
            assert path.endswith('.webp')
        return True

    if os.path.exists('Images/Output'):
        shutil.rmtree('Images/Output')

    result = subprocess.run(
        ['python', 'prog/bulk_webp_converter.py', '-f', 'webp', 'Images/'], capture_output=True, text=True)
    expected_Images = ['ID.webp', 'linkedinLogo.webp']

    output_path = os.path.join('Images', 'Output').replace('\\', '/')
    assert result.returncode == 0
    assert test_webp_images(expected_Images, output_path) == True


if __name__ == '__main__':
    
    test_wc('test/wc.test1.in','test/wc.test1.out','test/wc.test1.stdin.out')
    test_gron()
    test_bulk_webp_converter()
