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

NOTE: you only need to install pandas (line 7) if you will be pulling data from a csv file (see below).

## Setup

In your local repository's root directory, create a new file called ".env".

Update the contents of the ".env" file to specify your [local sales tax](https://taxfoundation.org/2021-sales-taxes/) (in decimal form):

    TAX_RATE = "0.065"

You may use the [sendgrid package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to send an email receipt to your customer. If you choose to do so, include the following in your .env file. Otherwise, comment out rows 133 - 175 in shopping_cart.py and do not add the following entries to your .env file. Read more on picking an email template [here](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#email-templates).

  + Update the contents of the ".env" file to specify your sendgrid API key:
  
        SENDGRID_API_KEY = "numbersandletters123"

  + Update the contents of the ".env" file to specify your sender's email address:

        SENDER_ADDRESS = "youremail@email.com"

  + Update the contents of the ".env" file to specify your sendgrid email template:

        SENDGRID_TEMPLATE_ID = "numbersandletters123"

When inputing your template data for the email (lines 142-147), use below as a reference: 
template_data = {
    "total_price_usd": to_usd(total_price),
    "human_friendly_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
    "products":
        sorted_selected_products
}

## Usage

Run the game script:

```py
python shopping_cart.py
```

## CSV Version
If using a csv file instead of manually changing the products data embedded in lines 12-30 of shopping_py, create a new folder in the repo called "data". Copy the provided "default_products.csv" file into your local repo under the "data" folder and rename it "products.csv". Un-comment lines 6, 8, and 10 and then comment out lines 12-33.