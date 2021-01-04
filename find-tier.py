import requests

class CovidTier:
    def __init__(self, postcode, tier):
        self.postcode = postcode
        self.tier = tier
    
    def __str__(self):
        return 'Postcode: ' + self.postcode + '\nTier: ' + str(self.tier)

def find_tier(postcode):
    res = CovidTier(postcode, -1)
    URL = "https://www.gov.uk/find-coronavirus-local-restrictions?postcode=" + postcode

    req = requests.get(URL)

    if (req.text.find('There is a problem') >= 1):
        print('Problem occurred')
        return res
    elif (req.text.find('Tier 1') >= 1):
        res.tier = 1
    elif (req.text.find('Tier 2') >= 1):
        res.tier = 2
    elif (req.text.find('Tier 3') >= 1):
        res.tier = 3
    elif (req.text.find('Tier 4') >= 1):
        res.tier = 4

    return res

tier = find_tier('sy231lu')

print(tier)