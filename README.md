# BotMarathi
[![Twitter Follow](https://img.shields.io/twitter/follow/botmarathi?color=w&label=follow%20%40Botmarathi&style=for-the-badge)](http://twitter.com/botmarathi)

A Marathi twitter bot that retweets and favorites some other popular tweets based on hashtag :hash:, location, and user. It also tweets certain information every day, such as latest news :newspaper:, a quote and some events which took place on this day some years ago.

The bot scraps the web to get the information, and utilizes BeautifulSoup to read the information properly. It using shcedule to run all these operations for periodically :clock1: at pre-determined intervals.

## What's this repository about?

Online running at [https://twitter.com/botmarathi]

This BotMarathi created using help of article published at [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library) and deployed on heruko.


## How do I run this project locally?

### 1. Clone the repository:

    git clone https://github.com/vinodnimbalkar/BotMarathi.git

### 2. Change Directory:  :open_file_folder:
    cd BotMarathi

### 3. Install dependency:

    pip install -r requirements.txt

### 4. Instructions
   * Create a new [Twitter Application.](https://apps.twitter.com/app/new) This is where you'll generate your keys :key:, tokens, and secrets.
   * Fill in your keys, tokens, and secrets in the creaditials.py file.
   * Check comments in MarathiBot.py to change this bot to as per your convenience.

### 5. Run on terminal: :running:

    python MarathiBot.py

### 6. And open Twitter in your web browser.:computer:

## Contributing

Feel free to open an issue (or even better, send a Pull Request) for expanding this list. Contributions are very welcome!! 😄

<a href="https://www.buymeacoffee.com/vinodnimbalkar" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
