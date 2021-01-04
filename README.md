# covid-tier-api
A very basic API, that isn't really an API, written in Python to return which tier is in which postcode. It currently returns the HTML from the [link (example)](https://www.gov.uk/find-coronavirus-local-restrictions?postcode=SW1A+1AA) here, and searches through the returned HTML to determine which Tier a postcode is in. If there is an error, for example the postcode is invalid, the function will return -1 as the tier.

Obviously, this application is dependent on the gov.uk website link being active, and will presumably not work after the UK Government's tier system has ended. This will only work for postcodes in England, other countries in the UK have seperate systems for handling the Coronavirus outbreak.

The application itself is licensed under the Unlicense, dedicating it to the public domain. Government information is licensed under the [Open Government License v3.0 (OGLv3.0)](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/].
