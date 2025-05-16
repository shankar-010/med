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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict
#             )

#         # Split the user's input into a list of symptoms
#         user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
#         print(f"User Symptoms (from form or chatbot): {user_symptoms}")  # Debug log

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
#                 show_hospitals=show_hospitals,
#                 symptoms_dict=symptoms_dict
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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict
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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict
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
#         show_hospitals=False,
#         symptoms_dict=symptoms_dict
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
# lab below




# from flask import Flask, request, render_template, jsonify
# import numpy as np
# import pandas as pd
# import pickle
# import sqlite3
# from datetime import datetime

# # Flask app
# app = Flask(__name__)

# # SQLite database setup
# def init_db():
#     conn = sqlite3.connect('healthytic.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS lab_test_results (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     disease TEXT NOT NULL,
#                     test_name TEXT NOT NULL,
#                     test_result TEXT NOT NULL,
#                     test_date TEXT NOT NULL,
#                     created_at TEXT NOT NULL
#                  )''')
#     conn.commit()
#     conn.close()

# # Initialize database
# init_db()

# # Load datasets
# sym_des = pd.read_csv("dataset/symtoms_df.csv")
# precautions = pd.read_csv("dataset/precautions_df.csv")
# workout = pd.read_csv("dataset/workout_df.csv")
# description = pd.read_csv("dataset/description.csv")
# medications = pd.read_csv('dataset/medications.csv')
# diets = pd.read_csv("dataset/diets.csv")

# # Load model
# svc = pickle.load(open('model/svc.pkl', 'rb'))

# # Lab tests recommendations based on diseases
# LAB_TESTS = {
#     "Heart attack": ["ECG", "Troponin Test", "Complete Blood Count (CBC)", "Lipid Profile"],
#     "Allergy": ["Allergy Skin Test", "IgE Blood Test", "Complete Blood Count (CBC)"],
#     "Diabetes": ["HbA1c Test", "Fasting Blood Sugar Test", "Oral Glucose Tolerance Test"],
#     "Bronchial Asthma": ["Spirometry", "Peak Flow Test", "Allergy Test"],
#     "Hypertension": ["Blood Pressure Monitoring", "Lipid Profile", "Kidney Function Test"],
#     "Pneumonia": ["Chest X-Ray", "Complete Blood Count (CBC)", "Sputum Culture"],
#     "Tuberculosis": ["Chest X-Ray", "Sputum Test", "Tuberculin Skin Test"],
#     "Malaria": ["Malaria Parasite Test", "Complete Blood Count (CBC)"],
#     "Dengue": ["NS1 Antigen Test", "Dengue IgM/IgG Test", "Platelet Count"],
#     "Typhoid": ["Widal Test", "Blood Culture", "Complete Blood Count (CBC)"],
#     "hepatitis A": ["Liver Function Test", "Hepatitis A IgM Test"],
#     "Hepatitis B": ["HBsAg Test", "Liver Function Test", "HBV DNA Test"],
#     "Hepatitis C": ["HCV Antibody Test", "Liver Function Test", "HCV RNA Test"],
#     "Hepatitis D": ["HDV Antibody Test", "Liver Function Test"],
#     "Hepatitis E": ["HEV IgM Test", "Liver Function Test"],
#     "AIDS": ["HIV Test", "CD4 Count", "Viral Load Test"]
# }

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

#     # Get recommended lab tests
#     tests = LAB_TESTS.get(dis, [])

#     return desc, pre, med, die, wrkout, tests

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
# }

# # Routes
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # Fetch test history from the database
#     conn = sqlite3.connect('healthytic.db')
#     c = conn.cursor()
#     c.execute("SELECT disease, test_name, test_result, test_date FROM lab_test_results ORDER BY created_at DESC")
#     test_history = [{"disease": row[0], "test_name": row[1], "test_result": row[2], "test_date": row[3]} for row in c.fetchall()]
#     conn.close()

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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict,
#                 recommended_tests=[],
#                 test_history=test_history
#             )

#         # Split the user's input into a list of symptoms
#         user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
#         print(f"User Symptoms (from form or chatbot): {user_symptoms}")  # Debug log

