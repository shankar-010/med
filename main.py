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



# from flask import Flask, request, render_template, jsonify, send_file
# import numpy as np
# import pandas as pd
# import pickle
# import sqlite3
# from datetime import datetime
# import json
# import os
# import tempfile
# import uuid
# from reportlab.lib.pagesizes import A4
# from reportlab.lib import colors
# from reportlab.lib.units import inch
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# app = Flask(__name__)

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

# init_db()

# sym_des = pd.read_csv("dataset/symtoms_df.csv")
# precautions = pd.read_csv("dataset/precautions_df.csv")
# workout = pd.read_csv("dataset/workout_df.csv")
# description = pd.read_csv("dataset/description.csv")
# medications = pd.read_csv('dataset/medications.csv')
# diets = pd.read_csv("dataset/diets.csv")

# svc = pickle.load(open('model/svc.pkl', 'rb'))

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

#     tests = LAB_TESTS.get(dis, [])

#     return desc, pre, med, die, wrkout, tests

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

# def get_predicted_value(patient_symptoms):
#     input_vector = np.zeros(len(symptoms_dict))
#     valid_symptoms = []

#     for item in patient_symptoms:
#         if item and item in symptoms_dict:
#             valid_symptoms.append(item)
#             input_vector[symptoms_dict[item]] = 1

#     if not valid_symptoms:
#         raise ValueError("No valid symptoms provided.")

#     prediction = svc.predict([input_vector])[0]
#     print(f"Input vector: {input_vector}, Prediction: {prediction}, Disease: {diseases_list[prediction]}")
#     return diseases_list[prediction]

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

# # Helper function to escape HTML-like characters for reportlab (similar to LaTeX escaping but for PDF rendering)
# def escape_for_pdf(text):
#     if not isinstance(text, str):
#         text = str(text)
#     # Replace special characters that might cause issues in reportlab
#     replacements = {
#         '&': '&amp;',
#         '<': '&lt;',
#         '>': '&gt;',
#     }
#     for char, escaped in replacements.items():
#         text = text.replace(char, escaped)
#     return text

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     conn = sqlite3.connect('healthytic.db')
#     c = conn.cursor()
#     c.execute("SELECT disease, test_name, test_result, test_date FROM lab_test_results ORDER BY created_at DESC")
#     test_history = [{"disease": row[0], "test_name": row[1], "test_result": row[2], "test_date": row[3]} for row in c.fetchall()]
#     conn.close()

#     default_values = {
#         'message': None,
#         'predicted_disease': None,
#         'static_hospitals': [],
#         'dis_des': None,
#         'my_precautions': [],
#         'medications': [],
#         'workout': [],
#         'my_diet': [],
#         'show_hospitals': False,
#         'symptoms_dict': symptoms_dict,
#         'recommended_tests': [],
#         'test_history': test_history,
#         'user_symptoms': []
#     }

#     if request.method == 'POST':
#         symptoms = request.form.get('symptoms', '').strip()
#         if not symptoms or symptoms.lower() == "symptoms":
#             print("No symptoms provided")
#             return render_template('index.html', **default_values, message="Please provide valid symptoms (comma-separated).")

#         user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
#         print(f"User Symptoms (from form or chatbot): {user_symptoms}")

#         try:
#             # Validate symptoms before prediction
#             valid_symptoms = [s for s in user_symptoms if s in symptoms_dict]
#             invalid_symptoms = [s for s in user_symptoms if s not in symptoms_dict]
#             if not valid_symptoms:
#                 print(f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}")
#                 return render_template('index.html', **default_values, message=f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}. Please use exact symptom names (e.g., chest_pain, high_fever).")

#             predicted_disease = get_predicted_value(user_symptoms)
#             print(f"Predicted Disease: '{predicted_disease}'")
#             dis_des, my_precautions, medications, my_diet, workout, recommended_tests = helper(predicted_disease)

#             my_precautions = [str(i) for i in my_precautions if i]
#             medications = [str(i) for i in medications if i]
#             my_diet = [str(i) for i in my_diet if i]
#             workout = [str(i) for i in workout if i]
#             recommended_tests = [str(i) for i in recommended_tests if i]
#             user_symptoms = [str(i) for i in user_symptoms if i]

#             hospital_diseases = [
#                 "Heart attack", "Allergy", "Pneumonia", "Tuberculosis", "Malaria", "Dengue", "Typhoid",
#                 "hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "AIDS"
#             ]
#             show_hospitals = predicted_disease in hospital_diseases
#             static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []

#             render_data = {
#                 'message': None,
#                 'predicted_disease': str(predicted_disease) if predicted_disease else "Not available",
#                 'static_hospitals': static_hospitals if static_hospitals else [],
#                 'dis_des': str(dis_des) if dis_des else "Not available",
#                 'my_precautions': my_precautions if my_precautions else [],
#                 'medications': medications if medications else [],
#                 'workout': workout if workout else [],
#                 'my_diet': my_diet if my_diet else [],
#                 'show_hospitals': show_hospitals,
#                 'symptoms_dict': symptoms_dict,
#                 'recommended_tests': recommended_tests if recommended_tests else [],
#                 'test_history': test_history,
#                 'user_symptoms': user_symptoms if user_symptoms else []
#             }

