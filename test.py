import subprocess
import os
import shutil
from difflib import Differ


def my_diff(expected, actual):
    d = Differ()
    comparison = list(d.compare(expected.split(), actual.split()))
    print(comparison)
    print('\n'.join(comparison))


def run_cat(command):
    cat = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE)
    return cat


def run_command(command, stdin=None):
    result = subprocess.run(command.split(
        ' '), capture_output=True, text=True, stdin=stdin)
    return result


def test_wc(inputFile, outputFile, stdInOutputFile):
    result = run_command('python3 prog/wc.py '+inputFile)
    print(result) if inputFile == 'test/wc.test3.in' else None
    d = Differ()
    assert result.returncode == 0
    with open(outputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            my_diff(expected_output, result.stdout)
        assert result.stdout == expected_output
    cat_output = run_cat('cat '+inputFile)
    print(cat_output.stdout, "Cat output is")
    result = run_command('python3 prog/wc.py', stdin=cat_output.stdout)

    with open(stdInOutputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            print("resceived Result", result.stdout)
            print("expected Result", expected_output)
            my_diff(expected_output, result.stdout)

        assert result.stdout == expected_output


def test_gron(inputFile, outputFile, stdInOutputFile):
    result = subprocess.run(['python3', 'prog/gron.py', inputFile],
                            capture_output=True, text=True)
    assert result.returncode == 0
    with open(outputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            my_diff(expected_output, result.stdout)
        assert result.stdout == expected_output

    cat_output = run_cat('cat '+inputFile)
    result = subprocess.run(['python3', 'prog/gron.py'],
                            capture_output=True, text=True, stdin=cat_output.stdout)
    with open(stdInOutputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            my_diff(expected_output, result.stdout)

        assert result.stdout == expected_output


def test_bulk_webp_converter(inputFile):
    def test_webp_images(images, output):

        for image in images:
            path = os.path.join(output, image).replace('\\', '/')

            assert os.path.exists(path) == True
            assert path.endswith('.webp')
        return True

    if os.path.exists(inputFile+'/Output'):
        shutil.rmtree(inputFile+'/Output')

    result = subprocess.run(
        ['python3', 'prog/bic.py', '-f', 'webp', inputFile], capture_output=True, text=True)
    expected_Images = [filename for filename in os.listdir(
        inputFile+'/expected_output')]
    print(expected_Images)
    output_path = os.path.join(inputFile, 'Output').replace('\\', '/')

    assert result.returncode == 0
    assert test_webp_images(expected_Images, output_path) == True


if __name__ == '__main__':
    passed = {'wc': 0, 'gron': 0, 'bulk_webp_converter': 0}
    failed = {'wc': 0, 'gron': 0, 'bulk_webp_converter': 0}
    total = 0
    for filename in os.listdir('test'):
        print("Testing", filename)
        if filename.startswith('wc.') and filename.endswith('.in'):
            try:
                test_wc('test/'+filename, 'test/'+filename.replace('.in',
                        '.out'), 'test/'+filename.replace('.in', '.stdin.out'))
                passed['wc'] += 2
                total += 2
            except Exception as e:
                failed['wc'] += 1
                print('failed with error as ', e)

        elif filename.startswith('gron.') and filename.endswith('.in'):
            try:
                test_gron('test/'+filename, 'test/'+filename.replace('.in',
                          '.out'), 'test/'+filename.replace('.in', '.stdin.out'))
                passed['gron'] += 2
                total += 2
            except Exception as e:
                failed['gron'] += 1
                print('failed with error as ', e)

        elif filename.startswith('bic_test'):
            try:
                test_bulk_webp_converter('test/'+filename)
                # input('Press enter to continue')
                passed['bulk_webp_converter'] += 1
                total += 1
            except Exception as e:
                failed['bulk_webp_converter'] += 1
                print('failed with error as ', e)

    # test_wc('test/wc.test1.in','test/wc.test1.out','test/wc.test1.stdin.out')

    # Print nicely formatted total passed and failed
    print("Total Passed:")
    print("wc:", passed['wc'])
    print("gron:", passed['gron'])
    print("bulk_webp_converter:", passed['bulk_webp_converter'])
    print("Total Failed:")
    print("wc:", failed['wc'])
    print("gron:", failed['gron'])
    print("bulk_webp_converter:", failed['bulk_webp_converter'])

    if failed['wc'] != 0 or failed['gron'] != 0 or failed['bulk_webp_converter'] != 0:
        exit(1)