#         try:
#             predicted_disease = get_predicted_value(user_symptoms)
#             print(f"Predicted Disease: '{predicted_disease}'")  # Debug log
#             dis_des, my_precautions, medications, my_diet, workout, recommended_tests = helper(predicted_disease)

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
#                 show_hospitals=show_hospitals,
#                 symptoms_dict=symptoms_dict,
#                 recommended_tests=recommended_tests,
#                 test_history=test_history
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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict,
#                 recommended_tests=[],
#                 test_history=test_history
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
#                 show_hospitals=False,
#                 symptoms_dict=symptoms_dict,
#                 recommended_tests=[],
#                 test_history=test_history
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
#         show_hospitals=False,
#         symptoms_dict=symptoms_dict,
#         recommended_tests=[],
#         test_history=test_history
#     )

# @app.route('/submit_test_results', methods=['POST'])
# def submit_test_results():
#     disease = request.form.get('disease')
#     test_name = request.form.get('test_name')
#     test_result = request.form.get('test_result')
#     test_date = request.form.get('test_date')

#     if not all([disease, test_name, test_result, test_date]):
#         return jsonify({"error": "All fields are required"}), 400

#     # Insert test result into the database
#     conn = sqlite3.connect('healthytic.db')
#     c = conn.cursor()
#     created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     c.execute("INSERT INTO lab_test_results (disease, test_name, test_result, test_date, created_at) VALUES (?, ?, ?, ?, ?)",
#               (disease, test_name, test_result, test_date, created_at))
#     conn.commit()
#     conn.close()

#     return jsonify({"message": "Test result saved successfully"}), 200

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