#             try:
#                 json.dumps(render_data['user_symptoms'])
#                 json.dumps(render_data['medications'])
#                 json.dumps(render_data['my_precautions'])
#                 json.dumps(render_data['workout'])
#                 json.dumps(render_data['my_diet'])
#                 json.dumps(render_data['recommended_tests'])
#                 json.dumps(render_data['static_hospitals'])
#                 print("All data serialized successfully")
#             except Exception as e:
#                 print(f"Serialization error: {str(e)}")
#                 print(f"Problematic data: {render_data}")
#                 return render_template('index.html', **default_values, message=f"Data serialization error: {str(e)}")

#             print("Rendering template with:", render_data)
#             return render_template('index.html', **render_data)

#         except ValueError as e:
#             print(f"ValueError: {str(e)}")
#             return render_template('index.html', **default_values, message=str(e))

#         except KeyError as e:
#             print(f"KeyError: {str(e)}")
#             return render_template('index.html', **default_values, message=f"Invalid symptom provided: {str(e)}. Please check your input.")

#         except Exception as e:
#             print(f"Unexpected error: {str(e)}")
#             return render_template('index.html', **default_values, message=f"An unexpected error occurred: {str(e)}")

#     print("Rendering index.html for GET request")
#     return render_template('index.html', **default_values)

# @app.route('/submit_lab_test', methods=['POST'])
# def submit_lab_test():
#     try:
#         data = request.get_json()
#         disease = data.get('disease')
#         test_name = data.get('test_name')
#         test_result = data.get('test_result')
#         test_date = data.get('test_date')
#         created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         if not all([disease, test_name, test_result, test_date]):
#             return jsonify({"error": "All fields are required"}), 400

#         conn = sqlite3.connect('healthytic.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO lab_test_results (disease, test_name, test_result, test_date, created_at) VALUES (?, ?, ?, ?, ?)",
#                   (disease, test_name, test_result, test_date, created_at))
#         conn.commit()
#         conn.close()

#         return jsonify({"message": "Lab test result submitted successfully"}), 200
#     except Exception as e:
#         print(f"Error submitting lab test: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/generate_report', methods=['POST'])
# def generate_report():
#     try:
#         data = request.get_json()
#         symptoms = data.get('symptoms', [])
#         predicted_disease = data.get('predicted_disease', 'Unknown')
#         description = data.get('description', 'No description available.')
#         precautions = data.get('precautions', [])
#         medications = data.get('medications', [])
#         diet = data.get('diet', [])
#         workouts = data.get('workouts', [])
#         lab_tests = data.get('lab_tests', [])

#         # Instead of generating LaTeX, return the raw data as JSON
#         report_data = {
#             "symptoms": symptoms,
#             "predicted_disease": predicted_disease,
#             "description": description,
#             "precautions": precautions,
#             "medications": medications,
#             "diet": diet,
#             "workouts": workouts,
#             "lab_tests": lab_tests,
#             "generated_date": datetime.now().strftime("%B %d, %Y")
#         }

#         return jsonify({"report_data": report_data}), 200
#     except Exception as e:
#         print(f"Error generating report: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/render_latex', methods=['POST'])
# def render_latex():
#     try:
#         # Get the report data from the request (previously sent by /generate_report)
#         data = request.get_json()
#         if not data or 'report_data' not in data:
#             return jsonify({"error": "No report data provided"}), 400

#         report_data = data['report_data']
#         symptoms = report_data.get('symptoms', [])
#         predicted_disease = report_data.get('predicted_disease', 'Unknown')
#         description = report_data.get('description', 'No description available.')
#         precautions = report_data.get('precautions', [])
#         medications = report_data.get('medications', [])
#         diet = report_data.get('diet', [])
#         workouts = report_data.get('workouts', [])
#         lab_tests = report_data.get('lab_tests', [])
#         generated_date = report_data.get('generated_date', datetime.now().strftime("%B %d, %Y"))

#         # Create a unique temporary directory for this request
#         temp_dir = tempfile.mkdtemp()
#         unique_id = str(uuid.uuid4())
#         pdf_file_path = os.path.join(temp_dir, f"report_{unique_id}.pdf")

#         # Create a PDF using reportlab
#         doc = SimpleDocTemplate(pdf_file_path, pagesize=A4, leftMargin=1*inch, rightMargin=1*inch, topMargin=1*inch, bottomMargin=1*inch)
#         styles = getSampleStyleSheet()

