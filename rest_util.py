import unirest

POST = "POST"
GET = "GET"

DEAFAULT_HEADERS = {"Accept": "application/json"}

SAMPLE_URL = "https://raw.githubusercontent.com/cshoemaker23/DronisosAnalytics/master/README.md"
# This is a dictionary, its just a bunch of key - value pairs
SAMPLE_REQUEST = {
    "url": SAMPLE_URL
}


def post(request):
    return __rest_call(POST, request)


def get(request):
    return __rest_call(GET, request)


'''
The "__" before the method makes it private. This means that it cannot be called 
outside of this file. It makes for cleaner code 
http://www.diveintopython.net/object_oriented_framework/private_functions.html
'''


def __rest_call(method, request):
    response = ""

    request_url = request.get("url")
    # The second parameter in the get means that if "headers" is not in the dictionary,
    # set the variable to DEFAULT_HEADERS.
    request_headers = request.get("headers", DEAFAULT_HEADERS)

    if(method == POST):
        response = unirest.post(request_url,
                                headers=request_headers,
                                params=request.get("params"))
    elif(method == GET):
        response = unirest.get(request_url)

    # We want to make sure we get some sort of 200 back (200 is a success for
    # an http request)
    print "-----------------------------------------------------------------------"
    if(response.code / 2 != 100):
        print "ERROR: Recieved %s for a %s request to %s" % (str(response.code), method, request.get("url"))
    else:
        print "SUCCESS: Recieved %s for a %s request to %s" % (str(response.code), method, request.get("url"))

    print "Response body: " + str(response.body)
    print "-----------------------------------------------------------------------"


# To import this file you would do `import rest_util` then
# If this was imported then you could say `rest_util.get(request)`
# but since this is in the same file, we can just call it, since its
# declared above
get(SAMPLE_REQUEST)
