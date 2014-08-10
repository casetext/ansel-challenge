# coding=utf8
"""
Try the challenge in Python first before figuring out how to do it in Node.
Smells a little hacky because it is.
"""

import os
import re
import requests
import json

# Load CourtListener credentials from file cl_creds
CL_USER, CL_PASS = map(lambda s: s.strip(), open("cl_creds").readlines())

# URL for querying CourtListener API with a citation, asking for JSON
CITATION_QUERY_URL = "https://www.courtlistener.com/api/rest/v1/search/?citation=%s&format=json"

DATA_DIR = 'test/data'
RESULTS_DIR = 'test/results'

# Magical regex after some trial & error
# re_case = re.compile("""(\d+\s+[\w\d\.]+\s+\d+)(?:,.+?)*?\s*\(.*?\d{4}\)""")
re_both = re.compile("""(?:(\d+\s+[\w\d\.]+\s+\d+)(?:,.+?)*?\s*\(.*?\d{4}\))|(\d+\s+[\w\d\.]+\s+§\s?\d+\w?(?:\.\d\w?)?)""")

def query_courtlistener(citation):
    """
    Query the CourtListener API with a citation
    """
    # Prepare API call URL and submit request
    url = CITATION_QUERY_URL % ("\"" + citation + "\"")
    response = requests.get(url, auth=(CL_USER, CL_PASS))

    # Convert response from JSON -> dict
    j = json.loads(response.content)

    # Make sure we only get one hit.
    if len(j.get('objects')) == 1:
        # Return the meat of the CourtListener response
        return j.get('objects')[0]
    else:
        # Freak out if we got more than one hit for a citation query.
        # (Added quotation marks around citation to avoid problems.)
        raise Exception("Whoops, got %d objects!" % len(j.get('objects')))

def make_clean_citation(citation):
    """
    Reconstruct a clean citation for a case
    """
    j = query_courtlistener(citation)
    return "%s, %s (%s)" % (j.get('case_name'), j.get('citation'), j.get('date_filed')[:4])

def main():
    for fname in os.listdir(DATA_DIR):
        print("File: %s" % fname)

        # Accumulate found citations here so we can skip repeats
        found = []

        for line in open(DATA_DIR + os.sep + fname).readlines():

            for match in re_both.finditer(line):

                # First try the half of the regex for cases
                if match.group(1) is not None:
                    hit = match.group(1)

                # If not, try the second half for statutes/regulations
                elif match.group(2) is not None:
                    hit = match.group(2)

                # Add it to our list of matches if it's not already there.
                if hit not in found:
                    found.append(hit)

        for citation in found:

            # Get a clean citation for cases
            try:
                print(make_clean_citation(citation))

            # Print as-is for everything else
            except:
                print(citation)

        print("")

if __name__ == "__main__":
    main()