#         # Define custom styles
#         title_style = ParagraphStyle(
#             'TitleStyle',
#             parent=styles['Heading1'],
#             fontSize=16,
#             spaceAfter=12,
#             alignment=1  # Center
#         )
#         heading_style = ParagraphStyle(
#             'HeadingStyle',
#             parent=styles['Heading2'],
#             fontSize=14,
#             spaceAfter=10
#         )
#         subheading_style = ParagraphStyle(
#             'SubheadingStyle',
#             parent=styles['Heading3'],
#             fontSize=12,
#             spaceAfter=8
#         )
#         normal_style = ParagraphStyle(
#             'NormalStyle',
#             parent=styles['Normal'],
#             fontSize=10,
#             spaceAfter=6,
#             leading=12
#         )

#         story = []

#         # Header (mimicking fancyhdr)
#         story.append(Paragraph("Healthytic Health Report", title_style))
#         story.append(Paragraph(f"Generated on: {generated_date}", normal_style))
#         story.append(Spacer(1, 0.3 * inch))

#         # Patient Health Summary
#         story.append(Paragraph("Patient Health Summary", heading_style))
#         story.append(Paragraph(
#             "This report is generated by Healthytic, an AI-driven health insight platform. "
#             "It provides a summary of your symptoms, predicted condition, and recommended care plan. "
#             "Please consult a healthcare professional for a thorough diagnosis and treatment.",
#             normal_style
#         ))
#         story.append(Spacer(1, 0.2 * inch))

#         # Symptom Summary
#         story.append(Paragraph("Symptom Summary", subheading_style))
#         if symptoms:
#             symptoms_text = "".join([f"• {escape_for_pdf(symptom.replace('_', ' ').capitalize())}<br/>" for symptom in symptoms])
#             story.append(Paragraph(symptoms_text, normal_style))
#         else:
#             story.append(Paragraph("No symptoms provided.", normal_style))
#         story.append(Spacer(1, 0.2 * inch))

#         # Predicted Condition
#         story.append(Paragraph("Predicted Condition", subheading_style))
#         story.append(Paragraph(f"<b>{escape_for_pdf(predicted_disease)}</b>", normal_style))
#         story.append(Paragraph(f"<i>Description:</i> {escape_for_pdf(description)}", normal_style))
#         story.append(Spacer(1, 0.2 * inch))

#         # Suggested Care Plan
#         story.append(Paragraph("Suggested Care Plan", subheading_style))

#         # Precautions
#         story.append(Paragraph("Precautions", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
#         if precautions:
#             precautions_text = "".join([f"• {escape_for_pdf(precaution)}<br/>" for precaution in precautions])
#             story.append(Paragraph(precautions_text, normal_style))
#         else:
#             story.append(Paragraph("No precautions provided.", normal_style))
#         story.append(Spacer(1, 0.1 * inch))

#         # Medications
#         story.append(Paragraph("Medications", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
#         if medications:
#             medications_text = "".join([f"• {escape_for_pdf(medication)}<br/>" for medication in medications])
#             story.append(Paragraph(medications_text, normal_style))
#         else:
#             story.append(Paragraph("No medications provided.", normal_style))
#         story.append(Spacer(1, 0.1 * inch))

#         # Recommended Lab Tests
#         story.append(Paragraph("Recommended Lab Tests", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
#         if lab_tests:
#             lab_tests_text = "".join([f"• {escape_for_pdf(test)}<br/>" for test in lab_tests])
#             story.append(Paragraph(lab_tests_text, normal_style))
#         else:
#             story.append(Paragraph("No lab tests recommended for this condition.", normal_style))
#         story.append(Spacer(1, 0.2 * inch))

#         # Lifestyle Changes
#         story.append(Paragraph("Lifestyle Changes", subheading_style))

#         # Dietary Recommendations
#         story.append(Paragraph("Dietary Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
#         if diet:
#             diet_text = "".join([f"• {escape_for_pdf(diet_item)}<br/>" for diet_item in diet])
#             story.append(Paragraph(diet_text, normal_style))
#         else:
#             story.append(Paragraph("No dietary recommendations provided.", normal_style))
#         story.append(Spacer(1, 0.1 * inch))

#         # Exercise Recommendations
#         story.append(Paragraph("Exercise Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
#         if workouts:
#             workouts_text = "".join([f"• {escape_for_pdf(workout_item)}<br/>" for workout_item in workouts])
#             story.append(Paragraph(workouts_text, normal_style))
#         else:
#             story.append(Paragraph("No exercise recommendations provided.", normal_style))
#         story.append(Spacer(1, 0.2 * inch))

#         # Important Notes
#         story.append(Paragraph("Important Notes", heading_style))
#         story.append(Paragraph(
#             "This report is intended for informational purposes only and should not replace professional medical advice. "
#             "Please share this report with your doctor for a comprehensive evaluation and personalized treatment plan.",
#             normal_style
#         ))
#         story.append(Spacer(1, 0.1 * inch))

