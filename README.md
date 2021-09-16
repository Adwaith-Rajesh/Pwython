### Installation
To install pwython, simply clone this repository and install via the `setup.py`, it will look like this when done through command line:

```
git clone https://github.com/SystematicError/Pwython
cd Pwython
pip install .
```

After installing you can delete the `Pwython` directory which you just cloned. If you do not have git, you can get a zipped version of the code from [here](https://github.com/SystematicError/Pwython/archive/refs/heads/master.zip).

### Usage
You can use pwython exaclty as you would use python, just replace `python` with `python -m pwython`. For example:

This is how you would run your python code the "traditional" way:

```
python main.py
```

But this is how you run it with pwython:

```
python -m pwython main.py
```

If you are on a MacOS or Linux, you can add `alias pwython="python -m pwython"` in your bashrc file and run your code directly by typing `pwython main.py` in the terminal!