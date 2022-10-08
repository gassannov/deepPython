import json
import re

json_str = '{"word1": "foo bar","word2": "some bar","word3": "some foo","word4": "loren ipsum","word5": "dolor sit",' \
           '"word6": "python code"} '


def callback_func():
    pass


def parse_json(json_str: str, keyword_callback=None, required_fields=None, keywords=None):
    json_doc = {}
    try:
        json_doc = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        print("json.decoder.JSONDecodeError")
        return
    except TypeError:
        print("Put str")
        return

    if required_fields is None or keywords is None:
        return None

    fields = list(set(json_doc.keys()) & set(required_fields))
    for field in fields:
        for keyword in keywords:
            if keyword in json_doc[field]:
                keyword_callback(json_doc[field])


# parse_json(json_str, required_fields=['word1', 'word2'])