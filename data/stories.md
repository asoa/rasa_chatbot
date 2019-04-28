## Generated Story 6520890970628450436
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "Bob Dylan"}
    - slot{"patient_name": "Bob Dylan"}
    - form: patient_info_form
    - slot{"patient_name": "Bob Dylan"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "may 1 , 2001"}
    - slot{"dob": "may 1 , 2001"}
    - form: patient_info_form
    - slot{"dob": "may 1, 2001"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "Zocor"}
    - slot{"medicines": ["vicodin", "Zocor"]}
    - form: patient_medicine_form
    - slot{"medicines": "vicodin, Zocor"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* symptoms
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_run_tests
* agree

## Generated Story 2423273420425193787
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "alex bailey"}
    - slot{"patient_name": "alex bailey"}
    - form: patient_info_form
    - slot{"patient_name": "alex bailey"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "jan 1 1000"}
    - slot{"dob": "jan 1 1000"}
    - form: patient_info_form
    - slot{"dob": "jan 1 1000"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_information
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "vicodin simvastatin"}
    - slot{"medicines": ["vicodin simvastatin"]}
    - form: patient_medicine_form
    - slot{"medicines": "vicodin simvastatin"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* correct_information
    - get_symptoms_form
    - form{"name": "get_symptoms_form"}
    - slot{"requested_slot": "symptoms"}
* form: symptoms
    - form: get_symptoms_form
    - slot{"symptoms": "drowsiness, headache, upset stomach"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_correlate_symptoms
    - slot{"prob_medicine": "vicodin-pos"}
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_run_tests
* agree

## Generated Story -3793258723292826179
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "perry jones"}
    - slot{"patient_name": "perry jones"}
    - form: patient_info_form
    - slot{"patient_name": "Perry Jones"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "oct 15 , 1978"}
    - slot{"dob": "oct 15 , 1978"}
    - form: patient_info_form
    - slot{"dob": "oct 15, 1978"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_information
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "zithromax"}
    - slot{"medicines": "zithromax"}
    - form: patient_medicine_form
    - slot{"medicines": "zithromax"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* correct_information
    - get_symptoms_form
    - form{"name": "get_symptoms_form"}
    - slot{"requested_slot": "symptoms"}
* form: symptoms
    - form: get_symptoms_form
    - slot{"symptoms": "I have a constant headache, vomiting, and stomach pain"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_correlate_symptoms
    - slot{"prob_medicine": "azithromycin-pos"}
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_run_tests
* agree
    - utter_your_welcome

