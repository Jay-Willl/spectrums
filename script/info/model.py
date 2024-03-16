import json

class Movie:
    def __init__(self, metadata, credits):
        self.metadata = metadata
        self.segments = list()
        self.credits = credits

    def to_json(self):
        return json.dumps({
            "movie": {
                "metadata": self.metadata,
                "credits": self.credits,
                "segments": self.segments
            }
        })


class Seg:
    def __init__(self):
        self.id = None
        self.start = None
        self.end = None
        self.size = tuple()
        self.elapse = None
    
