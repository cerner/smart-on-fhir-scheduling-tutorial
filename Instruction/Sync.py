Sync

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime

class CalendarSync:
    def __init__(self, credentials_file):
        # Load credentials from the 'credentials.json' file
        flow = InstalledAppFlow.from_client_secrets_file(credentials_file, ['https://www.googleapis.com/auth/calendar'])
        creds = flow.run_local_server(port=0)

        # Build the service
        self.service = build('calendar', 'v3', credentials=creds)

    def add_appointment(self, appointment):
        # Convert the FHIR appointment to a Google Calendar event
        event = {
            'summary': 'Appointment',
            'start': {
                'dateTime': appointment['start'],
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': appointment['end'],
                'timeZone': 'America/Los_Angeles',
            },
        }

        # Add the event to the primary calendar
        event = self.service.events().insert(calendarId='primary', body=event).execute()

        print('Event created:', event['htmlLink'])

# Usage
calendar_sync = CalendarSync('credentials.json')
appointment = {
    'start': datetime.datetime.now().isoformat(),
    'end': (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(),
}
calendar_sync.add_appointment(appointment)

