###############################################################################
# Setting flowfile attributes in ExecuteScript
#
# Variables provided in scope by script engine:
#
#    session - ProcessSession
#    context - ProcessContext
#    log - ComponentLog
#    REL_SUCCESS - Success Relationship
#    REL_FAILURE - Failure Relationship
###############################################################################

flowFile = session.get()
if flowFile != None:
    # Get attributes
    attribute1 = flowFile.getAttribute("attribute1")
    message = attribute1 + " update!"

    # Set single attribute
    flowFile = session.putAttribute(flowFile, "message", message)

    # Set multiple attributes
    flowFile = session.putAllAttributes(flowFile, {
        "attribute.one": "true",
        "attribute.two": "2"
    })

session.transfer(flowFile, REL_SUCCESS)