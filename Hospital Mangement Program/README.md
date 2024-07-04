# HospitalManagement Class

The `HospitalManagement` class manages information about doctors, patient details, appointments, fees calculation, and medicine prescription.

## Attributes

- `_doctors`: List of available doctors in the hospital.
- `_patient_age`: Age of the patient.
- `_blood_group`: Blood group of the patient.
- `_doc_dept`: Department of the doctor currently set.

## Methods

### Initialization

```python
def __init__(self) -> None:
    """Initialize with default attributes."""
    self._doctors = ["Cardiologist", "Dermatologist", "Gynaecologist", "Hematologist", 
                     "Gastroenterologist", "Neurologist", "Pulmonologist"]
    self._patient_age = 0
    self._blood_group = None
    self._doc_dept = None

def _set_doc_dept(self, doc_dept):
    """Set the department of the doctor (private method)."""
    if doc_dept in self._doctors:
        self._doc_dept = doc_dept
        print(f"Doctor department set to {doc_dept}.")
    else:
        print(f"{doc_dept} is not available in our hospital.")

def get_doc_dept(self):
    """Get the current department of the doctor."""
    return self._doc_dept

def chk_avial(self, doc_dept):
    """Check if a doctor is available in the hospital."""
    if doc_dept in self._doctors:
        print(f"{doc_dept} is available in our hospital.")
    else:
        print(f"{doc_dept} is not available in our hospital.")

def appt_doc(self, doc_dept, day):
    """Check and book appointments for a doctor on a specific day."""
    if doc_dept in self._doctors:
        print(f"Checking availability of {doc_dept} on {day}.")
        # Implement logic for appointment scheduling by day
    else:
        return f"{doc_dept} is not available in our hospital."

def set_patient_info(self, age, blood_group):
    """Set patient information."""
    self._patient_age = age
    self._blood_group = blood_group
    print(f"Patient information set: Age - {age}, Blood Group - {blood_group}")

def get_patient_info(self):
    """Get patient information."""
    return f"Patient Age: {self._patient_age}, Blood Group: {self._blood_group}"

@staticmethod
def calculate_fees(doc_dept, consultation_time):
    """Calculate consultation fees based on doctor's department and consultation time."""
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
    """Prescribe medicine based on diagnosis."""
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

# Example Usage
hospital = HospitalManagement()

# Check doctor availability and set doctor department
hospital.chk_avial("Cardiologist")
hospital._set_doc_dept("Dermatologist")

# Get current doctor department
print(hospital.get_doc_dept())

# Check and book appointments
print(hospital.appt_doc("Cardiologist", "Monday"))
print(hospital.appt_doc("Dermatologist", "Thursday"))
print(hospital.appt_doc("Dentist", "Monday"))

# Set and get patient information
hospital.set_patient_info(25, "O+")
print(hospital.get_patient_info())

# Calculate fees
fees = HospitalManagement.calculate_fees("Cardiologist", 30)  # 30 minutes consultation
print(f"The fees for the Cardiologist is: ${fees}")

# Prescribe medicine
medicine = HospitalManagement.prescribe_medicine("Hypertension")
print(f"The prescribed medicine for Hypertension is: {medicine}")
