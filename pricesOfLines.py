import urllib.request, json

try:
    url = "https://gateway.apiportal.ns.nl/public-prijsinformatie/prices"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': 'cd6eb5864b0441d9b633b2e3fccce635',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except urllib.error.HTTPError as e:
    print(f'HTTP error occurred: {e.code} - {e.reason}')
    print(e.read().decode())  # Toon het volledige antwoord van de server bij een fout
except urllib.error.URLError as e:
    print(f'URL error occurred: {e.reason}')
except Exception as e:
    print(f'General error: {str(e)}')
