from slot_values import Property, Subject


class FranklinQuestion:
    def __init__(self, template, facts, operations):
        self.template = template
        self.facts = facts
        self.operations = operations


class FuturePrediction(FranklinQuestion):
    def __init__(self):
        template = 'What will be the {property} of {subject} in {time}?'

        allowed_values = {
            'property': Property.values,
            'subject': Subject.Country.values,
            'time': Time.Future.values,
        }
