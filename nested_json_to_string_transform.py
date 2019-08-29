###############################################################################
# Sample to transform a flowfile with nested json format to string format
# modified from "https://github.com/BatchIQ/nifi-scripting-samples"
#
# Assumed nested input json format: 
# 
# {
#   "timestamp": 1514541007050,
#   "values":[
#       {
#           "name": "first",
#           "value": 12345,
#           "message": "Foo",
#           "timestamp": 151454100705
#       },
#       {   "name": "second",
#           "value": 54321,
#           "message": "Qoo",
#           "timestamp": 151454188888
#   }]
# }
# output:
#  first,12345,Foo,1514541007050
#  second,54321,Qoo,151454188888
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
            for value in input_obj['values']:
                output_text = "{},{},{},{}".format(value['name'],value['value'],value['message'],value['timestamp'])

                outputStream.write(bytearray(output_text.encode('utf-8')))
                outputStream.write(bytearray('\n'.encode('utf-8')))

        except:
            traceback.print_exc(file=sys.stdout)
            raise


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

    # Finish by transferring the FlowFile to an output relationship
session.transfer(flowFile, REL_SUCCESS)