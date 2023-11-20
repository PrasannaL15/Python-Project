# Python-Test-Harness
Prasanna Limaye plimaye@stevens.edu

Github URL : https://github.com/PrasannaL15/Python-Project

Hours Spend on the project : 35



# Automated Testing with `test.py`

This repository includes an automated testing script, `test.py`, designed to validate various functionalities within the codebase in the directory prog/. The script is structured to test three primary components:

## Testing Components

### Word Count Functionality (`wc.py`)

The `wc.py` script provides word count functionality with different flags (`-l`, `-w`, `-c`). Test cases cover:

- Multiple input files.
- Flags usage (-l, -w, -c).
- Standard input usage.

### JSON Formatter (`gron.py`)

The `gron.py` script converts JSON data to grepable format. Test scenarios include:

- Various input JSON files covering variety of test cases.
- Standard input usage.
- Formatting flag to provide base object using (--obj).

### Bulk Image Converter (`bic.py`)

The `bic.py` script handles bulk image conversions. Tests cover:

- Conversion of different image formats.
- specify the format required using -f format, the format can be webp, png, jpeg

## Running Tests

To run the tests:

1. Ensure Python 3.x is installed.
2. Navigate to the project directory.
3. Use following command to install all the required libraries 
   ```
   pip install -r requirements.txt
   ``` 
3. Execute the `test.py` script:

   ```bash
   python test.py



## There are no significant known bugs in this project

### The major issue faced was comparing the expected ouput and the output received from the subprocess. I have utilized difflib library to compare and check whether they are same or not. Another issue faced was of difference between ubuntu and windows file structure and problems arising from that.


### I have utilized following three extensions

1.  Extension: More advanced wc: multiple files

    You can provide multiple files to prog/wc.py and it will list down the output of each file and total.

    EXAMPLES :

    
    ```
        python prog/wc.py test/wc.test1.in test/wc.test1.in

    ```
    Output: 

           4       5      21 test/wc.test1.in
           8      10      42 test/wc.test1.in
          12      15      63 total
    
 
2.  Extension: More advanced wc: flags to control output

    You can provide flags (l, w, c) to get length, words or characters of the input file.
    You can also combine this with the multiple files 


    EXAMPLES:

    1. Only l flag
    ```
        python .\prog\wc.py -l test\wc.normal.in 
    ```                                                                       
    
    ``` 
    Output :

       3 test\wc.normal.in
    ```

    2. Only w falg
    ```
        python .\prog\wc.py -w test\wc.normal.in 
    ```
    
    ``` 
    Output :

      26 test\wc.normal.in
    ```

    3. with l and w flag
    ```
        python .\prog\wc.py -lw test\wc.normal.in 
    ```
    
    ``` 
    Output :

       3      26 test\wc.normal.in
    ```

    4. Only c flag
    ```
        python .\prog\wc.py -c test\wc.normal.in 
    ```
    
    ``` 
    Output :

     167 test\wc.normal.in
    ```

    5. with lwc flag 
    ```
        python .\prog\wc.py -lwc test\wc.normal.in 
    ```
    
    ``` 
    Output :
   
       3     26     167 test\wc.normal.in
    ```

    6. with lw flag and multiple files
    ```
        python .\prog\wc.py -lw test\wc.normal.in test\wc.test1.in 
    ```
    
    ``` 
    Output :

               3      26 test\wc.normal.in
               7      31 test\wc.test1.in
              10      57 total
    ```



3.  Extension: More advanced gron: control the base-object name

    You can specify the base object using --obj flag. This will change default json to the obj specified

    ```
        python .\prog\wc.py -lw test\wc.normal.in test\wc.test1.in 

    ```

    Output: 
    ```

        obj = {}
        obj.a = {}
        obj.a.232 = "Dddd"
        obj.a.d = 2323
        obj.menu = {}
        obj.menu.id = "file"
        obj.menu.popup = {}
        obj.menu.popup.menuitem = []
        obj.menu.popup.menuitem[0] = {}
        obj.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
        obj.menu.popup.menuitem[0].value = "New"
        obj.menu.popup.menuitem[1] = {}
        obj.menu.popup.menuitem[1].onclick = "OpenDoc()"
        obj.menu.popup.menuitem[1].value = "Open"
        obj.menu.popup.menuitem[2] = {}
        obj.menu.popup.menuitem[2].onclick = "CloseDoc()"
        obj.menu.popup.menuitem[2].value = "Close"
        obj.menu.value = "File"
    ```



