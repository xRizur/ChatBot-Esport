import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionListCompetitions(Action):
    def name(self) -> Text:
        return "action_list_competitions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            with open("competitions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                competitions = data.get("competitions", [])
        except Exception as e:
            dispatcher.utter_message(text="Sorry, an error occurred while reading the competitions data.")
            return []

        if competitions:
            message_lines = ["Here are the available competitions:"]
            for comp in competitions:
                name = comp.get("name", "Unknown")
                details = comp.get("details", "No details available")
                message_lines.append(f"- {name}: {details}")
            message = "\n".join(message_lines)
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="No competitions found.")

        return []
