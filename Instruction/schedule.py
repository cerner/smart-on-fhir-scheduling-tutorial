#schedule appointment python

"""

""" 
# 
# import requests
import json

class Scheduler:
    def __init__(self, server_url):
        self.server_url = server_url

    def schedule_visit(self, patient_id, practitioner_id, slot_id):
        # Create a new Appointment resource
        new_appointment = {
            'resourceType': 'Appointment',
            'status': 'booked',
            'slot': [
                {
                    'reference': f'Slot/{slot_id}'
                }
            ],
            'participant': [
                {
                    'actor': {
                        'reference': f'Patient/{patient_id}'
                    },
                    'status': 'accepted'
                },
                {
                    'actor': {
                        'reference': f'Practitioner/{practitioner_id}'
                    },
                    'status': 'accepted'
                }
            ]
        }

        # Send the new Appointment to the FHIR server
        response = requests.post(f'{self.server_url}/Appointment', json=new_appointment)

        if response.status_code == 201:
            print('Appointment created:', response.json())
        else:
            print('Failed to create Appointment:', response.status_code, response.text)

# Usage
scheduler = Scheduler('https://example.com/fhir')
scheduler.schedule_visit('example-patient-id', 'example-practitioner-id', 'example-slot-id')