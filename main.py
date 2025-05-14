# from flask import Flask, request, render_template, jsonify
# import numpy as np
# import pandas as pd
# import pickle
#
# # Flask app
# app = Flask(__name__)
#
# # Load datasets
# sym_des = pd.read_csv("dataset/symtoms_df.csv")
# precautions = pd.read_csv("dataset/precautions_df.csv")
# workout = pd.read_csv("dataset/workout_df.csv")
# description = pd.read_csv("dataset/description.csv")
# medications = pd.read_csv('dataset/medications.csv')
# diets = pd.read_csv("dataset/diets.csv")
#
# # Load model
# svc = pickle.load(open('model/svc.pkl', 'rb'))
#
# # Helper function to get disease details
# def helper(dis):
#     desc = description[description['Disease'] == dis]['Description']
#     desc = " ".join([w for w in desc]) if not desc.empty else "No description available."
#
#     pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
#     pre = [col for col in pre.values.flatten() if col] if not pre.empty else ["Consult a doctor"]
#
#     med = medications[medications['Disease'] == dis]['Medication']
#     med = [m for m in med.values.flatten() if m] if not med.empty else ["Consult a doctor"]
#
#     die = diets[diets['Disease'] == dis]['Diet']
#     die = [d for d in die.values.flatten() if d] if not die.empty else ["Balanced diet"]
#
#     wrkout = workout[workout['disease'] == dis]['workout']
#     wrkout = [w for w in wrkout.values if w] if not wrkout.empty else ["Rest"]
#
#     return desc, pre, med, die, wrkout
#
# # Symptoms dictionary
# symptoms_dict = {
#     'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4,
#     'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10,
#     'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15,
#     'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20,
#     'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25,
#     'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31,
#     'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36,
#     'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42,
#     'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46,
#     'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51,
#     'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56,
#     'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
#     'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66,
#     'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71,
#     'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75,
#     'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80,
#     'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85,
#     'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89,
#     'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93,
#     'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
#     'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102,
#     'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107,
#     'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
#     'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115,
#     'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118,
#     'prominent_veins_on_calf': 119,
#     'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124,
#     'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128,
#     'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
# }
#
# # Diseases list
# diseases_list = {
#     15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction',
#     33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma',
#     23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)',
#     28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A',
#     19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis',
#     36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack',
#     39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis',
#     5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection',
#     35: 'Psoriasis', 27: 'Impetigo'
# }
#
# # Model Prediction function
# def get_predicted_value(patient_symptoms):
#     input_vector = np.zeros(len(symptoms_dict))
#     valid_symptoms = []
#
#     # Filter valid symptoms
#     for item in patient_symptoms:
#         if item and item in symptoms_dict:  # Check if item is non-empty and exists in symptoms_dict
#             valid_symptoms.append(item)
#             input_vector[symptoms_dict[item]] = 1
#
#     if not valid_symptoms:  # If no valid symptoms are found
#         raise ValueError("No valid symptoms provided.")
#
#     return diseases_list[svc.predict([input_vector])[0]]
#
# # Static hospitals data
# STATIC_HOSPITALS = {
#     "Allergy": [
#         {"name": "Allergy Clinic Boston", "address": "789 Sneeze Rd, Boston, MA", "specialty": "Immunology", "phone": "555-111-2222", "website": "http://allergyclinic.com"},
#         {"name": "Allergy Specialists NYC", "address": "321 Itch Blvd, New York, NY", "specialty": "Allergy", "phone": "555-222-3333", "website": "http://allergyexperts.com"}
#     ],
#     "Heart attack": [
#         {"name": "Cardiac Care Boston", "address": "123 Heartbeat Rd, Boston, MA", "specialty": "Cardiology", "phone": "555-333-4444", "website": "http://cardiaccare.com"},
#         {"name": "NYC Heart Institute", "address": "456 Pulse Ave, New York, NY", "specialty": "Cardiology", "phone": "555-444-5555", "website": "http://nycheart.com"}
#     ],
#     # Add other diseases as needed
# }
#
# # Routes
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         symptoms = request.form.get('symptoms', '').strip()
#
#         # Check if symptoms input is empty or default
#         if not symptoms or symptoms.lower() == "symptoms":
#             print("No symptoms provided")
#             return render_template(
#                 'index.html',
#                 message="Please provide valid symptoms (comma-separated).",
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )
#
#         # Split the user's input into a list of symptoms
#         user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
#         print(f"User Symptoms: {user_symptoms}")  # Debug log
#
#         try:
#             predicted_disease = get_predicted_value(user_symptoms)
#             print(f"Predicted Disease: '{predicted_disease}'")  # Debug log
#             dis_des, my_precautions, medications, my_diet, workout = helper(predicted_disease)
#
#             # Filter out any None or empty precautions
#             my_precautions = [i for i in my_precautions if i]
#
#             # Define diseases that require hospital recommendations
#             hospital_diseases = [
#                 "Heart attack", "Allergy", "Pneumonia", "Tuberculosis", "Malaria", "Dengue", "Typhoid",
#                 "hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "AIDS"
#             ]
#             show_hospitals = predicted_disease in hospital_diseases
#             static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []
#             print(f"Show Hospitals: {show_hospitals}, Predicted Disease in Hospital Diseases: {predicted_disease in hospital_diseases}, Static Hospitals: {static_hospitals}")  # Debug log
#             print(f"Rendering template with: predicted_disease='{predicted_disease}', show_hospitals={show_hospitals}, static_hospitals={static_hospitals}")  # Debug log
#
#             return render_template(
#                 'index.html',
#                 message=None,
#                 predicted_disease=predicted_disease,
#                 static_hospitals=static_hospitals,
#                 dis_des=dis_des,
#                 my_precautions=my_precautions,
#                 medications=medications,
#                 workout=workout,
#                 my_diet=my_diet,
#                 show_hospitals=show_hospitals
#             )
#
#         except ValueError as e:
#             print(f"ValueError: {str(e)}")
#             return render_template(
#                 'index.html',
#                 message=str(e),
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )
#         except KeyError as e:
#             print(f"KeyError: {str(e)}")
#             return render_template(
#                 'index.html',
#                 message=f"Invalid symptom provided: {str(e)}. Please check your input.",
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )
#
#     # For GET request, provide default values
#     print("Rendering index.html for GET request")
#     return render_template(
#         'index.html',
#         message=None,
#         predicted_disease=None,
#         static_hospitals=[],
#         dis_des=None,
#         my_precautions=[],
#         medications=[],
#         workout=[],
#         my_diet=[],
#         show_hospitals=False
#     )
#
# @app.route('/about')
# def about():
#     return render_template("about.html")
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/developer')
# def developer():
#     return render_template("developer.html")
#
# @app.route('/blog')
# def blog():
#     return render_template('blog.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)
# below for maps

