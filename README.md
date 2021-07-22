# shopping-cart

A Python application to run the shopping cart exercise.


## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](https://github.com/stsikata/shopping-cart.git) and clone a remote copy on your local computer.

Navigate to the local copy from the command line:

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment called "shopping-env":

```sh
conda create -n shopping-env python=3.8 # first time only
conda activate shopping-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In your local repository's root directory, create a new file called ".env". Update the contents of the ".env" file to specify your desired ################username:

    PLAYER_NAME="Sedina Tsikata"

## Usage

Run the game script:

```py
python shopping_cart.py
```