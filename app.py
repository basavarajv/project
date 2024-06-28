import streamlit as st
import os
import json
import time

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   page_icon="🧑‍⚕️")
# Path to the file where user credentials will be stored
CREDENTIALS_FILE = 'user_credentials.json'

# Load user credentials from the file
def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return {}
    else:
        return {}

# Save user credentials to the file
def save_credentials(credentials):
    with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
        json.dump(credentials, f)

# Load credentials at the start
user_credentials = load_credentials()

# Function to validate login credentials
def validate_login(username, password):
    return user_credentials.get(username) == password




# Function to register a new user
def register_user(username, password):
    if username in user_credentials:
        return False  # Username already exists
    user_credentials[username] = password
    save_credentials(user_credentials)
    return True


            
# Function to render the login page
def login_page():
    
    # Apply custom CSS for background image
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/004/747/818/original/global-network-medical-healthcare-system-protection-concept-futuristic-medical-health-protection-shield-icon-with-shining-wireframe-above-multiple-on-dark-blue-background-seamless-loop-4k-animation-free-video.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background: rgba(255, 255, 255, 0);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.title('User Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        elif not username or not password:
            st.error("Username and password cannot be empty")
        else:
            st.error("Invalid username or password")
    
    st.markdown("new user!! click below to register", unsafe_allow_html=True)
    if st.button("Go to Registration"):
        st.session_state.show_register = True
        st.rerun()

# Function to render the registration page
def register_page():
    
    # Apply custom CSS for background image
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/004/747/818/original/global-network-medical-healthcare-system-protection-concept-futuristic-medical-health-protection-shield-icon-with-shining-wireframe-above-multiple-on-dark-blue-background-seamless-loop-4k-animation-free-video.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background: rgba(255, 255, 255, 0);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    
    st.title('User Registration')
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
            
        elif not username or not password or not confirm_password:
            st.error("Fields cannot be empty")
            
        elif register_user(username, password):
            st.success("Registration successful! Please log in.")
            st.session_state.show_register = False
            time.sleep(5) 
            st.rerun()
        else:
            st.error("Username already exists")

    if st.button("Go to Login"):
        st.session_state.show_register = False
        st.rerun()

            
        

# Function to render the new page after login
def new_page():
    import pickle
    import streamlit as st
    from streamlit_option_menu import option_menu
    import numpy as np
    import pandas as pd

    # Load saved models
    diabetes_model = pickle.load(
        open('diabetes_model.sav', 'rb'))
    diabetes_model_scaler = pickle.load(
        open('diabetes_model_scaler.sav', 'rb'))
    heart_disease_model = pickle.load(
        open('heart_disease_model.sav', 'rb'))
    lung_cancer_model = pickle.load(
        open('lung_cancer_model.sav', 'rb'))
    lung_cancer_model_scaler = pickle.load(
        open('lung_cancer_model_scaler.sav', 'rb'))
    
    
    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            'Human Diseases Prediction System',
            ['Gestational Diabetes Prediction', 'Heart Disease Prediction', 'Lung Cancer Prediction'],
            menu_icon='hospital-fill',
            icons=['activity', 'heart', 'person'],
            default_index=0
            )




    # Diabetes Prediction Page
    if selected == 'Gestational Diabetes Prediction':
        # Apply custom CSS for background image
        page_bg_img = '''
        <style>
        body {
            background-image: url("https://thedaily.case.edu/wp-content/uploads/2023/12/glucose-meter-diabetes-feat.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background: rgba(255, 255, 255, 0);
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        '''

        st.markdown(page_bg_img, unsafe_allow_html=True)

        # Streamlit webpage
        st.title(' Gestational Diabetes Prediction')

        # Input fields
        st.header('Patient Information')
        pregnancies = st.number_input(
            'Pregnancies', min_value=0, max_value=20, value=0)
        glucose = st.number_input('Glucose', min_value=0, max_value=200, value=0)
        blood_pressure = st.number_input(
            'Blood Pressure', min_value=0, max_value=140, value=0)
        skin_thickness = st.number_input(
            'Skin Thickness', min_value=0, max_value=100, value=0)
        insulin = st.number_input('Insulin', min_value=0, max_value=900, value=0)
        bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=0.0)
        dpf = st.number_input('Diabetes Pedigree Function',
                              min_value=0.0, max_value=2.5, value=0.0)
        age = st.number_input('Age', min_value=0, max_value=120, value=0)

        # Prediction button
        if st.button('Predict'):
            # Create a DataFrame for input values
            input_data = pd.DataFrame({
                'Pregnancies': [pregnancies],
                'Glucose': [glucose],
                'BloodPressure': [blood_pressure],
                'SkinThickness': [skin_thickness],
                'Insulin': [insulin],
                'BMI': [bmi],
                'DiabetesPedigreeFunction': [dpf],
                'Age': [age]
            })

            # Scale the input data
            input_data_scaled = diabetes_model_scaler.transform(input_data)

            # Make prediction
            prediction_prob = diabetes_model.predict_proba(input_data_scaled)[
                :, 1][0]
            prediction = diabetes_model.predict(input_data_scaled)[0]

            # Display the result
            st.subheader('Prediction')
            st.write(
                f'The probability of you having diabetes is {prediction_prob:.2f}')
            
            


    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':

        # Apply custom CSS for background image
        page_bg_img = '''
        <style>
        body {
            background-image: url("https://www.cnet.com/a/img/resize/5dc30cf96f2260d29b5fb003c767a0cc9089c16d/hub/2024/01/31/8aa3dae2-069b-47cb-9e01-1dc95ca4359c/gettyimages-1401415353.jpg?auto=webp&fit=crop&height=675&width=1200");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background: rgba(255, 255, 255, 0);
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        '''

        st.markdown(page_bg_img, unsafe_allow_html=True)

        st.title('Heart Disease Prediction using ML')

        # Input fields for user data
        age = st.number_input('Age', min_value=0, max_value=120, step=1)
        sex = st.selectbox('Sex ''''[0: Female, 1: Male]''', options=[0, 1])  # 0: Female, 1: Male
        cp = st.selectbox('Describe your chest pain'
                          '''[0: Typical angina
                          1: Atypical angina
                          2: Non-anginal pain
                          3: Asymptomatic]''', options=[0, 1, 2, 3])
        trestbps = st.number_input(
            'Resting Blood Pressure', min_value=0, max_value=200)
        chol = st.number_input('Serum Cholestoral in mg/dl',
                               min_value=0, max_value=600)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl [0: False, 1: True]',
                           options=[0, 1])  # 0: False, 1: True
        restecg = st.selectbox(
            'Resting Electrocardiographic results''''
            [0: Normal
            1: Having ST-T wave abnormality
            2: Showing probable or definite left ventricular hypertrophy]''', options=[0, 1, 2])
        thalach = st.number_input(
            'Maximum Heart Rate achieved', min_value=0, max_value=220)
        exang = st.selectbox('Exercise Induced Angina [1 = yes, 0 = no]', options=[0, 1])
        oldpeak = st.number_input(
            'ST depression induced by exercise', min_value=0.0, max_value=10.0)
        slope = st.selectbox(
            'Slope of the peak exercise ST segment ''''[0: Upsloping
            1: Flat
            2: Downsloping]''', options=[0, 1, 2])
        ca = st.selectbox('Major vessels colored by flourosopy',
                          options=[0, 1, 2, 3, 4])
        thal = st.selectbox('Thalassemia [ 0 = normal; 1 = fixed defect; 2 = reversable defect]', options=[0, 1, 2, 3])

        if st.button('Predict Heart Disease'):
            # Prepare the input data
            input_data = np.array(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            # Make prediction
            prediction = heart_disease_model.predict(input_data)
            probability = heart_disease_model.predict_proba(input_data)[0][1]
            # Display the result
            st.subheader('Prediction')
            st.write(
                f'The probability of you having heart disease is {probability:.2f}')
            





    if selected == 'Lung Cancer Prediction':
        # Apply custom CSS for background image
        page_bg_img = '''
        <style>
        body {
            background-image: url("https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_756141_16919757324217839.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background: rgba(255, 255, 255, 0);
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        '''

        st.markdown(page_bg_img, unsafe_allow_html=True)

        import streamlit as st
        import pandas as pd

        # Title of the web app
        st.title("Lung Cancer Prediction")

        # Collect user input features
        def user_input_features():
            Age = st.number_input('Age', min_value=1, max_value=120, value=30)
            Gender = st.selectbox('Gender', [0, 1])
            Air_Pollution = st.number_input(
                'Air Pollution', min_value=1, max_value=10, value=5)
            Alcohol_use = st.number_input(
                'Alcohol use', min_value=1, max_value=10, value=5)
            Dust_Allergy = st.number_input(
                'Dust Allergy', min_value=1, max_value=10, value=5)
            OccuPational_Hazards = st.number_input(
                'OccuPational Hazards', min_value=1, max_value=10, value=5)
            Genetic_Risk = st.number_input(
                'Genetic Risk', min_value=1, max_value=10, value=5)
            chronic_Lung_Disease = st.number_input(
                'chronic Lung Disease', min_value=1, max_value=10, value=5)
            Balanced_Diet = st.number_input(
                'Balanced Diet', min_value=1, max_value=10, value=5)
            Obesity = st.number_input(
                'Obesity', min_value=1, max_value=10, value=5)
            Smoking = st.number_input(
                'Smoking', min_value=1, max_value=10, value=5)
            Passive_Smoker = st.number_input(
                'Passive Smoker', min_value=1, max_value=10, value=5)
            Chest_Pain = st.number_input(
                'Chest Pain', min_value=1, max_value=10, value=5)
            Coughing_of_Blood = st.number_input(
                'Coughing of Blood', min_value=1, max_value=10, value=5)
            Fatigue = st.number_input(
                'Fatigue', min_value=1, max_value=10, value=5)
            Weight_Loss = st.number_input(
                'Weight Loss', min_value=1, max_value=10, value=5)
            Shortness_of_Breath = st.number_input(
                'Shortness of Breath', min_value=1, max_value=10, value=5)
            Wheezing = st.number_input(
                'Wheezing', min_value=1, max_value=10, value=5)
            Swallowing_Difficulty = st.number_input(
                'Swallowing Difficulty', min_value=1, max_value=10, value=5)
            Clubbing_of_Finger_Nails = st.number_input(
                'Clubbing of Finger Nails', min_value=1, max_value=10, value=5)
            Frequent_Cold = st.number_input(
                'Frequent Cold', min_value=1, max_value=10, value=5)
            Dry_Cough = st.number_input(
                'Dry Cough', min_value=1, max_value=10, value=5)
            Snoring = st.number_input(
                'Snoring', min_value=1, max_value=10, value=5)

            data = {
                'Age': Age,
                'Gender': Gender,
                'Air Pollution': Air_Pollution,
                'Alcohol use': Alcohol_use,
                'Dust Allergy': Dust_Allergy,
                'OccuPational Hazards': OccuPational_Hazards,
                'Genetic Risk': Genetic_Risk,
                'chronic Lung Disease': chronic_Lung_Disease,
                'Balanced Diet': Balanced_Diet,
                'Obesity': Obesity,
                'Smoking': Smoking,
                'Passive Smoker': Passive_Smoker,
                'Chest Pain': Chest_Pain,
                'Coughing of Blood': Coughing_of_Blood,
                'Fatigue': Fatigue,
                'Weight Loss': Weight_Loss,
                'Shortness of Breath': Shortness_of_Breath,
                'Wheezing': Wheezing,
                'Swallowing Difficulty': Swallowing_Difficulty,
                'Clubbing of Finger Nails': Clubbing_of_Finger_Nails,
                'Frequent Cold': Frequent_Cold,
                'Dry Cough': Dry_Cough,
                'Snoring': Snoring
            }

            features = pd.DataFrame(data, index=[0])
            return features

        input_df = user_input_features()

        # Apply scaling
        scaled_input = lung_cancer_model_scaler.transform(input_df)

        # Make predictions
        prediction = lung_cancer_model.predict(scaled_input)
       

        
        if st.button('Predict Lung Cancer'):
            st.subheader('Prediction')
            lung_cancer_label = ['Low', 'Medium', 'High']
            st.write(lung_cancer_label[prediction[0]])
            
            
    
            
                        
    # Option menu in the sidebar
    with st.sidebar:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()  # Rerun the app to reflect the new state

         

# Main function to control the flow
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'show_register' not in st.session_state:
        st.session_state['show_register'] = False

    if st.session_state['logged_in']:
        new_page()
    elif st.session_state['show_register']:
        register_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