# from flask import Flask, request, render_template, jsonify
# import numpy as np
# import pandas as pd
# import pickle

# # Flask app
# app = Flask(__name__)

# # Load datasets
# sym_des = pd.read_csv("dataset/symtoms_df.csv")
# precautions = pd.read_csv("dataset/precautions_df.csv")
# workout = pd.read_csv("dataset/workout_df.csv")
# description = pd.read_csv("dataset/description.csv")
# medications = pd.read_csv('dataset/medications.csv')
# diets = pd.read_csv("dataset/diets.csv")

# # Load model
# svc = pickle.load(open('model/svc.pkl', 'rb'))

# # Helper function to get disease details
# def helper(dis):
#     desc = description[description['Disease'] == dis]['Description']
#     desc = " ".join([w for w in desc]) if not desc.empty else "No description available."

#     pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
#     pre = [col for col in pre.values.flatten() if col] if not pre.empty else ["Consult a doctor"]

#     med = medications[medications['Disease'] == dis]['Medication']
#     med = [m for m in med.values.flatten() if m] if not med.empty else ["Consult a doctor"]

#     die = diets[diets['Disease'] == dis]['Diet']
#     die = [d for d in die.values.flatten() if d] if not die.empty else ["Balanced diet"]

#     wrkout = workout[workout['disease'] == dis]['workout']
#     wrkout = [w for w in wrkout.values if w] if not wrkout.empty else ["Rest"]

