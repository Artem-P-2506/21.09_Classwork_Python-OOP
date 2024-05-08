import json
from datetime import datetime

class dataWrapper():
    @classmethod
    def serializationData(cls, text):
        message = {
            "Date": str(datetime.now()),
            "message": text,
        }
        return json.dumps(message)

    @classmethod
    def deserializationFullData(cls, message):
        data = json.loads(message)
        return data