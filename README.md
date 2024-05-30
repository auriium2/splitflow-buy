# ✨ AutoRSA ✨ 
## Discord Bot and CLI Tool
A CLI tool and Discord bot to buy, sell, and monitor holdings across multiple brokerage accounts!

<p>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
<img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
<img src="https://img.shields.io/badge/-discord.py-%232c2f33?style=for-the-badge&logo=discord&logoColor=white"/>
<img src="https://img.shields.io/badge/-docker-%232c2f33?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

## 🤔 How Does It Work? 🤔
This program uses APIs to interface with your brokerages. When available, official APIs are always used. If an official API is not available, then a third-party API is used. As a last resort, Selenium or Playwright Stealth are used to automate the browser.

## 📝 Installation 📝
There are two ways to use this program: as a Discord bot or as a CLI tool. The setup instructions will be a little different depending on which method you choose. However, both methods require the same pre-setup steps, and the same `.env` file format.

### 🛠️ Pre-Setup 🛠️
1. Install `git` for your operating system.
2. Clone this repository and cd into it:
```bash
git clone https://github.com/NelsonDane/auto-rsa.git
cd auto-rsa
```
3. Copy the `.env.example` file to a new file called `.env`:
```bash
cp .env.example .env
```
4. Fill in the `.env` file with your brokerage credentials. See the [Supported Brokerages](#-supported-brokerages-) section for more information.

Now follow the instructions for either the Discord Bot or CLI Tool. Once setup is complete, see the [Usage](#-usage-) section for how to use the program.

### 🤖 Discord Bot Installation 🤖
To create your Discord bot and get your `DISCORD_TOKEN` for your `.env`, follow this [guide](guides/discordBot.md).

There are two ways to run the Discord bot: using Docker or running the Python script. When running the bot using the Python script, the bot will only be online when the script is running. With Docker, the bot will run in the background, restarting and updating automatically.

### 🐳 Discord Bot: Docker 🐳
1. Add `DISCORD_TOKEN` and `DISCORD_CHANNEL` to your `.env` file.
2. Create the container using the provided [docker-compose.yml](docker-compose.yml) file:
```bash
docker-compose up -d
```
3. The bot should appear online in Discord (You can also do `!ping` to check).

Docker Note: If you make any changes to your `.env` file, you will need to restart the container by running `docker-compose up -d` again. The bot will also automatically stay up to date thanks to the included [Watchtower](https://containrrr.dev/watchtower/).

### 🏃‍♂️ Discord Bot: Python Script 🏃‍♀️
1. Install Python 3.10 or higher
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Add `DISCORD_TOKEN` and `DISCORD_CHANNEL` to your `.env` file.
4. Start the bot using the following command:
```bash
python autoRSA.py discord
```
5. The bot should appear online in Discord (You can also do `!ping` to check).

### 💻 CLI Tool Installation 💻
To run the CLI tool, follow these steps:
1. Install Python 3.10 or higher
2. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Run the script using `python autoRSA.py`. It should say that no arguments were given, then exit. This is expected, and means everything was installed and set up correctly.

## 👀 Usage 👀

To buy and sell stocks, use this command:

`<action> <amount> <ticker> <accounts> <dry>`

For example, to buy 1 AAPL in all accounts:

`buy 1 AAPL all false`

For a dry run of the above command in Robinhood only:

`buy 1 AAPL robinhood true`

For a real run on Fidelity and Robinhood, but not Schwab:

`buy 1 AAPL fidelity,robinhood not schwab false`

For a real run on Fidelity and Robinhood but not Schwab buying both AAPL and GOOG:

`buy 1 AAPL,GOOG fidelity,robinhood not schwab false`

To check your account holdings:

`holdings <accounts>`

To restart the Discord bot (only for the Docker Discord bot):

`!restart` (without appending `!rsa`)

For help:

`!help` (without appending `!rsa`)

### ⚙️ Parameters Explanation ⚙️
- `<prefix>`: string, The prefix for the command. For the Discord bot, this is `!rsa`. For the CLI tool, this is `python autoRSA.py`.
- `<action>`: string, "buy" or "sell"
- `<amount>`: integer, Amount to buy or sell.
- `<ticker>`: string, The stock ticker to buy or sell. Separate multiple tickers with commas and no spaces.
- `<accounts>`: string, What brokerage to run command in (robinhood, schwab, etc, or all). Separate multiple brokerages with commas and no spaces.
- `<not accounts>`: string proceeding `not`, What brokerages to exclude from command. Separate multiple brokerages with commas and no spaces.
- `<dry>`: boolean, Whether to run in `dry` mode (in which no transactions are made. Useful for testing). Set to `True`, `False`, or just write `dry` for`True`. Defaults to `True`, so if you want to run a real transaction, you must set this explicitly.

Note: There are two special keywords you can use when specifying accounts: `all` and `day1`. `all` will use every account that you have set up. `day1` will use "day 1" brokers, which are:
- Chase
- Fennel
- Firstrade
- Public
- Robinhood
- Schwab
- Tastytrade
- Tradier
- Webull

This is useful for brokers that provide quick turnaround times, hence the nickname "day 1".

## 🗺️ Other Guides 🗺️
More detailed guides for some of the difficult setups:
- [Discord Bot Setup](guides/discordBot.md)
- [Robinhood 2FA Setup](guides/robinhoodSetup.md)
- [Schwab 2FA Setup](guides/schwabSetup.md)

## 🤝 Contributing 🤝
Found or fixed a bug? Have a feature request? Want to add support for a new brokerage? Feel free to open an issue or pull request!

Enjoying the project? Feel free to Sponsor me on GitHub or Ko-fi!

[![Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/NelsonDane)
[![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white
)](https://ko-fi.com/X8X6LFCI0)

## 😳 DISCLAIMER 😳
DISCLAIMER: I am not a financial advisor and not affiliated with any of the brokerages listed below. Use this tool at your own risk. I am not responsible for any losses or damages you may incur by using this project. This tool is provided as-is with no warranty.

## 👍 Supported brokerages 👍

All brokers: separate account credentials with a colon (":"). For example, `SCHWAB_USERNAME:SCHWAB_PASSWORD`. Separate multiple logins with the same broker with a comma (","). For example, `SCHWAB_USERNAME:SCHWAB_PASSWORD,SCHWAB_USERNAME2:SCHWAB_PASSWORD2`.

Some brokerages require `Playwright` to run. On Windows, the `playwright install` command might not be recognized. If this is the case, run `python -m playwright install` instead.

#### Chase
Made by [MaxxRK](https://github.com/MaxxRK/) using the [chaseinvest-api](https://github.com/MaxxRK/chaseinvest-api). Go give them a ⭐
- `CHASE_USERNAME`
- `CHASE_PASSWORD`
- `CELL_PHONE_LAST_FOUR`
Optional .env variables:
- `DEBUG` (Set to `True` to enable debug mode)`

`.env` file format:
- `CHASE=CHASE_USERNAME:CHASE_PASSWORD:CELL_PHONE_LAST_FOUR:DEBUG`

### Fennel
Made by yours truly using the [fennel-invest-api](https://github.com/NelsonDane/fennel-invest-api). Consider giving me a ⭐

Required `.env` variables:
- `FENNEL_EMAIL`

`.env` file format:
- `FENNEL=FENNEL_EMAIL`

Fennel accounts don't have passwords, so you need to login by inputting the code sent to your email. The script will then save your session credentials for future use.

### Fennel
Made by yours truly using the [fennel-invest-api](https://github.com/NelsonDane/fennel-invest-api). Consider giving me a ⭐

Required `.env` variables:
- `FENNEL_EMAIL`

`.env` file format:
- `FENNEL=FENNEL_EMAIL`

Fennel accounts don't have passwords, so you need to login by inputting the code sent to your email. The script will then save your session credentials for future use.

### Fidelity
Made by yours truly using Selenium (and many hours of web scraping).

Required `.env` variables:
- `FIDELITY_USERNAME`
- `FIDELITY_PASSWORD`

`.env` file format:
- `FIDELITY=FIDELITY_USERNAME:FIDELITY_PASSWORD`

### Firstrade
Made by [MaxxRK](https://github.com/MaxxRK/) using the [firstrade-api](https://github.com/MaxxRK/firstrade-api). Go give them a ⭐

Required `.env` variables:
- `FIRSTRADE_USERNAME`
- `FIRSTRADE_PASSWORD`
- `FIRSTRADE_PIN`

`.env` file format:
- `FIRSTRADE=FIRSTRADE_USERNAME:FIRSTRADE_PASSWORD:FIRSTRADE_PIN`

### Public
Made by yours truly using using [public-invest-api](https://github.com/NelsonDane/public-invest-api). Consider giving me a ⭐

Required `.env` variables:
- `PUBLIC_USERNAME`
- `PUBLIC_PASSWORD`

`.env` file format:
- `PUBLIC_BROKER=PUBLIC_USERNAME:PUBLIC_PASSWORD`

Note: Because Windows already has a `PUBLIC` environment variable, you will need to use `PUBLIC_BROKER` instead.

### Robinhood
Made using [robin_stocks](https://github.com/jmfernandes/robin_stocks). Go give them a ⭐

Required `.env` variables:
- `ROBINHOOD_USERNAME`
- `ROBINHOOD_PASSWORD`
- `ROBINHOOD_TOTP` (If 2fa enabled, else NA)

`.env` file format:
- With 2fa: `ROBINHOOD=ROBINHOOD_USERNAME:ROBINHOOD_PASSWORD:ROBINHOOD_TOTP`
- Without 2fa: `ROBINHOOD=ROBINHOOD_USERNAME:ROBINHOOD_PASSWORD:NA`

Configuring 2fa can be tricky, so follow this [guide](guides/robinhoodSetup.md).

### Schwab
Made using the [schwab-api](https://github.com/itsjafer/schwab-api). Go give them a ⭐

Required `.env` variables:
- `SCHWAB_USERNAME`
- `SCHWAB_PASSWORD`
- `SCHWAB_TOTP_SECRET` (If 2fa is enabled, else NA)

`.env` file format:
- With 2fa: `SCHWAB=SCHWAB_USERNAME:SCHWAB_PASSWORD:SCHWAB_TOTP_SECRET`
- Without 2fa: `SCHWAB=SCHWAB_USERNAME:SCHWAB_PASSWORD:NA`

To get your TOTP secret, follow this [guide](guides/schwabSetup.md).

Note 1: Think or Swim must be enabled on all accounts. To enable, go to `Trade` > `Trading Platforms` > `Learn how to enable thinkorswim`. Then press `Continue` and expand the `thinkorswim Access Agreement` and accept it. Then press `Continue` again. Then select the checkbox for all available accounts and press `Submit`. It may take a day or two for the accounts to be enabled.

### Tradier
Made by yours truly using the official [Tradier API](https://documentation.tradier.com/brokerage-api/trading/getting-started). Consider giving me a ⭐

Required `.env` variables:
- `TRADIER_ACCESS_TOKEN`

`.env` file format:
- `TRADIER=TRADIER_ACCESS_TOKEN`

To get your access token, go to your [Tradier API settings](https://dash.tradier.com/settings/api).

### Tastytrade
Made by [MaxxRK](https://github.com/MaxxRK/) using the [tastytrade-api](https://github.com/tastyware/tastytrade). Go give them a ⭐

Required `.env` variables:
- `TASTYTRADE_USERNAME`
- `TASTYTRADE_PASSWORD`

`.env` file format:
- `TASTYTRADE=TASTYTRADE_USERNAME:TASTYTRADE_PASSWORD`

### Webull
Made using the [webull](https://github.com/tedchou12/webull) library. Go give them a ⭐

Required `.env` variables:
- `WEBULL_USERNAME`
- `WEBULL_PASSWORD`
- `WEBULL_DID`
- `WEBULL_TRADING_PIN`

`.env` file format:
- `WEBULL=WEBULL_USERNAME:WEBULL_PASSWORD:WEBULL_DID:WEBULL_TRADING_PIN`

Your `WEBULL_USERNAME` can be your email or phone number. If using a phone number, it must be formatted as: +1-XXXXXXXXXX or +86-XXXXXXXXXXX.

To get your Webull DID, follow this [guide](https://github.com/tedchou12/webull/wiki/Workaround-for-Login-%E2%80%90-Method-2).

### 🤷‍♂️ Maybe future brokerages 🤷‍♀️
#### Vanguard
In progress [here](https://github.com/NelsonDane/auto-rsa/pull/242).
#### SoFi
In progress [here](https://github.com/NelsonDane/auto-rsa/pull/237).
### 👎 Never working brokerages 👎
#### Stash
Why.
