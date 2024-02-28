import json
import uuid
from datetime import datetime

class dataWrapper():
    @classmethod
    def serializationData(cls, text, UUID=None, time=None):
        if UUID is None:
            UUID = str(uuid.uuid4())
        if time is None:
            time = str(datetime.now())
        message = {
            "UUID": UUID,
            "Date": time,
            "msq": text
        }
        return json.dumps(message)

    @classmethod
    def deserializationFullData(cls, message):
        data = json.loads(message)
        return data