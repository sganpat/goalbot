# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
import time

class ValidateGoalForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_goal_form"

    # async def validate_confirm_exercise(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     if value:
    #         return {"confirm_exercise": True}
    #     else:
    #         return {"exercise": "None", "confirm_exercise": False }

    def validate_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate goal"""

        return []


    def validate_specific_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate specific goal"""

        goal_intent = tracker.get_intent_of_latest_message()

        print (goal_intent)

        # Check if specific goal is no and ask them to restate the goal
        if value:
            return {"specific_goal": True}
        else:
            if goal_intent == "deny":
                dispatcher.utter_message(response="utter_make_specific_goal")
                return {"goal": None, "specific_goal": None}
            else:
                dispatcher.utter_message(response="utter_explain_specific")
                return {"specific_goal": None}

    
    def validate_challenging_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate challenging goal"""

        goal_intent = tracker.get_intent_of_latest_message()

        print (goal_intent)
        
        # Check if challenging goal is no and ask them to restate the goal
        if value:
            return {"challenging_goal": True}
        else:
            if goal_intent == "deny":
                dispatcher.utter_message(response="utter_make_challenging_goal")
                return {"goal": None, "challenging_goal": None}
            else:
                dispatcher.utter_message(response="utter_explain_effortful")
                return {"challenging_goal": None}
    

    def validate_persistent_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate persistent goal"""

        goal_intent = tracker.get_intent_of_latest_message()

        print (goal_intent)

        # Check if persistent goal is no
        if value:
            return {"persistent_goal": True}
        else:
            if goal_intent == "deny":
                dispatcher.utter_message(response="utter_make_persistent_goal")
                return {"persistent_goal": False}
            else:
                dispatcher.utter_message(response="utter_explain_persistence")
                return {"persistent_goal": None}
    

    def validate_goal_actions(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate goal actions"""

        goal_intent = tracker.get_intent_of_latest_message()

        print (goal_intent)

        # Check if asking to explain action
        if goal_intent == "explain":
            dispatcher.utter_message(response="utter_explain_strategy")
            return {"goal_actions": None}

        return []



class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        goal = tracker.get_slot("goal")
        specific_goal = tracker.get_slot("specific_goal")
        challenging_goal = tracker.get_slot("challenging_goal")
        persistent_goal = tracker.get_slot("persistent_goal")
        goal_actions = tracker.get_slot("goal_actions")

        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return


class ActionShowGoals(Action):
    def name(self) -> Text:
        return "action_show_goals"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        goal = tracker.get_slot("goal")
        
        if goal:
            dispatcher.utter_message(response="utter_show_goal")
        else:
            dispatcher.utter_message(response="utter_no_goal")
            dispatcher.utter_message(response="utter_do")
        
        return


class ActionExplainGoals(Action):
    def name(self) -> Text:
        return "action_explain_goals"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(response="utter_what_is_goal")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_explain_specific")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_explain_effortful")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_explain_persistence")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_explain_strategy")
        
        return


class ActionAboutBot(Action):
    def name(self) -> Text:
        return "action_about_bot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(response="utter_about_what")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_about_purpose")
        # time.sleep(1)
        dispatcher.utter_message(response="utter_about_why")
        
        return


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

