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

    def validate_specific_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate specific goal"""

        # Check if specific goal is no and ask them to restate the goal
        if value:
            return {"specific_goal": True}
        else:
            dispatcher.utter_message(response="utter_make_specific_goal")
            return {"goal": None, "specific_goal": None}
    
    def validate_challenging_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate challenging goal"""

        # Check if challenging goal is no and ask them to restate the goal
        if value:
            return {"challenging_goal": True}
        else:
            dispatcher.utter_message(response="utter_make_challenging_goal")
            return {"goal": None, "challenging_goal": None}
    
    def validate_persistent_goal(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate persistent goal"""

        # Check if persistent goal is no
        if value:
            return {"persistent_goal": True}
        else:
            dispatcher.utter_message(response="utter_make_persistent_goal")
            return {"persistent_goal": False}
    
    def validate_goal_actions(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate goal actions"""

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


        # confirm_exercise = tracker.get_slot("confirm_exercise")
        # exercise = tracker.get_slot("exercise")
        # sleep = tracker.get_slot("sleep")
        # stress = tracker.get_slot("stress")
        # diet = tracker.get_slot("diet")


        # response = create_health_log(
        #         confirm_exercise=confirm_exercise,
        #         exercise=exercise,
        #         sleep=sleep,
        #         stress=stress,
        #         diet=diet,
        #         goal=goal
        #     )

        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []




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