from flask import Flask, request, render_template, jsonify, send_file
import numpy as np
import pandas as pd
import pickle
import sqlite3
from datetime import datetime
import json
import os
import tempfile
import uuid
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('healthytic.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lab_test_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    disease TEXT NOT NULL,
                    test_name TEXT NOT NULL,
                    test_result TEXT NOT NULL,
                    test_date TEXT NOT NULL,
                    created_at TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

init_db()

sym_des = pd.read_csv("dataset/symtoms_df.csv")
precautions = pd.read_csv("dataset/precautions_df.csv")
workout = pd.read_csv("dataset/workout_df.csv")
description = pd.read_csv("dataset/description.csv")
medications = pd.read_csv('dataset/medications.csv')
diets = pd.read_csv("dataset/diets.csv")

svc = pickle.load(open('model/svc.pkl', 'rb'))

LAB_TESTS = {
    "Heart attack": ["ECG", "Troponin Test", "Complete Blood Count (CBC)", "Lipid Profile"],
    "Allergy": ["Allergy Skin Test", "IgE Blood Test", "Complete Blood Count (CBC)"],
    "Diabetes": ["HbA1c Test", "Fasting Blood Sugar Test", "Oral Glucose Tolerance Test"],
    "Bronchial Asthma": ["Spirometry", "Peak Flow Test", "Allergy Test"],
    "Hypertension": ["Blood Pressure Monitoring", "Lipid Profile", "Kidney Function Test"],
    "Pneumonia": ["Chest X-Ray", "Complete Blood Count (CBC)", "Sputum Culture"],
    "Tuberculosis": ["Chest X-Ray", "Sputum Test", "Tuberculin Skin Test"],
    "Malaria": ["Malaria Parasite Test", "Complete Blood Count (CBC)"],
    "Dengue": ["NS1 Antigen Test", "Dengue IgM/IgG Test", "Platelet Count"],
    "Typhoid": ["Widal Test", "Blood Culture", "Complete Blood Count (CBC)"],
    "hepatitis A": ["Liver Function Test", "Hepatitis A IgM Test"],
    "Hepatitis B": ["HBsAg Test", "Liver Function Test", "HBV DNA Test"],
    "Hepatitis C": ["HCV Antibody Test", "Liver Function Test", "HCV RNA Test"],
    "Hepatitis D": ["HDV Antibody Test", "Liver Function Test"],
    "Hepatitis E": ["HEV IgM Test", "Liver Function Test"],
    "AIDS": ["HIV Test", "CD4 Count", "Viral Load Test"]
}

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

    tests = LAB_TESTS.get(dis, [])

    return desc, pre, med, die, wrkout, tests

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

def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    valid_symptoms = []

    for item in patient_symptoms:
        if item and item in symptoms_dict:
            valid_symptoms.append(item)
            input_vector[symptoms_dict[item]] = 1

    if not valid_symptoms:
        raise ValueError("No valid symptoms provided.")

    prediction = svc.predict([input_vector])[0]
    print(f"Input vector: {input_vector}, Prediction: {prediction}, Disease: {diseases_list[prediction]}")
    return diseases_list[prediction]

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

# Helper function to escape HTML-like characters for reportlab (similar to LaTeX escaping but for PDF rendering)
def escape_for_pdf(text):
    if not isinstance(text, str):
        text = str(text)
    # Replace special characters that might cause issues in reportlab
    replacements = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
    }
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('healthytic.db')
    c = conn.cursor()
    c.execute("SELECT disease, test_name, test_result, test_date FROM lab_test_results ORDER BY created_at DESC")
    test_history = [{"disease": row[0], "test_name": row[1], "test_result": row[2], "test_date": row[3]} for row in c.fetchall()]
    conn.close()

    default_values = {
        'message': None,
        'predicted_disease': None,
        'static_hospitals': [],
        'dis_des': None,
        'my_precautions': [],
        'medications': [],
        'workout': [],
        'my_diet': [],
        'show_hospitals': False,
        'symptoms_dict': symptoms_dict,
        'recommended_tests': [],
        'test_history': test_history,
        'user_symptoms': []
    }

    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '').strip()
        if not symptoms or symptoms.lower() == "symptoms":
            print("No symptoms provided")
            return render_template('index.html', **default_values, message="Please provide valid symptoms (comma-separated).")

        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        print(f"User Symptoms (from form or chatbot): {user_symptoms}")

        try:
            # Validate symptoms before prediction
            valid_symptoms = [s for s in user_symptoms if s in symptoms_dict]
            invalid_symptoms = [s for s in user_symptoms if s not in symptoms_dict]
            if not valid_symptoms:
                print(f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}")
                return render_template('index.html', **default_values, message=f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}. Please use exact symptom names (e.g., chest_pain, high_fever).")

            predicted_disease = get_predicted_value(user_symptoms)
            print(f"Predicted Disease: '{predicted_disease}'")
            dis_des, my_precautions, medications, my_diet, workout, recommended_tests = helper(predicted_disease)

            my_precautions = [str(i) for i in my_precautions if i]
            medications = [str(i) for i in medications if i]
            my_diet = [str(i) for i in my_diet if i]
            workout = [str(i) for i in workout if i]
            recommended_tests = [str(i) for i in recommended_tests if i]
            user_symptoms = [str(i) for i in user_symptoms if i]

            hospital_diseases = [
                "Heart attack", "Allergy", "Pneumonia", "Tuberculosis", "Malaria", "Dengue", "Typhoid",
                "hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "AIDS"
            ]
            show_hospitals = predicted_disease in hospital_diseases
            static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []

            render_data = {
                'message': None,
                'predicted_disease': str(predicted_disease) if predicted_disease else "Not available",
                'static_hospitals': static_hospitals if static_hospitals else [],
                'dis_des': str(dis_des) if dis_des else "Not available",
                'my_precautions': my_precautions if my_precautions else [],
                'medications': medications if medications else [],
                'workout': workout if workout else [],
                'my_diet': my_diet if my_diet else [],
                'show_hospitals': show_hospitals,
                'symptoms_dict': symptoms_dict,
                'recommended_tests': recommended_tests if recommended_tests else [],
                'test_history': test_history,
                'user_symptoms': user_symptoms if user_symptoms else []
            }

            try:
                json.dumps(render_data['user_symptoms'])
                json.dumps(render_data['medications'])
                json.dumps(render_data['my_precautions'])
                json.dumps(render_data['workout'])
                json.dumps(render_data['my_diet'])
                json.dumps(render_data['recommended_tests'])
                json.dumps(render_data['static_hospitals'])
                print("All data serialized successfully")
            except Exception as e:
                print(f"Serialization error: {str(e)}")
                print(f"Problematic data: {render_data}")
                return render_template('index.html', **default_values, message=f"Data serialization error: {str(e)}")

            print("Rendering template with:", render_data)
            return render_template('index.html', **render_data)

        except ValueError as e:
            print(f"ValueError: {str(e)}")
            return render_template('index.html', **default_values, message=str(e))

        except KeyError as e:
            print(f"KeyError: {str(e)}")
            return render_template('index.html', **default_values, message=f"Invalid symptom provided: {str(e)}. Please check your input.")

        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return render_template('index.html', **default_values, message=f"An unexpected error occurred: {str(e)}")

    print("Rendering index.html for GET request")
    return render_template('index.html', **default_values)

