# Cafe-POS

A Simple Cafe Point-of-Sales app with simple database feature. Build with Python and PyQt5 GUI framework.

**Note!** If you want, latest version of PyQt and alternative PySide binding should be work, but not tested.

The code is a bit mess, but it should works perfectly.

<img src="preview.png" alt="drawing" width="200"/>

## Requirements

* Python >=3.6 (Tested on Python 3.9)

## How to run ?

### Easy step

* Download manually this repo
* Extract it
* Open the folder with VSCode
* Run the **initDB.py** then **loginWindow.py**

### Conventional step

Download manually or git clone this repo

```shell
git clone https://blablabla
```

Change directory

```shell
cd <yourpath>
```

(Optional) Setting your virtual environments in Windows with Powershell

```powershell
python -m venv c:\path\to\myenv
.\Scripts\Activate.ps1
```

Install pip package (required)

```shell
pip install pyqt5 pyqt5-tools
```

Database initialization

```shell
python initDB.py
```

Run the app

```shell
python loginWindow.py
```
