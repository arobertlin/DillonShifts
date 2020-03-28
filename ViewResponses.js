// this is a google app script, should be run at scripts.google.com

function viewResponses(formid) {
  var existingForm = FormApp.openById(formid);
  var netids = []
  var formResponses = existingForm.getResponses()
  for (var i = 0; i < formResponses.length; i++) {
  var formResponse = formResponses[i];
        // var email = formResponse.getRespondentEmail();
     // netids.push(email)
  var itemResponses = formResponse.getItemResponses();
    if (itemResponses[1].getResponse() == 'Yes') {
      netids.push(itemResponses[0].getResponse())
    }

    // Logger.log(email);
    // Logger.log('Response #%s to the question "%s" was "%s"',
        //(i + 1).toString(),
  // netids.push(itemResponses[0].getResponse())
        /* itemResponse.getItem().getTitle(),
        itemResponse.getResponse()); */
  }
  return netids
}
