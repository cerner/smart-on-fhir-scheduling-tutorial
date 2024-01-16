centralCalendar.py
# 
# class CentralCalendar:
    def __init__(self, fhir_calendars, variable_calendars):
        self.fhir_calendars = fhir_calendars
        self.variable_calendars = variable_calendars

    def check_availability(self, start_time, end_time):
        # Check availability in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            if not calendar.check_availability(start_time, end_time):
                return False
        return True

    def new_appointment(self, patient_id, practitioner_id, start_time, end_time):
        # Schedule new appointment in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.new_appointment(patient_id, practitioner_id, start_time, end_time)

    def reschedule_appointment(self, appointment_id, new_start_time, new_end_time):
        # Reschedule appointment in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.reschedule_appointment(appointment_id, new_start_time, new_end_time)

    def cancel_appointment(self, appointment_id):
        # Cancel appointment in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.cancel_appointment(appointment_id)

    def send_reminder(self, appointment_id):
        # Send reminder for appointment in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.send_reminder(appointment_id)

    def sync(self):
        # Sync all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.sync()

    def resolve_conflict(self, appointment_id):
        # Resolve conflict for appointment in all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.resolve_conflict(appointment_id)

    def fetch_patient_details(self, patient_id):
        # Fetch patient details from all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.fetch_patient_details(patient_id)

    def fetch_practitioner_details(self, practitioner_id):
        # Fetch practitioner details from all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.fetch_practitioner_details(practitioner_id)

    def fetch_appointment_history(self, patient_id):
        # Fetch appointment history from all calendars
        for calendar in self.fhir_calendars + self.variable_calendars:
            calendar.fetch_appointment_history(patient_id)