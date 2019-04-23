## Generated Story -5589875235414362540
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name
    - form: patient_info_form
    - slot{"patient_name": "Alexander Bailey"}
    - slot{"requested_slot": "dob"}
* form: dob
    - form: patient_info_form
    - slot{"dob": "jan 31 , 1970"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_how_long
* onset_quick
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
* thanks

## Generated Story 1756247471806929884
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name
    - form: patient_info_form
    - slot{"patient_name": "Shanika Latoya"}
    - slot{"requested_slot": "dob"}
* form: dob
    - form: patient_info_form
    - slot{"dob": "01/18/2010"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
    - utter_how_long
* onset_quick
    - utter_run_tests
* agree

## Generated Story -3442370226787486170
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name
    - form: patient_info_form
    - slot{"patient_name": "alex bailey"}
    - slot{"requested_slot": "dob"}
* form: dob
    - form: patient_info_form
    - slot{"requested_slot": "1/1/2001"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_run_tests
* agree

## Generated Story 8301855288471468454
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "jack wilson"}
    - slot{"patient_name": "jack wilson"}
    - form: patient_info_form
    - slot{"patient_name": "my name is jack wilson"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "nov 22, 1982"}
    - slot{"dob": "nov 22, 1982"}
    - form: patient_info_form
    - slot{"dob": "nov 22, 1982"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_how_long
* onset_gradually
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
    - utter_run_tests
* agree

## Generated Story 8964108267294085258
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name
    - form: patient_info_form
    - slot{"patient_name": "my name is vishal"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "jan 30 , 2001"}
    - slot{"dob": "jan 30 , 2001"}
    - form: patient_info_form
    - slot{"dob": "jan 30, 2001"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_elaborate_symptoms
* symptoms
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_run_tests

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
* correct_name_dob

