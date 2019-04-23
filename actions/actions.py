from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import Action


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


class PatientMedicine(FormAction):
    def name(self):
        return "patient_medicine_form"

    @staticmethod
    def required_slots(tracker):
        return ['medicines']

    # def slot_mappings(self):
    #     # return {"medicines": self.from_text(intent="medicines")}
    #     # return {'medicines': self.from_entity('medicines')}
    #     return

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_verify_medicine', tracker)
        return []


class MedicineInfo(Action):
    """ summarize medicine side effects and return to user """
    def name(self):
        return "action_medicine_info"

    def run(self, dispatcher, tracker, domain):
        self.meds = tracker.get_slot('medicines')
        parsed_meds = self.parse_medicines()
        # dispatcher.utter_message(parsed_meds[0])
        # dispatcher.utter_message(parsed_meds[1])

        for medicine in parsed_meds:
            # get medicine info from api
            info = self.get_med_info(medicine)
            dispatcher.utter_message('{}: {}'.format(medicine, info))

        return []

    def parse_medicines(self):
        if ',' in self.meds:
            medicines = [med.strip() for meds in self.meds for med in meds.split(',')]
        else:
            medicines = [med.strip() for meds in self.meds for med in meds.split(' ')]
        return medicines

    def get_med_info(self, medicine):
        """ use beautiful soup to parse google search results for sever side effects of the medicine """
        return 'medicine info'


class OutOfScope(Action):
    """ user intent is not recognized by NLU -> summarize google search and return to user"""
    def name(self):
        return "out_of_scope"

    def run(self, dispatcher, tracker, domain):
        # do stuff

        return [SlotSet("<slot>")]