#         # Contact Information
#         contact_info = (
#             "For further assistance, contact us at:<br/>"
#             "• <b>Email:</b> <link href='mailto:support@healthcenter.com' color='blue'>support@healthcenter.com</link><br/>"
#             "• <b>Phone:</b> (123) 456-7890<br/>"
#             "• <b>Website:</b> <link href='https://healthcenter.com' color='blue'>healthcenter.com</link>"
#         )
#         story.append(Paragraph(contact_info, normal_style))

#         # Build the PDF
#         doc.build(story)

#         # Check if PDF was generated
#         if not os.path.exists(pdf_file_path):
#             return jsonify({"error": "PDF generation failed"}), 500

#         # Send the PDF file as a response
#         response = send_file(
#             pdf_file_path,
#             as_attachment=True,
#             download_name="health_report.pdf",
#             mimetype='application/pdf'
#         )

#         # Clean up temporary files
#         try:
#             for file_path in [pdf_file_path]:
#                 if os.path.exists(file_path):
#                     os.remove(file_path)
#             if os.path.exists(temp_dir):
#                 os.rmdir(temp_dir)
#         except Exception as cleanup_error:
#             print(f"Cleanup error: {cleanup_error}")

#         return response

#     except Exception as e:
#         print(f"Error in render_latex: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/developer')
# def developer():
#     return render_template('developer.html')

# @app.route('/blog')
# def blog():
#     return render_template('blog.html')

# if __name__ == "__main__":
#     app.run(debug=True)
# pres