#     return desc, pre, med, die, wrkout

# # Symptoms dictionary
# symptoms_dict = {
#     'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4,
#     'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10,
#     'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15,
#     'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20,
#     'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25,
#     'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31,
#     'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36,
#     'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42,
#     'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46,
#     'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51,
#     'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56,
#     'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
#     'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66,
#     'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71,
#     'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75,
#     'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80,
#     'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85,
#     'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89,
#     'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93,
#     'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
#     'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102,
#     'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107,
#     'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
#     'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115,
#     'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118,
#     'prominent_veins_on_calf': 119,
#     'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124,
#     'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128,
#     'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
# }

# # Diseases list
# diseases_list = {
#     15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction',
#     33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma',
#     23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)',
#     28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A',
#     19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis',
#     36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack',
#     39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis',
#     5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection',
#     35: 'Psoriasis', 27: 'Impetigo'
# }

# # Model Prediction function
# def get_predicted_value(patient_symptoms):
#     input_vector = np.zeros(len(symptoms_dict))
#     valid_symptoms = []

#     # Filter valid symptoms
#     for item in patient_symptoms:
#         if item and item in symptoms_dict:  # Check if item is non-empty and exists in symptoms_dict
#             valid_symptoms.append(item)
#             input_vector[symptoms_dict[item]] = 1

#     if not valid_symptoms:  # If no valid symptoms are found
#         raise ValueError("No valid symptoms provided.")

#     return diseases_list[svc.predict([input_vector])[0]]

# # Static hospitals data
# STATIC_HOSPITALS = {
#     "Allergy": [
#         {"name": "Allergy Clinic Boston", "address": "789 Sneeze Rd, Boston, MA", "specialty": "Immunology", "phone": "555-111-2222", "website": "http://allergyclinic.com"},
#         {"name": "Allergy Specialists NYC", "address": "321 Itch Blvd, New York, NY", "specialty": "Allergy", "phone": "555-222-3333", "website": "http://allergyexperts.com"}
#     ],
#     "Heart attack": [
#         {"name": "Cardiac Care Boston", "address": "123 Heartbeat Rd, Boston, MA", "specialty": "Cardiology", "phone": "555-333-4444", "website": "http://cardiaccare.com"},
#         {"name": "NYC Heart Institute", "address": "456 Pulse Ave, New York, NY", "specialty": "Cardiology", "phone": "555-444-5555", "website": "http://nycheart.com"}
#     ],
#     # Add other diseases as needed
# }

# # Routes
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         symptoms = request.form.get('symptoms', '').strip()

#         # Check if symptoms input is empty or default
#         if not symptoms or symptoms.lower() == "symptoms":
#             print("No symptoms provided")
#             return render_template(
#                 'index.html',
#                 message="Please provide valid symptoms (comma-separated).",
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )

#         # Split the user's input into a list of symptoms
#         user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
#         print(f"User Symptoms: {user_symptoms}")  # Debug log

#         try:
#             predicted_disease = get_predicted_value(user_symptoms)
#             print(f"Predicted Disease: '{predicted_disease}'")  # Debug log
#             dis_des, my_precautions, medications, my_diet, workout = helper(predicted_disease)

#             # Filter out any None or empty precautions
#             my_precautions = [i for i in my_precautions if i]

#             # Define diseases that require hospital recommendations
#             hospital_diseases = [
#                 "Heart attack", "Allergy", "Pneumonia", "Tuberculosis", "Malaria", "Dengue", "Typhoid",
#                 "hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "AIDS"
#             ]
#             show_hospitals = predicted_disease in hospital_diseases
#             static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []
#             print(f"Show Hospitals: {show_hospitals}, Predicted Disease in Hospital Diseases: {predicted_disease in hospital_diseases}, Static Hospitals: {static_hospitals}")  # Debug log
#             print(f"Rendering template with: predicted_disease='{predicted_disease}', show_hospitals={show_hospitals}, static_hospitals={static_hospitals}")  # Debug log

