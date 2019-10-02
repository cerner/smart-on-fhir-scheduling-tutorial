$('#slot-search-form').on('submit', function(e) {
  e.preventDefault();
  slotSearch();
});

$('#clear-slots').on('click', function(e) {
  $('#slots').html('');
  $('#slots-holder-row').hide();
});

function slotSearch() {
  clearUI();
  $('#loading-row').show();

  // Grab Slot query parameters from the slot-search-form
  var form = document.getElementById('slot-search-form');
  var slotParams = {};
  for(var i = 0; i < form.length; i++) {
    // Handle date params later
    if (form.elements[i].name.startsWith('date-')) { continue; }
    slotParams[form.elements[i].name] = form.elements[i].value;
  }
  // Appointment start date and appointment end date need to both be set in query parameter 'start'
  slotParams['start'] = {$ge: form.elements['date-start'].value, $lt: form.elements['date-end'].value};

  FHIR.oauth2.ready(function(smart) {
    // Query the FHIR server for Slots
    smart.api.fetchAll({type: 'Slot', query: slotParams}).then(

      // Display Appointment information if the call succeeded
      function(slots) {
        // If any Slots matched the criteria, display them
        if (slots.length) {
          var slotsHTML = '';

          slots.forEach(function(slot) {
            slotsHTML = slotsHTML + slotHTML(slot.id, slot.type.text, slot.start, slot.end);
          });

          renderSlots(slotsHTML);
        }
        // If no Slots matched the criteria, inform the user
        else {
          renderSlots('<p>No Slots found for the selected query parameters.</p>');
        }
      },

      // Display 'Failed to read Slots from FHIR server' if the call failed
      function() {
        clearUI();
        $('#errors').html('<p>Failed to read Slots from FHIR server</p>');
        $('#errors-row').show();
      }
    );
  });
}

function slotHTML(id, type, start, end) {
  console.log('Slot: id:[' + id + '] type:[' + type + '] start:[' + start + '] end:[' + end + ']');

  var slotReference = 'Slot/' + id,
      prettyStart = new Date(start),
      prettyEnd = new Date(end);

  return "<div class='card'>" +
           "<div class='card-body'>" +
             "<h5 class='card-title'>" + type + '</h5>' +
             "<p class='card-text'>Start: " + prettyStart + '</p>' +
             "<p class='card-text'>End: " + prettyEnd + '</p>' +
           '</div>' +
         '</div>';
}

function renderSlots(slotsHTML) {
  clearUI();
  $('#slots').html(slotsHTML);
  $('#slots-holder-row').show();
}

function clearUI() {
  $('#errors').html('');
  $('#errors-row').hide();
  $('#loading-row').hide();
  $('#slots').html('');
  $('#slots-holder-row').hide();
  $('#appointment').html('');
  $('#appointment-holder-row').hide();
  $('#patient-search-create-row').hide();
}
;
