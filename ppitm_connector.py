#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------
# Phantom PP ITM python file by Asher Lee
# Initial Dev by Asher Lee (BOQ)
# Supported Dev by John Wang (Splunk)
# Additional Dev by <NAME> (Splunk)
# -----------------------------------------

# Python 3 Compatibility imports
from __future__ import print_function, unicode_literals

# Phantom App imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# Usage of the consts file is recommended
from ppitm_consts import *
import requests
import json
from bs4 import BeautifulSoup


class RetVal(tuple):
    def __new__(cls, val1, val2=None):
        return tuple.__new__(RetVal, (val1, val2))


class PpItmConnector(BaseConnector):
    def __init__(self):
        # Call the BaseConnectors init first
        super(PpItmConnector, self).__init__()
        self._state = None

        # Variable to hold a base_url in case the app makes REST calls
        # Do note that the app json defines the asset config, so please
        # modify this as you deem fit.
        self._base_url = None
        self._client_secret = None
        self._client_id = None
        self._api_version = None
        self._access_token = None
        self._refresh_token = None
        self._token_type = None
        self._status_code = 0
        self._full_token = None
        

    def _process_stream_response(self, response, action_result):
        if response.status_code == 200:
            return RetVal(phantom.APP_SUCCESS, response.text)
        return RetVal(
            action_result.set_status(
                phantom.APP_ERROR, "Empty response and no information in the header"
            ), None
        )

    def _process_empty_response(self, response, action_result):
        if response.status_code == 200:
            return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)
            return RetVal(phantom.APP_SUCCESS, {})
        return RetVal(
            action_result.set_status(
                phantom.APP_ERROR, "Empty response and no information in the header"
            ), None
        )

    def _process_html_response(self, response, action_result):
        # An html response, treat it like an error
        status_code = response.status_code

        # Handle valid responses from ipinfo.io
        if (status_code == 200):
            return RetVal(phantom.APP_SUCCESS, response.text)

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            error_text = soup.text
            split_lines = error_text.split('\n')
            split_lines = [x.strip() for x in split_lines if x.strip()]
            error_text = '\n'.join(split_lines)
        except:
            error_text = "Cannot parse error details"
            message = "Status Code: {0}. Data from server:\n{1}\n".format(status_code,
            error_text)
            message = message.replace('{', '{{').replace('}', '}}')
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_html_response_orig(self, response, action_result):
        # An html response, treat it like an error
        status_code = response.status_code

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            error_text = soup.text
            split_lines = error_text.split('\n')
            split_lines = [x.strip() for x in split_lines if x.strip()]
            error_text = '\n'.join(split_lines)
        except:
            error_text = "Cannot parse error details"
        message = "Status Code: {0}. Data from server:\n{1}\n".format(status_code, error_text)
        message = message.replace(u'{', '{{').replace(u'}', '}}')
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_json_response(self, r, action_result):
        # Try a json parse
        try:
            resp_json = r.json()
        except Exception as e:
            return RetVal(
                action_result.set_status(
                    phantom.APP_ERROR, "Unable to parse JSON response. Error: {0}".format(str(e))
                ), None
            )
        # Please specify the status codes here
        if 200 <= r.status_code < 399:
            return RetVal(phantom.APP_SUCCESS, resp_json)
        # You should process the error returned in the json
        message = "Error from server. Status Code: {0} Data from server: {1}".format(
            r.status_code,
            r.text.replace(u'{', '{{').replace(u'}', '}}')
        )
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)


    def _process_response(self, r, action_result):
        # store the r_text in debug data, it will get dumped in the logs if the action fails
        if hasattr(action_result, 'add_debug_data'):
            action_result.add_debug_data({'r_status_code': r.status_code})
            action_result.add_debug_data({'r_text': r.text})
            action_result.add_debug_data({'r_headers': r.headers})
        # Process each 'Content-Type' of response separately
        # Process a json response
        if 'json' in r.headers.get('Content-Type', ''):
            return self._process_json_response(r, action_result)
        if 'octet-stream' in r.headers.get('Content-Type', ''):
            return self._process_stream_response(r, action_result)

        # Process an HTML response, Do this no matter what the api talks.
        # There is a high chance of a PROXY in between phantom and the rest of
        # world, in case of errors, PROXY's return HTML, this function parses
        # the error and adds it to the action_result.
        if 'html' in r.headers.get('Content-Type', ''):
            return self._process_html_response(r, action_result)
        # it's not content-type that is to be parsed, handle an empty response
        if not r.text:
            return self._process_empty_response(r, action_result)
        # everything else is actually an error at this point
        message = "Can't process response from server. Status Code: {0} Data from server: {1}".format(
            r.status_code,
            r.text.replace('{', '{{').replace('}', '}}')
        )
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _get_token(self, action_result):
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'scope': '*'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json'
        }

        url = self._base_url + "/auth/oauth/token"

        self.save_progress("#GET-TOK:  Connecting to API Endpoint and posting id/secret as headers")

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            self.save_progress("#GET-TOK: POST request sent for AUTH TOKEN ----#")
        except Exception as e:
            self.error_print("#GET-TOK: Error while conecting to server for AUTH TOKEN: ", e)
            return action_result.set_status(phantom.APP_ERROR, "{}: {}".format("#GET-TOK: Error while connecting to server: ", str(e)))
        
        self.save_progress("#---- ---- ** TOKEN RECEIVED ** ---- ----#")

        thaJSON = response.json()
        self._access_token = thaJSON['access_token']
        self._refresh_token = thaJSON['refresh_token']
        self._token_type = thaJSON['token_type']
        self._status_code = response.status_code
        self._full_token = thaJSON
        self.save_progress("#GET-TOK: AUTH TOKEN sub-process completed: {0} #".format(self._status_code))
        self.save_progress("#GET-TOK: token vars set if token type set, TOKEN-TYPE = {0} #".format(self._token_type))

        return phantom.APP_SUCCESS
        
    def _make_rest_call(self, endpoint, action_result, method="get", **kwargs):
        # **kwargs can be any additional parameters that requests.request accepts
        config = self.get_config()
        resp_json = None

        if not self._access_token:
            ret_val_tokenization = self._get_token(action_result)
            if phantom.is_fail(ret_val_tokenization):
                error_message = action_result.get_message()
                return RetVal(action_result.get_status(), TOKENIZATION_ERR_MSG.format(error_message))

        if self._access_token:
            headers = {
                'headers': {
                    "Authorization": BEARER_STRING.format(self._access_token),
                    "Content-Type": "application/json"
                }
            }
            kwargs.update(headers)

        try:
            request_func = getattr(requests, method)
        except AttributeError:
            return RetVal(
                action_result.set_status(phantom.APP_ERROR, "Invalid method: {0}".format(method)),
                resp_json
            )
        # Create a URL to connect to
        url = self._base_url + endpoint
        try:
            r = request_func(
                url,
                # auth=(username, password),  # basic authentication
                verify=config.get('verify_server_cert', False),
                **kwargs
            )
        except Exception as e:
            return RetVal(
                action_result.set_status(
                    phantom.APP_ERROR, "Error Connecting to server. Details: {0}".format(str(e))
                ), resp_json
            )
        return self._process_response(r, action_result)

    def _handle_test_connectivity(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("#####################################")

        ret_val = self._get_token(action_result)

        if phantom.is_fail(ret_val):
            error_message = action_result.get_message()
            self.save_progress("Test Connectivity Failed.")
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, error_message)
        
        self.save_progress("Test Connectivity Passed")
        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)
    
    def _handle_get_email(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))
        self.save_progress("#####################################")

        attachments = param.get('attachments')
        stream = param.get('stream')
        fqid = param['fqid']

        theEndpoint="/activity/events/{fqid}/messages/default/contents/_raw?stream={stream}".format(fqid=fqid,stream=stream)
        
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, params=None, headers=None, method='get'
        )

        self.save_progress("ret_val: {0}".format(ret_val))
        self.save_progress("response: {0}".format(response))

        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error while executing Get E-mail action, response: {}".format(response))

        action_result.add_data(response)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_ticket(self, param):
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("#####################################")

        fqid = param['fqid']      
        
        post_data = { 
            "id": param['assignee_id'] 
        }

        theEndpoint="/activity/events/{}/annotations/workflow/assignment".format(fqid)

        # make rest call
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, params=None, headers=None, json=post_data, method='put'
        )

        self.save_progress("response: {0}".format(response))
        self.save_progress("ret_val: {0}".format(ret_val))

        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error during Assign Owner action executing, response: {}".format(response))

        action_result.add_data(response)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_ticket(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))
        self.save_progress("#####################################")
        
        fqid = param.get('fqid', '')
        includes = param.get('includes', '')
        theEndpoint="/activity/events/{0}".format(fqid)
        
        # make rest call
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, params=None, headers=None
        )

        self.save_progress("response: {0}".format(response))
        self.save_progress("ret_val: {0}".format(ret_val))

        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error during Get Ticket action executing, response: {}".format(response))
        
        construct_timeline="{}/search/timeline?contextId={}&activityId={}&fqid={}&field=user.name&region=us-east-1&sources=email:pps"
        construct_timeline.format(self._base_url.replace("apis","apps"), response['contextId'], response['partitionKey'], fqid)

        timeline_url = {'timeline_url': construct_timeline}

        # Add the response into the data section
        action_result.add_data(response)
        action_result.add_data(timeline_url)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_comment(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))
        self.save_progress("#####################################")

        fqid = param['fqid']
        post_data= {
            "data": [ 
                {
                    "alias": "string", 
                    "kind": param['kind'],
                    "text": param['comment']
                }
            ]
        }

        theEndpoint="/activity/events/{fqid}/annotations/comments".format(fqid=fqid)

        # make rest call
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, method="post", params=None, headers=None, json=post_data
        )

        self.save_progress("ret_val: {0}".format(ret_val))
        self.save_progress("response: {0}".format(response))

        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error during Add Comment action executing, response: {}".format(response))

        action_result.add_data(response)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_users(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        parentStatuses = param.get('parentStatuses', '')

        parameters = {
            'alias': param['username'],
            'status': param['status'],
            'assignments': param['assignments'],
            'includeInactivePolicies': param['includeInactivePolicies'],
            'details.user.firstName': param['detailsuserfirstname'],
            'details.user.lastName': param['detailsuserlastname']
        }

        if param.get('offset'):
            parameters.update({'offset': int(param['offset'])})

        if param.get('limit'):
            parameters.update({'limit': int(param['limit'])})

        if param.get('includes'):
            parameters.update({'includes': param['includes']})

        parentStatuses_attrib=""
        if parentStatuses != "" and parentStatuses != "--":
            parentStatuses_attrib="status={0}&".format(parentStatuses)

        
        theEndpoint="/auth/users"       
        
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, params=parameters, headers=None, method='get'
        )
        self.save_progress("ret_val: {0}".format(ret_val))
        self.save_progress("response: {0}".format(response))
        
        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error during Get Users action executing, response: {}".format(response))

        action_result.add_data(response)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)
        
    def _handle_set_status(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))
        self.save_progress("#####################################")

        fqid = param['fqid']

        post_data= { 
            "state": { 
                "disposition": { 
                    "status": { 
                        "id": param['status_id'], 
                        "alias": param['status_title']
                    }, 
                    "category": param['status_category'] 
                }, 
                "assignee": { 
                    "id": param['assignee_id'] 
                }, 
                "actions": [ 
                    {
                        "kind": param['kind']
                    } 
                ] 
            } 
        }

        theEndpoint="/activity/events/{fqid}/annotations/workflow".format(fqid=fqid)

        # make rest call
        ret_val, response = self._make_rest_call(
            theEndpoint, action_result, method="patch", params=None, headers=None, json=post_data
        )

        self.save_progress("ret_val: {0}".format(ret_val))
        self.save_progress("response: {0}".format(response))

        if phantom.is_fail(ret_val):
            self.save_progress("#####################################")
            return action_result.set_status(phantom.APP_ERROR, "Error during Set Status action executing, response: {}".format(response))

        action_result.add_data(response)

        self.save_progress("#####################################")
        self.save_progress("#### ### ## #  SUCCESS  # ## ### ####")
        self.save_progress("#####################################")
        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):
        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == 'get_email':
            ret_val = self._handle_get_email(param)

        if action_id == 'update_ticket':
            ret_val = self._handle_update_ticket(param)

        if action_id == 'get_ticket':
            ret_val = self._handle_get_ticket(param)

        if action_id == 'add_comment':
            ret_val = self._handle_add_comment(param)

        if action_id == 'get_user':
            ret_val = self._handle_get_users(param)

        if action_id == 'set_status':
            ret_val = self._handle_set_status(param)

        if action_id == 'test_connectivity':
            ret_val = self._handle_test_connectivity(param)

        return ret_val

    def initialize(self):
        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        # get the asset config
        config = self.get_config()

        self._base_url = '{base_url}/{api_version}/apis'.format(base_url=config['base_url'], 
                                                                api_version=config.get('api_version'))
        self._client_id = config['client_id']
        self._client_secret = config['client_secret']

        return phantom.APP_SUCCESS

    def finalize(self):
        # Save the state, this data is saved across actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


def main():
    import argparse

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)

    args = argparser.parse_args()
    session_id = None

    username = args.username
    password = args.password

    if username is not None and password is None:

        # User specified a username but not a password, so ask
        import getpass
        password = getpass.getpass("Password: ")

    if username and password:
        try:
            login_url = PpItmConnector._get_phantom_base_url() + '/login'

            print("Accessing the Login page")
            r = requests.get(login_url, verify=False)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = dict()
            headers['Cookie'] = 'csrftoken=' + csrftoken
            headers['Referer'] = login_url

            print("Logging into Platform to get the session id")
            r2 = requests.post(login_url, verify=False, data=data, headers=headers)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: " + str(e))
            exit(1)

    with open(args.input_test_json) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = PpItmConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id
            connector._set_csrf_info(csrftoken, headers['Referer'])

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    exit(0)


if __name__ == '__main__':
    main()
