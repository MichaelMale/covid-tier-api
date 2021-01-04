import requests

class CovidTier:
    def __init__(self, postcode, tier=-1):
        '''Constructor for objects of type CovidTier.

        Keyword arguments:
        postcode -- A postcode located in England (default null)
        tier -- The tier that said postcode is in (default -1)
        '''
        self.postcode = postcode
        self.tier = tier
    
    def __str__(self):
        '''Displays postcode and tier info.

        Keyword arguments:
        self -- Object of type CovidTier to be displayed (default null)
        '''
        return 'Postcode: ' + self.postcode + '\nTier: ' + str(self.tier)

def find_tier(postcode):
    '''Find which tier a postcode is in.

    Keyword arguments:
    postcode -- A postcode located in England (default null)
    '''
    res = CovidTier(postcode)
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

print('COVID-19 Tier Finder for postcodes in England')
print('\nMichael Male - michaelmale31@gmail.com')
postcode = input('Please enter a postcode:\n')

tier = find_tier(postcode)

print(tier)