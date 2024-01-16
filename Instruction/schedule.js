//schedule a new visit

import FHIR from 'fhirclient';

// Assume we have a patientId, practitionerId, and slotId
let patientId = 'example-patient-id';
let practitionerId = 'example-practitioner-id';
let slotId = 'example-slot-id';

// Create a new Appointment resource
let newAppointment = {
    resourceType: 'Appointment',
    status: 'booked',
    slot: [
        {
            reference: `Slot/${slotId}`
        }
    ],
    participant: [
        {
            actor: {
                reference: `Patient/${patientId}`
            },
            status: 'accepted'
        },
        {
            actor: {
                reference: `Practitioner/${practitionerId}`
            },
            status: 'accepted'
        }
    ]
};

FHIR.oauth2.ready(function(smart) {
    // Send the new Appointment to the FHIR server
    smart.api.create({
        type: 'Appointment',
        resource: newAppointment
    }).then(
        function(appointment) {
            console.log('Appointment created:', appointment);
        },
        function(error) {
            console.error('Failed to create Appointment:', error);
        }
    );
});