#             return render_template(
#                 'index.html',
#                 message=None,
#                 predicted_disease=predicted_disease,
#                 static_hospitals=static_hospitals,
#                 dis_des=dis_des,
#                 my_precautions=my_precautions,
#                 medications=medications,
#                 workout=workout,
#                 my_diet=my_diet,
#                 show_hospitals=show_hospitals
#             )

#         except ValueError as e:
#             print(f"ValueError: {str(e)}")
#             return render_template(
#                 'index.html',
#                 message=str(e),
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )
#         except KeyError as e:
#             print(f"KeyError: {str(e)}")
#             return render_template(
#                 'index.html',
#                 message=f"Invalid symptom provided: {str(e)}. Please check your input.",
#                 predicted_disease=None,
#                 static_hospitals=[],
#                 dis_des=None,
#                 my_precautions=[],
#                 medications=[],
#                 workout=[],
#                 my_diet=[],
#                 show_hospitals=False
#             )

#     # For GET request, provide default values
#     print("Rendering index.html for GET request")
#     return render_template(
#         'index.html',
#         message=None,
#         predicted_disease=None,
#         static_hospitals=[],
#         dis_des=None,
#         my_precautions=[],
#         medications=[],
#         workout=[],
#         my_diet=[],
#         show_hospitals=False
#     )

# @app.route('/about')
# def about():
#     return render_template("about.html")

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/developer')
# def developer():
#     return render_template("developer.html")

# @app.route('/blog')
# def blog():
#     return render_template('blog.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# chat below 


from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle

# Flask app
app = Flask(__name__)

# Load datasets
sym_des = pd.read_csv("dataset/symtoms_df.csv")
precautions = pd.read_csv("dataset/precautions_df.csv")
workout = pd.read_csv("dataset/workout_df.csv")
description = pd.read_csv("dataset/description.csv")
medications = pd.read_csv('dataset/medications.csv')
diets = pd.read_csv("dataset/diets.csv")

# Load model
svc = pickle.load(open('model/svc.pkl', 'rb'))

# Helper function to get disease details
def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc]) if not desc.empty else "No description available."

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values.flatten() if col] if not pre.empty else ["Consult a doctor"]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [m for m in med.values.flatten() if m] if not med.empty else ["Consult a doctor"]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [d for d in die.values.flatten() if d] if not die.empty else ["Balanced diet"]

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = [w for w in wrkout.values if w] if not wrkout.empty else ["Rest"]

    return desc, pre, med, die, wrkout

# Symptoms dictionary
symptoms_dict = {
    'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4,
    'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10,
    'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15,
    'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20,
    'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25,
    'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31,
    'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36,
    'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42,
    'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46,
    'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51,
    'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56,
    'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
    'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66,
    'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71,
    'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75,
    'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80,
    'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85,
    'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89,
    'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93,
    'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
    'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102,
    'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107,
    'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
    'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115,
    'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118,
    'prominent_veins_on_calf': 119,
    'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124,
    'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128,
    'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
}

# Diseases list
diseases_list = {
    15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction',
    33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma',
    23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)',
    28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A',
    19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis',
    36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack',
    39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis',
    5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection',
    35: 'Psoriasis', 27: 'Impetigo'
}

# Model Prediction function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    valid_symptoms = []

    # Filter valid symptoms
    for item in patient_symptoms:
        if item and item in symptoms_dict:  # Check if item is non-empty and exists in symptoms_dict
            valid_symptoms.append(item)
            input_vector[symptoms_dict[item]] = 1

    if not valid_symptoms:  # If no valid symptoms are found
        raise ValueError("No valid symptoms provided.")

    return diseases_list[svc.predict([input_vector])[0]]

