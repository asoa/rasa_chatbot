## story_form_gradual_onset
* greet
 - utter_greet
 - patient_info_form
 - form{"name": "patient_info_form"}
 - form{"name": null}
 - utter_verify_name_dob
* correct_name_dob
 - utter_thank_you
 - utter_purpose
* symptoms
 - utter_empathy
 - utter_how_long
* onset_gradually
 - utter_elaborate_symptoms
* symptoms
 - utter_thank_you
 
## story_form_quick_onset
* greet
 - utter_greet
 - patient_info_form
 - form{"name": "patient_info_form"}
 - form{"name": null}
 - utter_verify_name_dob
* correct_name_dob
 - utter_thank_you
 - utter_purpose
* symptoms
 - utter_empathy
 - utter_how_long
* onset_gradually
 - utter_elaborate_symptoms
* symptoms
 - utter_thank_you

## Generated Story 8635970806305325727
* greet
    - utter_greet
    - patient_info_form
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_empathy
    - utter_how_long
* onset_gradually
    - utter_thanks

## Generated Story 7791351099600673334
* greet
    - utter_greet
    - patient_info_form
    - utter_verify_name_dob
* correct_name_dob
    - utter_thank_you
    - utter_purpose
* symptoms
    - utter_how_long
* onset_quick
    - utter_elaborate_symptoms
* symptoms

## Generated Story -5727405024873167436
* greet
    - utter_greet
    - patient_info_form
    - form{"name": "patient_info_form"}
    - slot{"requested_slot": "patient_name"}
* form: patient_name{"patient_name": "tom palen"}
    - slot{"patient_name": "tom palen"}
    - form: patient_info_form
    - slot{"patient_name": "Tom Palen"}
    - slot{"requested_slot": "dob"}
* form: dob{"dob": "jan 29 , 2010"}
    - slot{"dob": "jan 29 , 2010"}
    - form: patient_info_form
    - slot{"dob": "Jan 29, 2010"}
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
* thanks

# TODO: add story to get allergies

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
* form: dob{"dob": "jan 31 , 1970"}
    - slot{"dob": "jan 31 , 1970"}
    - form: patient_info_form
    - slot{"dob": "Jan 31, 1970"}
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