@app.route('/submit_lab_test', methods=['POST'])
def submit_lab_test():
    try:
        data = request.get_json()
        disease = data.get('disease')
        test_name = data.get('test_name')
        test_result = data.get('test_result')
        test_date = data.get('test_date')
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if not all([disease, test_name, test_result, test_date]):
            return jsonify({"error": "All fields are required"}), 400

        conn = sqlite3.connect('healthytic.db')
        c = conn.cursor()
        c.execute("INSERT INTO lab_test_results (disease, test_name, test_result, test_date, created_at) VALUES (?, ?, ?, ?, ?)",
                  (disease, test_name, test_result, test_date, created_at))
        conn.commit()
        conn.close()

        return jsonify({"message": "Lab test result submitted successfully"}), 200
    except Exception as e:
        print(f"Error submitting lab test: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        predicted_disease = data.get('predicted_disease', 'Unknown')
        description = data.get('description', 'No description available.')
        precautions = data.get('precautions', [])
        medications = data.get('medications', [])
        diet = data.get('diet', [])
        workouts = data.get('workouts', [])
        lab_tests = data.get('lab_tests', [])

        # Instead of generating LaTeX, return the raw data as JSON
        report_data = {
            "symptoms": symptoms,
            "predicted_disease": predicted_disease,
            "description": description,
            "precautions": precautions,
            "medications": medications,
            "diet": diet,
            "workouts": workouts,
            "lab_tests": lab_tests,
            "generated_date": datetime.now().strftime("%B %d, %Y")
        }

        return jsonify({"report_data": report_data}), 200
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/render_latex', methods=['POST'])
def render_latex():
    try:
        # Get the report data from the request (previously sent by /generate_report)
        data = request.get_json()
        if not data or 'report_data' not in data:
            return jsonify({"error": "No report data provided"}), 400

        report_data = data['report_data']
        symptoms = report_data.get('symptoms', [])
        predicted_disease = report_data.get('predicted_disease', 'Unknown')
        description = report_data.get('description', 'No description available.')
        precautions = report_data.get('precautions', [])
        medications = report_data.get('medications', [])
        diet = report_data.get('diet', [])
        workouts = report_data.get('workouts', [])
        lab_tests = report_data.get('lab_tests', [])
        generated_date = report_data.get('generated_date', datetime.now().strftime("%B %d, %Y"))

        # Create a unique temporary directory for this request
        temp_dir = tempfile.mkdtemp()
        unique_id = str(uuid.uuid4())
        pdf_file_path = os.path.join(temp_dir, f"report_{unique_id}.pdf")

        # Create a PDF using reportlab
        doc = SimpleDocTemplate(pdf_file_path, pagesize=A4, leftMargin=1*inch, rightMargin=1*inch, topMargin=1*inch, bottomMargin=1*inch)
        styles = getSampleStyleSheet()

        # Define custom styles
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontSize=16,
            spaceAfter=12,
            alignment=1  # Center
        )
        heading_style = ParagraphStyle(
            'HeadingStyle',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=10
        )
        subheading_style = ParagraphStyle(
            'SubheadingStyle',
            parent=styles['Heading3'],
            fontSize=12,
            spaceAfter=8
        )
        normal_style = ParagraphStyle(
            'NormalStyle',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            leading=12
        )

        story = []

        # Header (mimicking fancyhdr)
        story.append(Paragraph("Healthytic Health Report", title_style))
        story.append(Paragraph(f"Generated on: {generated_date}", normal_style))
        story.append(Spacer(1, 0.3 * inch))

        # Patient Health Summary
        story.append(Paragraph("Patient Health Summary", heading_style))
        story.append(Paragraph(
            "This report is generated by Healthytic, an AI-driven health insight platform. "
            "It provides a summary of your symptoms, predicted condition, and recommended care plan. "
            "Please consult a healthcare professional for a thorough diagnosis and treatment.",
            normal_style
        ))
        story.append(Spacer(1, 0.2 * inch))

        # Symptom Summary
        story.append(Paragraph("Symptom Summary", subheading_style))
        if symptoms:
            symptoms_text = "".join([f"• {escape_for_pdf(symptom.replace('_', ' ').capitalize())}<br/>" for symptom in symptoms])
            story.append(Paragraph(symptoms_text, normal_style))
        else:
            story.append(Paragraph("No symptoms provided.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        # Predicted Condition
        story.append(Paragraph("Predicted Condition", subheading_style))
        story.append(Paragraph(f"<b>{escape_for_pdf(predicted_disease)}</b>", normal_style))
        story.append(Paragraph(f"<i>Description:</i> {escape_for_pdf(description)}", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        # Suggested Care Plan
        story.append(Paragraph("Suggested Care Plan", subheading_style))

        # Precautions
        story.append(Paragraph("Precautions", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if precautions:
            precautions_text = "".join([f"• {escape_for_pdf(precaution)}<br/>" for precaution in precautions])
            story.append(Paragraph(precautions_text, normal_style))
        else:
            story.append(Paragraph("No precautions provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        # Medications
        story.append(Paragraph("Medications", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if medications:
            medications_text = "".join([f"• {escape_for_pdf(medication)}<br/>" for medication in medications])
            story.append(Paragraph(medications_text, normal_style))
        else:
            story.append(Paragraph("No medications provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        # Recommended Lab Tests
        story.append(Paragraph("Recommended Lab Tests", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if lab_tests:
            lab_tests_text = "".join([f"• {escape_for_pdf(test)}<br/>" for test in lab_tests])
            story.append(Paragraph(lab_tests_text, normal_style))
        else:
            story.append(Paragraph("No lab tests recommended for this condition.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        # Lifestyle Changes
        story.append(Paragraph("Lifestyle Changes", subheading_style))

        # Dietary Recommendations
        story.append(Paragraph("Dietary Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if diet:
            diet_text = "".join([f"• {escape_for_pdf(diet_item)}<br/>" for diet_item in diet])
            story.append(Paragraph(diet_text, normal_style))
        else:
            story.append(Paragraph("No dietary recommendations provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        # Exercise Recommendations
        story.append(Paragraph("Exercise Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if workouts:
            workouts_text = "".join([f"• {escape_for_pdf(workout_item)}<br/>" for workout_item in workouts])
            story.append(Paragraph(workouts_text, normal_style))
        else:
            story.append(Paragraph("No exercise recommendations provided.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        # Important Notes
        story.append(Paragraph("Important Notes", heading_style))
        story.append(Paragraph(
            "This report is intended for informational purposes only and should not replace professional medical advice. "
            "Please share this report with your doctor for a comprehensive evaluation and personalized treatment plan.",
            normal_style
        ))
        story.append(Spacer(1, 0.1 * inch))

        # Contact Information
        contact_info = (
            "For further assistance, contact us at:<br/>"
            "• <b>Email:</b> <link href='mailto:support@healthcenter.com' color='blue'>support@healthcenter.com</link><br/>"
            "• <b>Phone:</b> (123) 456-7890<br/>"
            "• <b>Website:</b> <link href='https://healthcenter.com' color='blue'>healthcenter.com</link>"
        )
        story.append(Paragraph(contact_info, normal_style))

        # Build the PDF
        doc.build(story)

        # Check if PDF was generated
        if not os.path.exists(pdf_file_path):
            return jsonify({"error": "PDF generation failed"}), 500

        # Send the PDF file as a response
        response = send_file(
            pdf_file_path,
            as_attachment=True,
            download_name="health_report.pdf",
            mimetype='application/pdf'
        )

        # Clean up temporary files
        try:
            for file_path in [pdf_file_path]:
                if os.path.exists(file_path):
                    os.remove(file_path)
            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)
        except Exception as cleanup_error:
            print(f"Cleanup error: {cleanup_error}")

        return response

    except Exception as e:
        print(f"Error in render_latex: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)
# pres



