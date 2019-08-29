###############################################################################
# Sample to transforming a flowfile with json format
# modified from "https://github.com/BatchIQ/nifi-scripting-samples"
#
# Assumed input json format: 
# {
#   "timestamp": 1514541007050,
#   "values":[ 
#       {
#           "name": "first",
#           "value": 12345,
#           "message": "Foo"
#           "timesatmp": 1514541007050
#        },
#        {
#           "name": "second",
#           "value": 12345,
#           "message": "qoo"
#            "timestamp": 1514541004656
#        },
#   ]
# }
# 
# output
# {
#   "tagname": "first",
#   "value": 152399025,
#   "message": "Hello World"
#   "timestamp": 1514541007050
#               }
# }
###############################################################################

import json
import sys
import traceback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil


class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_obj = json.loads(input_text)
            output_text = input_obj['name']

            outputStream.write(bytearray(output_text.encode('utf-8')))
        except:
            traceback.print_exc(file=sys.stdout)
            raise


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

    # Finish by transferring the FlowFile to an output relationship
session.transfer(flowFile, REL_SUCCESS)