from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class PatientInfoForm(FormAction):
    def name(self):
        return "patient_info_form"

    @staticmethod
    def required_slots(tracker):
        return ["patient_name", "dob"]

    def slot_mappings(self):
        return {"patient_name": self.from_text(intent="patient_name"),
                "dob": self.from_text(intent="dob")}

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_thank_you', tracker)
        return []