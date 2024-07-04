class HospitalManagement:
    def __init__(self) -> None:
        self._doctors = ["Cardiologist", "Dermatologist", "Gynaecologist", "Hematologist", "Gastroenterologist", "Neurologist", "Pulmonologist"]
        self._patient_age = 0
        self._blood_group = None
        self._doc_dept = None

    def _set_doc_dept(self, doc_dept):  # setter is made private
        if doc_dept in self._doctors:
            self._doc_dept = doc_dept
            print(f"Doctor department set to {doc_dept}.")
        else:
            print(f"{doc_dept} is not available in our hospital.")

    def get_doc_dept(self):  # getter method
        return self._doc_dept

    def chk_avial(self, doc_dept):
        if doc_dept in self._doctors:
            print(f"{doc_dept} is available in our hospital.")
        else:
            print(f"{doc_dept} is not available in our hospital.")

    def appt_doc(self, doc_dept, day):
        if doc_dept in self._doctors:
            print(f"Checking availability of {doc_dept} on {day}.")
            match day:
                case "Monday":
                    if doc_dept == "Cardiologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Monday"
                case "Tuesday":
                    if doc_dept == "Dermatologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Tuesday"
                case "Wednesday":
                    if doc_dept == "Gynaecologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Wednesday"
                case "Thursday":
                    if doc_dept == "Hematologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Thursday"
                case "Friday":
                    if doc_dept == "Gastroenterologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Friday"
                case "Saturday":
                    if doc_dept == "Neurologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Saturday"
                case "Sunday":
                    if doc_dept == "Pulmonologist":
                        return "Yes"
                    else:
                        return f"{doc_dept} is not available on Sunday"
                case _:
                    return "No appointments available on this day."
        else:
            return f"{doc_dept} is not available in our hospital."

    def set_patient_info(self, age, blood_group):  # setter for patient information
        self._patient_age = age
        self._blood_group = blood_group
        print(f"Patient information set: Age - {age}, Blood Group - {blood_group}")

    def get_patient_info(self):  # getter for patient information
        return f"Patient Age: {self._patient_age}, Blood Group: {self._blood_group}"

    @staticmethod
    def calculate_fees(doc_dept, consultation_time):
        base_fee = 100
        specialist_fees = {
            "Cardiologist": 200,
            "Dermatologist": 150,
            "Gynaecologist": 180,
            "Hematologist": 170,
            "Gastroenterologist": 190,
            "Neurologist": 210,
            "Pulmonologist": 160
        }
        specialist_fee = specialist_fees.get(doc_dept, 0)
        total_fee = base_fee + specialist_fee + (consultation_time * 10)
        return total_fee

    @classmethod
    def prescribe_medicine(cls, diagnosis):
        medication_dict = {
            "Hypertension": "Amlodipine",
            "Diabetes": "Metformin",
            "Asthma": "Albuterol",
            "Dermatitis": "Hydrocortisone",
            "Anemia": "Ferrous Sulfate",
            "Gastritis": "Omeprazole",
            "Migraine": "Sumatriptan"
        }
        medication = medication_dict.get(diagnosis, "Consult your doctor for appropriate medication.")
        return medication

# Example:
hospital = HospitalManagement()
hospital.chk_avial("Cardiologist")
hospital._set_doc_dept("Dermatologist")  # Using the private setter method
print(hospital.get_doc_dept())  # Using the getter method
print(hospital.appt_doc("Cardiologist", "Monday"))
print(hospital.appt_doc("Dermatologist", "Thursday"))
print(hospital.appt_doc("Dentist", "Monday"))

hospital.set_patient_info(25, "O+")
print(hospital.get_patient_info())

# Calculate fees 
fees = HospitalManagement.calculate_fees("Cardiologist", 30)  
print(f"The fees for the Cardiologist is: ${fees}")

# Prescribe medicine 
medicine = HospitalManagement.prescribe_medicine("Hypertension")
print(f"Your medicnie is: {medicine}")
