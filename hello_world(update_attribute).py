###############################################################################
# Setting flowfile attributes in ExecuteScript
#
# Variables provided in scope by script engine:
#
#    session - ProcessSession
#    REL_SUCCESS - Success Relationship
###############################################################################

flowFile = session.get()
if flowFile != None:
    # Update single attribute, if the attribute doesn't exist, it will be created
    flowFile = session.putAttribute(flowFile, "message", "Hello-World")
session.transfer(flowFile, REL_SUCCESS)