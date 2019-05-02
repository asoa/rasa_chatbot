from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import Action
from actions.Drug import Drug
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted


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
        # dispatcher.utter_template( 'utter_thank_you', tracker)
        return []


class CorrelateSymptoms(Action):
    def __init__(self):
        self.med_synthetic_dict = {'vicodin':['hydrocodone'],
                                   'simvastatin':['zocor'],
                                   'lisinopril':['prinivil','zestril'],
                                   'levothyroxine':['synthroid'],
                                   'azithromycin':['zithromax','z-pak'],
                                   'metformin':['glucophage'],
                                   'lipitor':['atorvastatin'],
                                   'amlodipine':['norvasc'],
                                   'amoxicillin':['NULL'],
                                   'hydrochlorothiazide':['hctz', 'water pill']}

    def name(self):
        return "action_correlate_symptoms"

    def _get_drug_alias(self, medicines):
        med_generics = [generic for med in medicines  # iterate over user's meds
                            for k, v in self.med_synthetic_dict.items()  # iterate over all med_generic mappings
                                for generic in v  # iterate over all generic medicine names
                                    if med == generic]
        return med_generics

    def run(self, dispatcher, tracker, domain):
        _symptoms = tracker.get_slot('symptoms')
        medicines = tracker.get_slot('medicines')
        d = Drug(symptoms=_symptoms)
        pred, generics, prob_strings = d.get_attributes()
        print(pred)

        if pred in medicines:
            dispatcher.utter_message('[Note] Predicted medicine *{}* has side effects noted by patient'.format(pred))
            dispatcher.utter_message(prob_strings)
            return [SlotSet("prob_medicine", "{}".format(pred + '-pos'))]
        elif len(set([pred]).intersection(generics)) != 0:
            # generic = [drug for l in self.med_synthetic_dict[pred[0]] for drug in l]
            generic = set([pred]).intersection(generics)
            dispatcher.utter_message('[Note] Predicted medicine *{}* is a generic for *{}* and has side effects noted by patient'.format(pred, generic))
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


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]


class ActionRestarted(Action):
    """ This is for restarting the chat"""
    def name(self):
        return "action_restarted"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]














