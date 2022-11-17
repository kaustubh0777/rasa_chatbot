# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from stocks_api import api_stock_price
from news_api import market_news
from term_def import get_term_definition

class ActionStockPrice(Action):

     def name(self) -> Text:
         return "action_stock_price"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #entities = tracker.latest_message.get("entities", [])
        #entities = {e["entity"]: e["value"] for e in entities}

        stcknme = tracker.latest_message['entities'][0]['value']

        stockprice = api_stock_price(stcknme)

        dispatcher.utter_message(text=f"The stock price of {stcknme} is {stockprice}")

        return []


class ActionMarketNews(Action):

     def name(self) -> Text:
         return "action_get_news"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         
        today_news = market_news()

        dispatcher.utter_message(text=today_news)

        return []


class ActionTermDefinition(Action):

     def name(self) -> Text:
         return "action_get_definition"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        fin_term = tracker.latest_message['entities']#[0]['value']

        #term_def = get_term_definition(fin_term)     

        dispatcher.utter_message(text=f"The term {fin_term} is defined as ")

        return []
