# # actions.py
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionAddPlayer(Action):
#     def name(self) -> Text:
#         return "action_add_player"

#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Pobranie slotów
#         player_name = tracker.get_slot("player_name")
#         tournament_name = tracker.get_slot("tournament_name")

#         # Tu można dodać logikę zapisu do bazy danych.
#         # Na przykład: Database.add_player(tournament_name, player_name)

#         # Zwrot slotów, aby przechowywać dane w sesji.
#         return [SlotSet("player_name", player_name),
#                 SlotSet("tournament_name", tournament_name)]

# class ActionShowFullInfo(Action):
#     def name(self) -> Text:
#         return "action_show_full_info"

#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         tournament_name = tracker.get_slot("tournament_name")
#         if not tournament_name:
#             # fallback - jeśli nie wiadomo, o który turniej chodzi
#             tournament_name = "Super Cup 2024"  # default/placeholder

#         # Możesz tu pobrać z DB szczegółowe info o turnieju
#         # info = Database.get_full_info(tournament_name)

#         # dispatcher.utter_message(text="Oto szczegóły: ...")

#         return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionAddPlayer(Action):
#     def name(self) -> Text:
#         return "action_add_player"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Przykład: nic nie robi, tylko zwraca
#         return []

# class ActionShowFullInfo(Action):
#     def name(self) -> Text:
#         return "action_show_full_info"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return []

