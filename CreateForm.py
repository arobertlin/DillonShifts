from __future__ import print_function
from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

def main():
    """Runs the sample.
    """
    SCRIPT_ID = 'yourscriptid'

    # Setup the Apps Script API
    SCOPES = 'https://www.googleapis.com/auth/forms'
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('script', 'v1', credentials=creds)

    # Create an execution request object.
    request = {"function": "createForm", "parameters": ["Sunday 2-6"], "devMode": True}

    try:
        # Make the API request.
        response = service.scripts().run(body=request,
                scriptId=SCRIPT_ID).execute()

        if 'error' in response:
            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                        trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns. Here, the function returns an Apps Script Object
            # with String keys and values, and so the result is treated as a
            # Python dictionary (folderSet).
            returnvalues = response['response'].get('result', {})
            if not returnvalues:
                print('No data returned!')
            else:
                print('Got a Response!')
                print('ID: ' + returnvalues['id'])
                print('url: ' + returnvalues['url'])

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print(e.content)


if __name__ == '__main__':
    main()
