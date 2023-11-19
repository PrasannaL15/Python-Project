import subprocess
import os
import shutil
from difflib import Differ


def my_diff(expected, actual):
    d = Differ()
    comparison = list(d.compare(expected.split(), actual.split()))
    delta = ''.join(x[2:] for x in comparison if x.startswith('- ') or x.startswith('+ '))
    # print(comparison)
    print('delta is')
    print('\n'.join(comparison))


def run_cat(command):
    try:
        cat = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE)
        return cat

    except:
        raise Exception('e')
    

def run_command(command, stdin=None):
    result = subprocess.run(command.split(
        ' '), capture_output=True, text=True, stdin=stdin)
    return result


def test_wc(inputFile, outputFile, stdInOutputFile,lFlagOutputFile= None,wFlagOutputFile =None, cFlagOutputFile = None):
    global passed

    result = run_command('python3 prog/wc.py '+inputFile)
    assert result.returncode == 0 , result.stderr
    with open(outputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            print("without flag",inputFile)
            print("resceived Result", result.stdout)
            print("expected Result", expected_output)
            my_diff(expected_output, result.stdout)
        assert result.stdout == expected_output
    passed['wc']+=1

    if lFlagOutputFile and  os.path.exists(lFlagOutputFile) :
        result = run_command('python3 prog/wc.py -l '+inputFile)
        assert result.returncode == 0 , result.stderr
        with open(lFlagOutputFile, 'r') as f:
            expected_output = f.read()
            if result.stdout != expected_output:
                print("with l flag",inputFile)
                print("resceived Result", result.stdout)
                print("expected Result", expected_output)
                my_diff(expected_output, result.stdout)
            assert result.stdout == expected_output
        passed['wc']+=1
        
    if wFlagOutputFile and  os.path.exists(wFlagOutputFile) :
        result = run_command('python3 prog/wc.py -w '+inputFile)
        assert result.returncode == 0 , result.stderr
        with open(wFlagOutputFile, 'r') as f:
            expected_output = f.read()
            if result.stdout != expected_output:
                print("with w flag",inputFile)
                print("resceived Result", result.stdout)
                print("expected Result", expected_output)
                my_diff(expected_output, result.stdout)
            assert result.stdout == expected_output
        passed['wc']+=1
            
    if cFlagOutputFile and  os.path.exists(cFlagOutputFile) :
        result = run_command('python3 prog/wc.py -c '+inputFile)
        assert result.returncode == 0 , result.stderr
        with open(cFlagOutputFile, 'r') as f:
            expected_output = f.read()
            if result.stdout != expected_output:
                print("with c flag",inputFile)
                print("resceived Result", result.stdout)
                print("expected Result", expected_output)
                my_diff(expected_output, result.stdout)
            assert result.stdout == expected_output    
        passed['wc']+=1
    
    
    cat_output = run_cat('cat '+inputFile)
    



    result = run_command('python3 prog/wc.py', stdin=cat_output.stdout)

    with open(stdInOutputFile, 'r') as f:
        expected_output = f.read()
        if result.stdout != expected_output:
            print("resceived Result", result.stdout)
            print("expected Result", expected_output)
            my_diff(expected_output, result.stdout)

        assert result.stdout == expected_output
    passed['wc']+=1
    

def test_gron(inputFile, outputFile,flag =None):
    global passed
    
    result = subprocess.run(['python3', 'prog/gron.py', inputFile],
                            capture_output=True, text=True)
    
    if flag is not None:
        result = subprocess.run(['python3', 'prog/gron.py', '--obj',flag,inputFile],
                            capture_output=True, text=True)
    
    assert result.returncode == 0, result
    with open(outputFile, 'r') as f:
        expected_output = f.read()

        if result.stdout != expected_output:
            print("expected output is ",expected_output)
            print("actual output is ", result.stdout)

            my_diff(expected_output, result.stdout)
        assert result.stdout == expected_output
    passed['gron']+=1

def test_bulk_webp_converter(inputFile,format):
    global passed 

    def test_webp_images(images, output,format):

        for image in images:
            path = os.path.join(output, image).replace('\\', '/')
            assert os.path.exists(path) == True, path
            assert path.endswith(format) , path+format
        return True

    if os.path.exists(inputFile+'/Output'):
        shutil.rmtree(inputFile+'/Output')

    result = subprocess.run(
        ['python3', 'prog/bic.py', '-f', format, inputFile], capture_output=True, text=True)
    expected_Images = [filename for filename in os.listdir(
        inputFile+'/expected_output')]
    # print(expected_Images)
    output_path = os.path.join(inputFile, 'Output').replace('\\', '/')

    assert result.returncode == 0, result.stderr
    assert test_webp_images(expected_Images, output_path, format) == True, 'Conversion is not correct'
    passed['bulk_image_converter']+=1
# filename = 'gron.test1.in'
# test_gron('test/'+filename, 'test/'+filename.replace('.in',
#                           '.out'))

# exit(1)

passed = {'wc': 0, 'gron': 0, 'bulk_image_converter': 0}
failed = {'wc': 0, 'gron': 0, 'bulk_image_converter': 0}
total = 0
    


if __name__ == '__main__':
    for filename in os.listdir('test'):
        
        if filename.startswith('wc.') and filename.endswith('.in') and not filename.endswith('l.in') and not filename.endswith('w.in') and not filename.endswith('c.in'):
            print("Testing", filename)
            try:
                test_wc('test/'+filename, 'test/'+filename.replace('.in',
                        '.out'), 'test/'+filename.replace('.in', '.stdin.out'),'test/'+filename.replace('.in', '.l.out'),'test/'+filename.replace('.in', '.w.out'),'test/'+filename.replace('.in', '.c.out'))
            except AssertionError or Exception as e:
                failed['wc'] += 1
                print('failed with error as ', e)

        elif filename.startswith('gron.') and filename.endswith('.in') and '-' not in filename:
            print("Testing", filename)
            
            try:
                test_gron('test/'+filename, 'test/'+filename.replace('.in',
                          '.out'),)
            
            except AssertionError or Exception as e:
                failed['gron'] += 1
                print('failed with error as ', e)
        elif filename.startswith('gron.') and filename.endswith('.out') and '-'  in filename:
            print("Testing json with", filename)
            infilename = filename.split('-')[0]
            outputfilename = filename
            flag = filename.split('-')[1]
            flag = flag.split('.')[0]

            try:
                test_gron('test/'+infilename+'.in', 'test/'+outputfilename,flag)
            
            except AssertionError or Exception as e:
                failed['gron'] += 1
                print('failed with error as ', e)
            

        elif filename.startswith('bic_test'):
            print("Testing", filename)
            format = filename.split('-')[1]
            try:
                test_bulk_webp_converter('test/'+filename,format)
                # input('Press enter to continue')
            except AssertionError or Exception as e:
                failed['bulk_image_converter'] += 1
                print('failed with error as ', e)

    # test_wc('test/wc.test1.in','test/wc.test1.out','test/wc.test1.stdin.out')

    # Print nicely formatted total passed and
    total = sum([value for key,value in passed.items()]) + sum([value for key,value in failed.items()])  
    print("Total Tests Performed:", total)
    print("Total Passed:")
    print("wc:", passed['wc'])
    print("gron:", passed['gron'])
    print("bulk_image_converter:", passed['bulk_image_converter'])
    
    print("Total Failed:")
    print("wc:", failed['wc'])
    print("gron:", failed['gron'])
    print("bulk_image_converter:", failed['bulk_image_converter'])

    if failed['wc'] != 0 or failed['gron'] != 0 or failed['bulk_image_converter'] != 0:
        exit(1)
