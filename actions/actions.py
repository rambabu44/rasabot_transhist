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


account_details = {
    "9874563210123687": {
        "name": "John Doe",
        "phone": 9812345678,
        "balance": 1000,
    },
    "9874563210123688": {
        "name": "somenme",
        "phone": 9812345008,
        "balance": 1002,
    }
}

transaction_history = {
    "9874563210123687": {
        { 
        "timestamp": "2023-05-05",
        "balance": 50,
        "description": "salary"},
        {
           { 
        "timestamp": "2023-05-06",
        "balance": 60,
        "description": "bonus"} 
        }
    }
}


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")
        if account_number in account_details:
            balance = account_details[account_number]["balance"]
            response = f"Dear {account_details[account_number]['name']}, your {account_number} has a balance of Rs. {balance}"
        else:
            response = "Sorry, I couldn't find any account with the provided account number."
        dispatcher.utter_message(text=response)
        return []

class ActionCheckTransactionHistory(Action):
    def name(self) -> Text:
        return "action_check_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")
        if account_number in transaction_history:
            # Simulating transaction history retrieval
            transaction_history = transaction_history(account_number)

            if transaction_history:
                response = "Here is your transaction history:\n"
                for transaction in transaction_history:
                    timestamp = transaction['timestamp']
                    amount = transaction['balance']
                    description = transaction['description']
                    response += f"- {timestamp}: Rs. {amount}, {description}\n"
            else:
                response = "No transaction history found for your account."
        else:
            response = "Sorry, I couldn't find any account with the provided account number."

        dispatcher.utter_message(text=response)
        return []
    
