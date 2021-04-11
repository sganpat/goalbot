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

