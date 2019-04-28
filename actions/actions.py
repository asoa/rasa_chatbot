from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import Action
from actions.Drug import Drug


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
    """ opt1: summarize medicine side effects and return to user #TODO
    """
    def name(self):
        return "action_medicine_info"

    def run(self, dispatcher, tracker, domain):
        self.meds = tracker.get_slot('medicines')
        parsed_meds = self.parse_medicines()
        # dispatcher.utter_message(parsed_meds[0])
        # dispatcher.utter_message(parsed_meds[1])

        # for medicine in parsed_meds:
        #     # get medicine info from api
        #     info = self.get_med_info(medicine)
        #     dispatcher.utter_message('{}: {}'.format(medicine, info))

        return []

    def parse_medicines(self):
        if ',' in self.meds:
            medicines = [med.strip() for meds in self.meds for med in meds.split(',')]
        elif len(self.meds) == 1:
            medicines = self.meds
        elif len(self.meds) == 0:
            return SlotSet("medicines", None)
        else:
            medicines = [med.strip() for meds in self.meds for med in meds.split(' ')]
        return medicines

    def get_med_info(self, medicine):
        """ use beautiful soup to parse google search results for sever side effects of the medicine """
        return 'medicine info'


class GetName(FormAction):
    """ get name from intent """
    def name(self):
        return "action_get_name"

    def slot_mappings(self):
        return {'patient_name': self.from_text(intent='patient_name')}


class GetSymptoms(FormAction):
    """ predict the patients symptoms to medicine catalog """
    def name(self):
        return "get_symptoms_form"

    @staticmethod
    def required_slots(tracker):
        return ['symptoms']

    def slot_mappings(self):
        return {'symptoms': self.from_text(intent='symptoms')}

    # def run(self, dispatcher, tracker, domain):
    #     symptoms = tracker.get_slot('symptoms')
        # self.correlate_symptoms(symptoms)

    def correlate_symptoms(self, symptoms):
        self.pred = Drug().nb_predict(symptoms)
        return [SlotSet("prob_medicine")]

    def submit(self, dispatcher, tracker, domain):
        # dispatcher.utter_message(self.pred)
        # dispatcher.utter_template('utter_thank_you', tracker)
        return []


class CorrelateSymptoms(Action):
    def name(self):
        return "action_correlate_symptoms"

    def run(self, dispatcher, tracker, domain):
        _symptoms = tracker.get_slot('symptoms')
        medicines = tracker.get_slot('medicines')
        d = Drug(symptoms=_symptoms)
        pred = d.pred[0]
        print(pred)
        if pred[0] in medicines:
            dispatcher.utter_message('[Note] Predicted medicine *{}* has side effects noted by patient'.format(pred))
            return [SlotSet("prob_medicine", "{}".format(pred + '-pos'))]
        else:
            dispatcher.utter_message('[Note] Predicted medicine *{}* is reported not taken by patient'.format(pred))
            return [SlotSet("prob_medicine", "{}".format(pred + '-neg'))]


class OutOfScope(Action):
    """ user intent is not recognized by NLU -> summarize google search and return to user"""
    def name(self):
        return "action_google_search"

    def run(self, dispatcher, tracker, domain):
        # TODO

        return [SlotSet("<slot>")]














