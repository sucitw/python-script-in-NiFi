import sys
import traceback
from org.apache.nifi.processor import Processor
from org.apache.nifi.processor import Relationship
from org.apache.nifi.components import PropertyDescriptor
from org.apache.nifi.processor.util import StandardValidators

class UpdateAttributes(Processor) :
    __rel_success = Relationship.Builder().description("Success").name("success").build()

    def __init__(self) :
        pass

    def initialize(self, context) :
        pass

    def getRelationships(self) :
        return set([self.__rel_success])

    def validate(self, context) :
        pass

    def getPropertyDescriptors(self) :
        descriptor = PropertyDescriptor.Builder().name("for-attributes").addValidator(StandardValidators.NON_EMPTY_VALIDATOR).build()
        return [descriptor]

    def onPropertyModified(self, descriptor, newValue, oldValue) :
        pass

    def onTrigger(self, context, sessionFactory) :
        session = sessionFactory.createSession()
        try :
            # ensure there is work to do
            flowfile = session.get()
            if flowfile is None :
                return

            # extract some attribute values
            fromPropertyValue = context.getProperty("for-attributes").getValue()
            fromAttributeValue = flowfile.getAttribute("for-attributes")

            # set an attribute
            flowfile = session.putAttribute(flowfile, "from-property", fromPropertyValue)
            flowfile = session.putAttribute(flowfile, "from-attribute", fromAttributeValue)
            flowfile = session.putAttribute(flowfile, "message", 'Hello-World')


            # transfer
            session.transfer(flowfile, self.__rel_success)
            session.commit()
        except :
            print sys.exc_info()[0]
            print "Exception in TestReader:"
            print '-' * 60
            traceback.print_exc(file=sys.stdout)
            print '-' * 60

            session.rollback(true)
            raise

processor = UpdateAttributes()
