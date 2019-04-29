## fallback
- utter_unclear

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
* long_time
    - utter_run_tests
* agree
    - action_restarted

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
* long_time
    - utter_run_tests
* agree
    - action_restarted

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
* long_time
    - utter_run_tests
* agree
    - action_restarted

## Generated Story 990528445627180298
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "Sally J. Moorehouse"}
    - slot{"patient_name": "Sally J. Moorehouse"}
    - form: patient_info_form
    - slot{"patient_name": "Sally J. Moorehouse"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "october 18 , 1965"}
    - slot{"dob": "october 18 , 1965"}
    - form: patient_info_form
    - slot{"dob": "october 18, 1965"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_information
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "synthroid"}
    - slot{"medicines": "synthroid"}
    - form: patient_medicine_form
    - slot{"medicines": ["Prinivil", "synthroid"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* correct_information
    - get_symptoms_form
    - form{"name": "get_symptoms_form"}
    - slot{"requested_slot": "symptoms"}
* form: symptoms
    - form: get_symptoms_form
    - slot{"symptoms": "I have this nagging cough and constant chest pain"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_correlate_symptoms
    - slot{"prob_medicine": "lisinopril-neg"}
    - utter_empathy
    - utter_how_long
* long_time
    - utter_run_tests
* agree
    - action_restarted

## Generated Story 5776828992397326258
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "brian kelly"}
    - slot{"patient_name": "brian kelly"}
    - form: patient_info_form
    - slot{"patient_name": "My name is Brian Kelly"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "sep 25 1989"}
    - slot{"dob": "sep 25 1989"}
    - form: patient_info_form
    - slot{"dob": "sep 25 1989"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_information
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "hydrocodone"}
    - slot{"medicines": "hydrocodone"}
    - form: patient_medicine_form
    - slot{"medicines": ["metformin", "amlodipine", "hydrocodone"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* correct_information
    - get_symptoms_form
    - form{"name": "get_symptoms_form"}
    - slot{"requested_slot": "symptoms"}
* form: symptoms
    - form: get_symptoms_form
    - slot{"symptoms": "i have confusion, sometimes tremors, and sometimes i feel like i might pass out"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_correlate_symptoms
    - slot{"prob_medicine": "amlodipine-neg"}
    - utter_empathy
    - utter_how_long
* long_time
    - utter_run_tests
* agree
    - action_restarted
## Generated Story -8315453361725917321
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "sam smith"}
    - slot{"patient_name": "sam smith"}
    - form: patient_info_form
    - slot{"patient_name": "sam smith"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "jun 7 1987"}
    - slot{"dob": "jun 7 1987"}
    - form: patient_info_form
    - slot{"dob": "jun 7 1987"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_information
    - utter_thank_you
    - patient_medicine_form
    - form{"name": "patient_medicine_form"}
    - slot{"requested_slot": "medicines"}
* form: medicines{"medicines": "hydrocodone"}
    - slot{"medicines": "hydrocodone"}
    - form: patient_medicine_form
    - slot{"medicines": "hydrocodone"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_medicines
* correct_information
    - get_symptoms_form
    - form{"name": "get_symptoms_form"}
    - slot{"requested_slot": "symptoms"}
* form: symptoms
    - form: get_symptoms_form
    - slot{"symptoms": "i have constipation, drowsiness, and i feel tired all the time"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_correlate_symptoms
    - slot{"prob_medicine": "simvastatin-neg"}
    - utter_empathy
    - utter_how_long
* long_time
    - utter_run_tests
* correct_information
    - action_restarted

