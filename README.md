# cheatingAPI
This will be used on 12th Feb 2024 to get answers directly into the CLI@TINT_Computer_Lab during python practical!


**Usage:**
Verification....
*step 1* : Verify the python installation using cmd.
  + Linux : `python3 --version` (if not installed install it by using `sudo apt install python3`)
  + Windows : `python --version` (You can go to the python official website an download the executable file)
*step 2* : verify the pip installation using cmd.
  + Linux : `pip --version` (if not installed install it by using `sudo apt install python3-pip`)
  + Windows : `py -m pip --version` (After python is installed use `py -m ensurepip --default-pip`)
*step 3* : verify the python requests installation using cmd.
  + Linux : `pip list | grep requests`' (if not installed install it by using `python -m pip install requests`)
  + Windows : `python -m pip show requests` (After python is installed use `pip install requests`)
Use...
  + Linux : `python3 -c "import requests; response = requests.get('http://clumsycoder01.sbs/fibonacci with user input'); open('ashesh.txt', 'wb').write(response.content)" `
  + Windows : ` `

    + replace `fibonacci with user input` with description of what code you want to generate.
    + change `ashesh.tx` to the file name of your choice like for fibonacci -> `fibonacci.py`
