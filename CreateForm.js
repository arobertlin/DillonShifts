// this is a google app script, should be run at scripts.google.com

function createForm(shift) {
   // create & name Form
   //var curDate = Utilities.formatDate(new Date(), "GMT+1", "MM/dd/yyyy")
   var item = "Shift Coverage Form " + shift;
   var form = FormApp.create(item)
       .setTitle(item);

   // single line text field
   item = "Net ID";
   form.addTextItem()
       .setTitle(item)
       .setRequired(true);

   // radiobuttons
   item = "Do you want to enter in a lottery for this shift?";
   var choices = ["Yes", "No"];
   form.addMultipleChoiceItem()
       .setTitle(item)
       .setChoiceValues(choices)
       .setRequired(true)

  // responses = form.getResponses()
  // Logger.log(responses)

  return {'url':form.getPublishedUrl(), 'id':form.getId()}
 }