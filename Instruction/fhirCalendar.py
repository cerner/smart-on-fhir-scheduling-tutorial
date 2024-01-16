class FhirCalendar:
    def __init__(self, fhir_api):
        self.fhir_api = fhir_api

    def check_availability(self, start_time, end_time):
        # Check availability using the FHIR API
        pass

    def new_appointment(self, patient_id, practitioner_id, start_time, end_time):
        # Schedule new appointment using the FHIR API
        pass

    def reschedule_appointment(self, appointment_id, new_start_time, new_end_time):
        # Reschedule appointment using the FHIR API
        pass

    def cancel_appointment(self, appointment_id):
        # Cancel appointment using the FHIR API
        pass

    def send_reminder(self, appointment_id):
        # Send reminder for appointment using the FHIR API
        pass

    def sync(self):
        # Sync with the FHIR API
        pass

    def resolve_conflict(self, appointment_id):
        # Resolve conflict using the FHIR API
        pass

    def fetch_patient_details(self, patient_id):
        # Fetch patient details using the FHIR API
        pass

    def fetch_practitioner_details(self, practitioner_id):
        # Fetch practitioner details using the FHIR API
        pass

    def fetch_appointment_history(self, patient_id):
        # Fetch appointment history using the FHIR API
        pass