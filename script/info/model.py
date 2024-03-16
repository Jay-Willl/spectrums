import json

class Movie:
    def __init__(self, metadata, credits, segments):
        self.metadata = metadata
        self.segments = segments
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
        self.size = None
        self.elapse = None
        self.eigenvalue = None
    
    def to_json(self):
        return {
            "id": self.id,
            "start": self.start,
            "end": self.end,
            "size": self.size,
            "elapse": self.elapse,
            "eigenvalue": self.eigenvalue
        }
