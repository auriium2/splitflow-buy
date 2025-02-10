# Nelson Dane
# Script to automate RSA stock purchases

# Import libraries
import os
import sys
import traceback
import cherrypy


# Check Python version (minimum 3.10, maximum 3.12)
print()

try:
    import discord
    from discord.ext import commands
    from dotenv import load_dotenv

    # Custom API libraries
    from bbaeAPI import *
    from chaseAPI import *
    from dspacAPI import *
    from fennelAPI import *
    from fidelityAPI import *
    from firstradeAPI import *
    from helperAPI import (
        ThreadHandler,
        check_package_versions,
        printAndDiscord,
        stockOrder,
        updater,
    )
    from publicAPI import *
    from robinhoodAPI import *
    from schwabAPI import *
    from sofiAPI import *
    from tastyAPI import *
    from tornadoAPI import *
    from tradierAPI import *
    from vanguardAPI import *
    from webullAPI import *
    from wellsfargoAPI import *
except Exception as e:
    print(f"Error importing libraries: {e}")
    print(traceback.format_exc())
    print("Please run 'pip install -r requirements.txt'")
    sys.exit(1)

# Initialize .env file
load_dotenv()

# Global variables
SUPPORTED_BROKERS = [
    "bbae",
    "chase",
    "dspac",
    "fennel",
    "fidelity",
    "firstrade",
    "public",
    "robinhood",
    "schwab",
    "sofi",
    "tastytrade",
    "tornado",
    "tradier",
    "vanguard",
    "webull",
    "wellsfargo",
]
DAY1_BROKERS = [
    "bbae",
    "chase",
    "dspac",
    "fennel",
    "firstrade",
    "public",
    "schwab",
    "sofi",
    "tastytrade",
    "tradier",
    "webull",
]

SAFE_FOR_SF = [
    "bbae",
    "chase",
    "dspac",
    "fennel",
    "firstrade",
    "public",
    "schwab",
    "sofi",
    "tastytrade",
    "tradier",
    "webull",
]

DISCORD_BOT = False
DOCKER_MODE = False
DANGER_MODE = False

# Account nicknames
def nicknames(broker):
    if broker == "bb":
        return "bbae"
    if broker == "ds":
        return "dspac"
    if broker in ["fid", "fido"]:
        return "fidelity"
    if broker == "ft":
        return "firstrade"
    if broker == "rh":
        return "robinhood"
    if broker == "tasty":
        return "tastytrade"
    if broker == "vg":
        return "vanguard"
    if broker == "wb":
        return "webull"
    if broker == "wf":
        return "wellsfargo"
    return broker


# Runs the specified function for each broker in the list
# broker name + type of function
def fun_run(orderObj: stockOrder, command, botObj=None, loop=None):
    if command in [("_init", "_holdings"), ("_init", "_transaction")]:
        totalValue = 0
        for broker in orderObj.get_brokers():
            if broker in orderObj.get_notbrokers():
                continue
            broker = nicknames(broker)
            first_command, second_command = command
            try:
                # Initialize broker
                fun_name = broker + first_command
                if broker.lower() == "wellsfargo":
                    # Fidelity requires docker mode argument
                    orderObj.set_logged_in(
                        globals()[fun_name](
                            DOCKER=DOCKER_MODE, botObj=botObj, loop=loop
                        ),
                        broker,
                    )
                elif broker.lower() == "tornado":
                    # Requires docker mode argument and loop
                    orderObj.set_logged_in(
                        globals()[fun_name](DOCKER=DOCKER_MODE, loop=loop),
                        broker,
                    )
                elif broker.lower() in [
                    "bbae",
                    "dspac",
                    "fennel",
                    "firstrade",
                    "public",
                ]:
                    # Requires bot object and loop
                    orderObj.set_logged_in(
                        globals()[fun_name](botObj=botObj, loop=loop), broker
                    )
                elif broker.lower() in ["chase", "fidelity", "sofi", "vanguard"]:
                    fun_name = broker + "_run"
                    # PLAYWRIGHT_BROKERS have to run all transactions with one function
                    th = ThreadHandler(
                        globals()[fun_name],
                        orderObj=orderObj,
                        command=command,
                        botObj=botObj,
                        loop=loop,
                    )
                    th.start()
                    th.join()
                    _, err = th.get_result()
                    if err is not None:
                        raise Exception(
                            "Error in "
                            + fun_name
                            + ": Function did not complete successfully."
                        )
                else:
                    orderObj.set_logged_in(globals()[fun_name](), broker)

                print()
                if broker.lower() not in ["chase", "fidelity", "sofi", "vanguard"]:
                    # Verify broker is logged in
                    orderObj.order_validate(preLogin=False)
                    logged_in_broker = orderObj.get_logged_in(broker)
                    if logged_in_broker is None:
                        print(f"Error: {broker} not logged in, skipping...")
                        continue
                    # Get holdings or complete transaction
                    if second_command == "_holdings":
                        fun_name = broker + second_command
                        globals()[fun_name](logged_in_broker, loop)
                    elif second_command == "_transaction":
                        fun_name = broker + second_command
                        globals()[fun_name](
                            logged_in_broker,
                            orderObj,
                            loop,
                        )
                        printAndDiscord(
                            f"All {broker.capitalize()} transactions complete",
                            loop,
                        )
                # Add to total sum
                totalValue += sum(
                    account["total"]
                    for account in orderObj.get_logged_in(broker)
                    .get_account_totals()
                    .values()
                )
            except Exception as ex:
                print(traceback.format_exc())
                print(f"Error in {fun_name} with {broker}: {ex}")
                print(orderObj)
            print()

        # Print final total value and closing message
        if "_holdings" in command:
            printAndDiscord(
                f"Total Value of All Accounts: ${format(totalValue, '0.2f')}", loop
            )
        printAndDiscord("All commands complete in all brokers", loop)
    else:
        print(f"Error: {command} is not a valid command")

@cherrypy.expose
class AutoRSAService(object):

    @cherrypy.tools.json_out()
    def GET(self, **params):
        print("GET request received\n")
        return "Hello, World!"

    @cherrypy.tools.json_out()
    def POST(self, **params):
        try:
            body = cherrypy.request.body.read().decode('utf-8')
            params = json.loads(body)
            action = params.get('action')
            amount = params.get('amount')
            stock = params.get('stock')
            dry = params.get('dry')
        except Exception as ex:
            raise cherrypy.HTTPError(400, f"bad request: {ex}")

        objOrder = stockOrder()
        objOrder.set_action(action)
        objOrder.set_amount(amount)
        objOrder.set_stock(stock)
        objOrder.set_brokers(DAY1_BROKERS + ["robinhood"])
        objOrder.set_dry(dry)
        try:
            objOrder.order_validate(preLogin=True)
        except Exception as ex:
            return str(ex)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(fun_run(objOrder, ("_init", "_transaction"), None, loop))
        return "OK"


if __name__ == "__main__":

    print("Starting serwvwwwer...")

    DOCKER_MODE = True
    #updater()
    #check_package_versions()

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    })


    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(AutoRSAService(), '/', conf)