import numpy as np
import pandas as pd
from sklearn.svm import SVC
from flask import Flask, request, render_template, jsonify, send_file, session, redirect, url_for
import pickle
import sqlite3
from datetime import datetime
import json
import os
import tempfile
import uuid
import logging
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secure-random-key-12345'  # Replace with a secure key in production

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Directory for storing uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('healthytic.db')
    c = conn.cursor()
    # Lab test results table
    c.execute('''CREATE TABLE IF NOT EXISTS lab_test_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    disease TEXT NOT NULL,
                    test_name TEXT NOT NULL,
                    test_result TEXT NOT NULL,
                    test_date TEXT NOT NULL,
                    created_at TEXT NOT NULL
                 )''')
    # Users table for authentication
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                 )''')
    # Health locker documents table
    c.execute('''CREATE TABLE IF NOT EXISTS health_locker (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    document_type TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    upload_date TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                 )''')
    conn.commit()
    conn.close()

init_db()

# Load datasets and model
try:
    sym_des = pd.read_csv("dataset/symtoms_df.csv")
    precautions = pd.read_csv("dataset/precautions_df.csv")
    workout = pd.read_csv("dataset/workout_df.csv")
    description = pd.read_csv("dataset/description.csv")
    medications = pd.read_csv('dataset/medications.csv')
    diets = pd.read_csv("dataset/diets.csv")
    svc = pickle.load(open('model/svc.pkl', 'rb'))
except Exception as e:
    logger.error(f"Error loading datasets or model: {str(e)}")
    raise

# Define lab tests for diseases
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
    "AIDS": ["HIV Test", "CD4 Count", "Viral Load Test"],
    "Fungal infection": ["Skin Scraping Test", "Fungal Culture"],
    "GERD": ["Endoscopy", "pH Monitoring"],
    "Chronic cholestasis": ["Liver Function Test", "Ultrasound"],
    "Drug Reaction": ["Patch Test", "Blood Test"],
    "Peptic ulcer diseae": ["Endoscopy", "H. pylori Test"],
    "Gastroenteritis": ["Stool Culture", "Blood Test"],
    "Migraine": ["MRI", "CT Scan"],
    "Cervical spondylosis": ["X-Ray", "MRI"],
    "Paralysis (brain hemorrhage)": ["CT Scan", "MRI"],
    "Jaundice": ["Liver Function Test", "Bilirubin Test"],
    "Chicken pox": ["Blood Test", "Viral Culture"],
    "Common Cold": ["Throat Swab", "Blood Test"],
    "Dimorphic hemmorhoids(piles)": ["Colonoscopy", "Sigmoidoscopy"],
    "Varicose veins": ["Doppler Ultrasound", "Venous Duplex Scan"],
    "Hypothyroidism": ["TSH Test", "T4 Test"],
    "Hyperthyroidism": ["TSH Test", "T3/T4 Test"],
    "Hypoglycemia": ["Blood Glucose Test", "HbA1c Test"],
    "Osteoarthristis": ["X-Ray", "MRI"],
    "Arthritis": ["Rheumatoid Factor Test", "X-Ray"],
    "(vertigo) Paroymsal  Positional Vertigo": ["Dix-Hallpike Test", "MRI"],
    "Acne": ["Skin Biopsy", "Hormone Level Test"],
    "Urinary tract infection": ["Urinalysis", "Urine Culture"],
    "Psoriasis": ["Skin Biopsy", "Blood Test"],
    "Impetigo": ["Bacterial Culture", "Skin Swab"]
}

# Define static hospitals (expanded)
STATIC_HOSPITALS = {
    "Heart attack": [
        {"name": "Cardiac Care Boston", "address": "123 Heartbeat Rd, Boston, MA", "specialty": "Cardiology", "phone": "555-333-4444", "website": "http://cardiaccare.com"},
        {"name": "NYC Heart Institute", "address": "456 Pulse Ave, New York, NY", "specialty": "Cardiology", "phone": "555-444-5555", "website": "http://nycheart.com"}
    ],
    "Allergy": [
        {"name": "Allergy Clinic Boston", "address": "789 Sneeze Rd, Boston, MA", "specialty": "Immunology", "phone": "555-111-2222", "website": "http://allergyclinic.com"},
        {"name": "Allergy Specialists NYC", "address": "321 Itch Blvd, New York, NY", "specialty": "Allergy", "phone": "555-222-3333", "website": "http://allergyexperts.com"}
    ],
    "Pneumonia": [
        {"name": "Boston Pulmonary Center", "address": "101 Lung St, Boston, MA", "specialty": "Pulmonology", "phone": "555-555-6666", "website": "http://bostonpulmonary.com"}
    ],
    "Tuberculosis": [
        {"name": "NYC TB Clinic", "address": "202 Cough Ave, New York, NY", "specialty": "Infectious Diseases", "phone": "555-666-7777", "website": "http://nyctbclinic.com"}
    ],
    "Malaria": [
        {"name": "Tropical Disease Center", "address": "303 Fever Rd, Miami, FL", "specialty": "Infectious Diseases", "phone": "555-777-8888", "website": "http://tropicaldisease.com"}
    ],
    "Dengue": [
        {"name": "Miami Dengue Specialists", "address": "404 Mosquito Ln, Miami, FL", "specialty": "Infectious Diseases", "phone": "555-888-9999", "website": "http://denguespecialists.com"}
    ],
    "Typhoid": [
        {"name": "Infectious Disease Clinic", "address": "505 Bacteria St, Chicago, IL", "specialty": "Infectious Diseases", "phone": "555-999-0000", "website": "http://infectiousdisease.com"}
    ],
    "hepatitis A": [
        {"name": "Liver Health Clinic", "address": "606 Hepa Rd, Los Angeles, CA", "specialty": "Hepatology", "phone": "555-000-1111", "website": "http://liverhealth.com"}
    ],
    "Hepatitis B": [
        {"name": "Hepatitis Center", "address": "707 Hepb Ave, San Francisco, CA", "specialty": "Hepatology", "phone": "555-111-2222", "website": "http://hepatitiscenter.com"}
    ],
    "Hepatitis C": [
        {"name": "HCV Treatment Center", "address": "808 Hepc Blvd, Seattle, WA", "specialty": "Hepatology", "phone": "555-222-3333", "website": "http://hcvcenter.com"}
    ],
    "Hepatitis D": [
        {"name": "Advanced Liver Care", "address": "909 Hepd St, Portland, OR", "specialty": "Hepatology", "phone": "555-333-4444", "website": "http://advancedlivercare.com"}
    ],
    "Hepatitis E": [
        {"name": "Hep E Specialists", "address": "1010 Hepe Ln, Denver, CO", "specialty": "Hepatology", "phone": "555-444-5555", "website": "http://hepespecialists.com"}
    ],
    "AIDS": [
        {"name": "HIV/AIDS Clinic", "address": "1111 Immune Rd, Atlanta, GA", "specialty": "Infectious Diseases", "phone": "555-555-6666", "website": "http://hivclinic.com"}
    ]
}

# Define symptoms and diseases
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
    'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119,
    'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124,
    'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128,
    'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
}

diseases_list = {
    15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction',
    33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma',
    23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'viral fever',
    28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A',
    19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis',
    36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack',
    39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis',
    5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection',
    35: 'Psoriasis', 27: 'Impetigo'
}

# Helper functions
def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc]) if not desc.empty else "No description available."

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values.flatten() if pd.notna(col)] if not pre.empty else ["Consult a doctor"]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [m for m in med.values.flatten() if pd.notna(m)] if not med.empty else ["Consult a doctor"]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [d for d in die.values.flatten() if pd.notna(d)] if not die.empty else ["Balanced diet"]

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = [w for w in wrkout.values if pd.notna(w)] if not wrkout.empty else ["Rest"]

    tests = LAB_TESTS.get(dis, [])

    return desc, pre, med, die, wrkout, tests

def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    valid_symptoms = []

    for item in patient_symptoms:
        if item and item in symptoms_dict:
            valid_symptoms.append(item)
            input_vector[symptoms_dict[item]] = 1

    if not valid_symptoms:
        raise ValueError("No valid symptoms provided.")

    feature_names = list(symptoms_dict.keys())
    input_df = pd.DataFrame([input_vector], columns=feature_names)

    prediction = svc.predict(input_df)[0]
    logger.info(f"Input vector: {input_vector}, Prediction: {prediction}, Disease: {diseases_list[prediction]}")
    return diseases_list[prediction]

def escape_for_pdf(text):
    if not isinstance(text, str):
        text = str(text)
    replacements = {
        '&': '&',
        '<': '<',
        '>': '>',
    }
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    return text

# Default values for rendering
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
    'test_history': [],
    'health_locker_documents': [],
    'user_symptoms': []
}

# Authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect('healthytic.db')
        c = conn.cursor()
        c.execute("SELECT id, username FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            logger.info(f"User {username} logged in successfully")
            return redirect(url_for('index'))
        else:
            logger.warning(f"Failed login attempt for username: {username}")
            return render_template('login.html', message="Invalid username or password")

    return render_template('login.html', message=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('register.html', message="Username and password are required")

        try:
            conn = sqlite3.connect('healthytic.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            logger.info(f"User {username} registered successfully")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            logger.warning(f"Registration failed: Username {username} already exists")
            return render_template('register.html', message="Username already exists")

    return render_template('register.html', message=None)

@app.route('/logout')
def logout():
    username = session.get('username', 'Unknown')
    session.pop('user_id', None)
    session.pop('username', None)
    logger.info(f"User {username} logged out")
    return redirect(url_for('index'))

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    # Fetch lab test history
    conn = sqlite3.connect('healthytic.db')
    c = conn.cursor()
    c.execute("SELECT disease, test_name, test_result, test_date FROM lab_test_results ORDER BY created_at DESC")
    test_history = [{"disease": row[0], "test_name": row[1], "test_result": row[2], "test_date": row[3]} for row in c.fetchall()]

    # Fetch health locker documents if user is logged in
    health_locker_documents = []
    if 'user_id' in session:
        c.execute("SELECT id, document_type, upload_date FROM health_locker WHERE user_id = ? ORDER BY upload_date DESC", (session['user_id'],))
        health_locker_documents = [{"id": row[0], "document_type": row[1], "upload_date": row[2]} for row in c.fetchall()]
    conn.close()

    default_values.update({
        'test_history': test_history,
        'health_locker_documents': health_locker_documents,
        'is_logged_in': 'user_id' in session
    })

    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '').strip()
        if not symptoms or symptoms.lower() == "symptoms":
            logger.warning("No symptoms provided in POST request")
            return render_template('index.html', **default_values, message="Please provide valid symptoms (comma-separated).")

        user_symptoms = [s.strip() for s in symptoms.split(',') if s.strip()]
        logger.info(f"User Symptoms: {user_symptoms}")

        try:
            valid_symptoms = [s for s in user_symptoms if s in symptoms_dict]
            invalid_symptoms = [s for s in user_symptoms if s not in symptoms_dict]
            if not valid_symptoms:
                logger.warning(f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}")
                return render_template('index.html', **default_values, message=f"No valid symptoms found. Invalid symptoms: {invalid_symptoms}. Please use exact symptom names (e.g., chest_pain, high_fever).")

            predicted_disease = get_predicted_value(user_symptoms)
            dis_des, my_precautions, medications, my_diet, workout, recommended_tests = helper(predicted_disease)

            my_precautions = [str(i) for i in my_precautions if i]
            medications = [str(i) for i in medications if i]
            my_diet = [str(i) for i in my_diet if i]
            workout = [str(i) for i in workout if i]
            recommended_tests = [str(i) for i in recommended_tests if i]
            user_symptoms = [str(i) for i in user_symptoms if i]

            hospital_diseases = list(STATIC_HOSPITALS.keys())
            show_hospitals = predicted_disease in hospital_diseases
            static_hospitals = STATIC_HOSPITALS.get(predicted_disease, []) if show_hospitals else []

            render_data = {
                'message': None,
                'predicted_disease': str(predicted_disease) if predicted_disease else "Not available",
                'static_hospitals': static_hospitals,
                'dis_des': str(dis_des) if dis_des else "Not available",
                'my_precautions': my_precautions,
                'medications': medications,
                'workout': workout,
                'my_diet': my_diet,
                'show_hospitals': show_hospitals,
                'symptoms_dict': symptoms_dict,
                'recommended_tests': recommended_tests,
                'test_history': test_history,
                'health_locker_documents': health_locker_documents,
                'user_symptoms': user_symptoms,
                'is_logged_in': 'user_id' in session
            }

            try:
                json.dumps(render_data['user_symptoms'])
                json.dumps(render_data['medications'])
                json.dumps(render_data['my_precautions'])
                json.dumps(render_data['workout'])
                json.dumps(render_data['my_diet'])
                json.dumps(render_data['recommended_tests'])
                json.dumps(render_data['static_hospitals'])
                logger.info("All data serialized successfully")
            except Exception as e:
                logger.error(f"Serialization error: {str(e)}")
                return render_template('index.html', **default_values, message=f"Data serialization error: {str(e)}")

            logger.info("Rendering template with data")
            return render_template('index.html', **render_data)

        except ValueError as e:
            logger.error(f"ValueError: {str(e)}")
            return render_template('index.html', **default_values, message=str(e))

        except KeyError as e:
            logger.error(f"KeyError: {str(e)}")
            return render_template('index.html', **default_values, message=f"Invalid symptom provided: {str(e)}. Please check your input.")

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return render_template('index.html', **default_values, message=f"An unexpected error occurred: {str(e)}")

    logger.info("Rendering index.html for GET request")
    return render_template('index.html', **default_values)

# Submit lab test route
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
            logger.warning("Missing required fields in lab test submission")
            return jsonify({"error": "All fields are required"}), 400

        try:
            datetime.strptime(test_date, '%Y-%m-%d')
        except ValueError:
            logger.warning(f"Invalid test date format: {test_date}")
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        conn = sqlite3.connect('healthytic.db')
        c = conn.cursor()
        c.execute("SELECT id FROM lab_test_results WHERE disease = ? AND test_name = ? AND test_date = ?",
                  (disease, test_name, test_date))
        if c.fetchone():
            conn.close()
            logger.warning(f"Duplicate lab test entry: {disease}, {test_name}, {test_date}")
            return jsonify({"error": "A test with the same disease, name, and date already exists"}), 400

        c.execute("INSERT INTO lab_test_results (disease, test_name, test_result, test_date, created_at) VALUES (?, ?, ?, ?, ?)",
                  (disease, test_name, test_result, test_date, created_at))
        conn.commit()
        conn.close()
        logger.info(f"Lab test submitted: {disease}, {test_name}")
        return jsonify({"message": "Lab test result submitted successfully"}), 200

    except Exception as e:
        logger.error(f"Error submitting lab test: {str(e)}")
        return jsonify({"error": str(e)}), 500

# File upload helper
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Health locker document upload
@app.route('/upload_document', methods=['POST'])
def upload_document():
    logger.info(f"Session data on upload_document: {session}")
    if 'user_id' not in session:
        logger.warning("Unauthorized document upload attempt")
        return jsonify({"error": "Please log in to upload documents", "redirect": url_for('login')}), 401

    if 'document_file' not in request.files or 'document_type' not in request.form:
        logger.warning("Missing document file or type in upload request")
        return jsonify({"error": "Document file and type are required"}), 400

    file = request.files['document_file']
    document_type = request.form['document_type']

    if file.filename == '':
        logger.warning("No file selected for upload")
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        logger.warning(f"Invalid file type uploaded: {file.filename}")
        return jsonify({"error": "Invalid file type. Allowed types: pdf, jpg, jpeg, png"}), 400

    try:
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)

        upload_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('healthytic.db')
        c = conn.cursor()
        c.execute("INSERT INTO health_locker (user_id, document_type, file_path, upload_date) VALUES (?, ?, ?, ?)",
                  (session['user_id'], document_type, file_path, upload_date))
        conn.commit()
        conn.close()

        logger.info(f"Document uploaded by user {session['username']}: {unique_filename}")
        return jsonify({"message": "Document uploaded successfully"}), 200

    except Exception as e:
        logger.error(f"Error uploading document: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Download document
@app.route('/download_document/<int:doc_id>')
def download_document(doc_id):
    if 'user_id' not in session:
        logger.warning("Unauthorized document download attempt")
        return redirect(url_for('login'))

    try:
        conn = sqlite3.connect('healthytic.db')
        c = conn.cursor()
        c.execute("SELECT file_path, document_type FROM health_locker WHERE id = ? AND user_id = ?", (doc_id, session['user_id']))
        doc = c.fetchone()
        conn.close()

        if not doc:
            logger.warning(f"Document not found or unauthorized access: ID {doc_id}")
            return "Document not found or unauthorized", 404

        file_path, document_type = doc
        return send_file(file_path, as_attachment=True, download_name=f"{document_type}_{doc_id}.{file_path.rsplit('.', 1)[1]}")

    except Exception as e:
        logger.error(f"Error downloading document {doc_id}: {str(e)}")
        return str(e), 500

# Generate report (JSON data)
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

        logger.info("Report data generated successfully")
        return jsonify({"report_data": report_data}), 200

    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Render PDF report
@app.route('/render_latex', methods=['POST'])
def render_latex():
    try:
        data = request.get_json()
        if not data or 'report_data' not in data:
            logger.warning("No report data provided for PDF rendering")
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

        temp_dir = tempfile.mkdtemp()
        unique_id = str(uuid.uuid4())
        pdf_file_path = os.path.join(temp_dir, f"report_{unique_id}.pdf")

        doc = SimpleDocTemplate(pdf_file_path, pagesize=A4, leftMargin=1*inch, rightMargin=1*inch, topMargin=1*inch, bottomMargin=1*inch)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, spaceAfter=12, alignment=1)
        heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=14, spaceAfter=10)
        subheading_style = ParagraphStyle('SubheadingStyle', parent=styles['Heading3'], fontSize=12, spaceAfter=8)
        normal_style = ParagraphStyle('NormalStyle', parent=styles['Normal'], fontSize=10, spaceAfter=6, leading=12)

        def add_watermark(canvas, doc):
            canvas.saveState()
            canvas.setFont("Helvetica", 40)
            canvas.setFillColor(colors.grey, alpha=0.1)
            canvas.rotate(45)
            canvas.drawString(3 * inch, -2 * inch, "Healthytic")
            canvas.restoreState()

        story = []

        story.append(Paragraph("Healthytic Health Report", title_style))
        story.append(Paragraph(f"Generated on: {generated_date}", normal_style))
        story.append(Spacer(1, 0.3 * inch))

        story.append(Paragraph("Patient Health Summary", heading_style))
        story.append(Paragraph(
            "This report is generated by Healthytic, an AI-driven health insight platform. "
            "It provides a summary of your symptoms, predicted condition, and recommended care plan. "
            "Please consult a healthcare professional for a thorough diagnosis and treatment.",
            normal_style
        ))
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph("Symptom Summary", subheading_style))
        if symptoms:
            symptoms_text = "".join([f"• {escape_for_pdf(symptom.replace('_', ' ').capitalize())}<br/>" for symptom in symptoms])
            story.append(Paragraph(symptoms_text, normal_style))
        else:
            story.append(Paragraph("No symptoms provided.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph("Predicted Condition", subheading_style))
        story.append(Paragraph(f"<b>{escape_for_pdf(predicted_disease)}</b>", normal_style))
        story.append(Paragraph(f"<i>Description:</i> {escape_for_pdf(description)}", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph("Suggested Care Plan", subheading_style))

        story.append(Paragraph("Precautions", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if precautions:
            precautions_text = "".join([f"• {escape_for_pdf(precaution)}<br/>" for precaution in precautions])
            story.append(Paragraph(precautions_text, normal_style))
        else:
            story.append(Paragraph("No precautions provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        story.append(Paragraph("Medications", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if medications:
            medications_text = "".join([f"• {escape_for_pdf(medication)}<br/>" for medication in medications])
            story.append(Paragraph(medications_text, normal_style))
        else:
            story.append(Paragraph("No medications provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        story.append(Paragraph("Recommended Lab Tests", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if lab_tests:
            lab_tests_text = "".join([f"• {escape_for_pdf(test)}<br/>" for test in lab_tests])
            story.append(Paragraph(lab_tests_text, normal_style))
        else:
            story.append(Paragraph("No lab tests recommended for this condition.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph("Lifestyle Changes", subheading_style))

        story.append(Paragraph("Dietary Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if diet:
            diet_text = "".join([f"• {escape_for_pdf(diet_item)}<br/>" for diet_item in diet])
            story.append(Paragraph(diet_text, normal_style))
        else:
            story.append(Paragraph("No dietary recommendations provided.", normal_style))
        story.append(Spacer(1, 0.1 * inch))

        story.append(Paragraph("Exercise Recommendations", ParagraphStyle('SubSubheading', parent=subheading_style, fontSize=11)))
        if workouts:
            workouts_text = "".join([f"• {escape_for_pdf(workout_item)}<br/>" for workout_item in workouts])
            story.append(Paragraph(workouts_text, normal_style))
        else:
            story.append(Paragraph("No exercise recommendations provided.", normal_style))
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph("Important Notes", heading_style))
        story.append(Paragraph(
            "This report is intended for informational purposes only and should not replace professional medical advice. "
            "Please share this report with your doctor for a comprehensive evaluation and personalized treatment plan.",
            normal_style
        ))
        story.append(Spacer(1, 0.1 * inch))

        contact_info = (
            "For further assistance, contact us at:<br/>"
            "• <b>Email:</b> <link href='mailto:support@healthcenter.com' color='blue'>support@healthcenter.com</link><br/>"
            "• <b>Phone:</b> (123) 456-7890<br/>"
            "• <b>Website:</b> <link href='https://healthcenter.com' color='blue'>healthcenter.com</link>"
        )
        story.append(Paragraph(contact_info, normal_style))

        doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)

        if not os.path.exists(pdf_file_path):
            logger.error("PDF generation failed")
            return jsonify({"error": "PDF generation failed"}), 500

        response = send_file(
            pdf_file_path,
            as_attachment=True,
            download_name="health_report.pdf",
            mimetype='application/pdf'
        )

        try:
            os.remove(pdf_file_path)
            os.rmdir(temp_dir)
        except Exception as cleanup_error:
            logger.warning(f"Cleanup error: {cleanup_error}")

        logger.info("PDF report generated and sent successfully")
        return response

    except Exception as e:
        logger.error(f"Error in render_latex: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Static pages
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