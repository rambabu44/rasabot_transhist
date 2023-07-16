# A dictionary for account information of customers with account number as key
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
# A dictionary for transaction history where a nested disctionary is used to record the balance with description in the key as timestamp
transaction_history = {
    "9874563210123687": {
        "2023-05-05" :{
            "balance": 50,
            "description": "salary"
        },
        "2023-05-06" :{
            "balance": 60,
            "description": "bonus"
        }
    },
    "9874563210123688": {
        "2023-04-05" :{
            "balance": 150,
            "description": "salary"
        },
        "2023-04-06" :{
            "balance": 160,
            "description": "bonus"
        }
    }
    
}



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#to return balance in a format as per task.
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

#to return transaction history 
class ActionCheckTransactionHistory(Action):
    def name(self) -> Text:
        return "action_check_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")
        if account_number in transaction_history:
            getTransHistory = transaction_history[account_number]
            response = "Here is your transaction history:\n"
            for transaction in getTransHistory:
                timestamp = transaction
                amount = getTransHistory[str(timestamp)]['balance']
                description = getTransHistory[str(timestamp)]['description']
                response += f"- {timestamp}: Rs. {amount}, {description}\n"
        else:
            response = "Sorry, I couldn't find any account with the provided account number."

        dispatcher.utter_message(text=response)
        return []
    
