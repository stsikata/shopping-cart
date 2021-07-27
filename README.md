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

In your local repository's root directory, create a new file called ".env".

Update the contents of the ".env" file to specify your local sales tax (in decimal form):

    TAX_RATE = "0.065"

Update the contents of the ".env" file to specify your sendgrid API key:
  
    SENDGRID_API_KEY = "numbersandletters123"

Update the contents of the ".env" file to specify your sender's email address:

    SENDER_ADDRESS = "youremail@email.com"

Update the contents of the ".env" file to specify your sendgrid email template:

    SENDGRID_TEMPLATE_ID = "numbersandletters123"

<!-- When inputing your template data for the email (line 162), use below as a reference: 
template_data = {
    "total_price_usd": to_usd(total_price),
    "human_friendly_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
    "products":
        sorted_selected_products
} -->

## Usage

Run the game script:

```py
python shopping_cart.py
```
If using a csv file instead of products data embedded in code, create a new folder in the repo called "data". Copy the provided "default_products.csv" file into your local repo and save as "data/products.csv". Un-comment lines 6, 8, and 10 and then comment out lines 12-33.