# Static hospitals data
STATIC_HOSPITALS = {
    "Allergy": [
        {"name": "Allergy Clinic Boston", "address": "789 Sneeze Rd, Boston, MA", "specialty": "Immunology", "phone": "555-111-2222", "website": "http://allergyclinic.com"},
        {"name": "Allergy Specialists NYC", "address": "321 Itch Blvd, New York, NY", "specialty": "Allergy", "phone": "555-222-3333", "website": "http://allergyexperts.com"}
    ],
    "Heart attack": [
        {"name": "Cardiac Care Boston", "address": "123 Heartbeat Rd, Boston, MA", "specialty": "Cardiology", "phone": "555-333-4444", "website": "http://cardiaccare.com"},
        {"name": "NYC Heart Institute", "address": "456 Pulse Ave, New York, NY", "specialty": "Cardiology", "phone": "555-444-5555", "website": "http://nycheart.com"}
    ],
}

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '').strip()

        # Check if symptoms input is empty or default
        if not symptoms or symptoms.lower() == "symptoms":
            print("No symptoms provided")
            return render_template(
                'index.html',
                message="Please provide valid symptoms (comma-separated).",
                predicted_disease=None,
                static_hospitals=[],
                dis_des=None,
                my_precautions=[],
                medications=[],
                workout=[],
                my_diet=[],
                show_hospitals=False,
                symptoms_dict=symptoms_dict
            )

        # Split the user's input into a list of symptoms
        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        print(f"User Symptoms (from form or chatbot): {user_symptoms}")  # Debug log

        try:
            predicted_disease = get_predicted_value(user_symptoms)
            print(f"Predicted Disease: '{predicted_disease}'")  # Debug log
            dis_des, my_precautions, medications, my_diet, workout = helper(predicted_disease)

            # Filter out any None or empty precautions
            my_precautions = [i for i in my_precautions if i]

            # Define diseases that require hospital recommendations
            hospital_diseases = [
                "Heart attack", "Allergy", "Pneumonia", "Tuberculosis", "Malaria", "Dengue", "Typhoid",
                "hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "AIDS"
            ]
            show_hospitals = predicted_disease in hospital_diseases
            static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []
            print(f"Show Hospitals: {show_hospitals}, Predicted Disease in Hospital Diseases: {predicted_disease in hospital_diseases}, Static Hospitals: {static_hospitals}")  # Debug log
            print(f"Rendering template with: predicted_disease='{predicted_disease}', show_hospitals={show_hospitals}, static_hospitals={static_hospitals}")  # Debug log

            return render_template(
                'index.html',
                message=None,
                predicted_disease=predicted_disease,
                static_hospitals=static_hospitals,
                dis_des=dis_des,
                my_precautions=my_precautions,
                medications=medications,
                workout=workout,
                my_diet=my_diet,
                show_hospitals=show_hospitals,
                symptoms_dict=symptoms_dict
            )

        except ValueError as e:
            print(f"ValueError: {str(e)}")
            return render_template(
                'index.html',
                message=str(e),
                predicted_disease=None,
                static_hospitals=[],
                dis_des=None,
                my_precautions=[],
                medications=[],
                workout=[],
                my_diet=[],
                show_hospitals=False,
                symptoms_dict=symptoms_dict
            )
        except KeyError as e:
            print(f"KeyError: {str(e)}")
            return render_template(
                'index.html',
                message=f"Invalid symptom provided: {str(e)}. Please check your input.",
                predicted_disease=None,
                static_hospitals=[],
                dis_des=None,
                my_precautions=[],
                medications=[],
                workout=[],
                my_diet=[],
                show_hospitals=False,
                symptoms_dict=symptoms_dict
            )

    # For GET request, provide default values
    print("Rendering index.html for GET request")
    return render_template(
        'index.html',
        message=None,
        predicted_disease=None,
        static_hospitals=[],
        dis_des=None,
        my_precautions=[],
        medications=[],
        workout=[],
        my_diet=[],
        show_hospitals=False,
        symptoms_dict=symptoms_dict
    )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developer')
def developer():
    return render_template("developer.html")

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)