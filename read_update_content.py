###############################################################################
# Write content to an outgoing flow file using a callback
# modified from "https://community.hortonworks.com/articles/75545/executescript-cookbook-part-2.html"
# 
# This script will read and overwirte content. In this example,
# the input content will not be used for output.
# 
# output:
# !dlroW olleH
###############################################################################



from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
    
# Define a subclass of StreamCallback for use in session.write()
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        outputStream.write(bytearray('Hello World!'[::-1].encode('utf-8')))
# end class
flowFile = session.get()
if(flowFile != None):
    flowFile = session.write(flowFile, PyStreamCallback())
    
session.transfer(flowFile, REL_SUCCESS)