"""
Copyright start
Copyright (C) 2008 - 2024 FortinetInc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""

import base64
from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger('cisco-esa')


class CiscoESA:
    def __init__(self, config):
        self.base_url = config.get('server_url').strip('/')
        if not self.base_url.startswith('https://'):
            self.base_url = 'https://{0}'.format(self.base_url)
        self.username = config['username']
        self.password = config['password']
        self.verify_ssl = config['verify_ssl']
        self.jwt_token = self.generate_jwt_token()

    def generate_jwt_token(self):
        data = {
            "data":
                {
                    "userName": base64.b64encode(self.username.encode('utf-8')).decode('utf-8'),
                    "passphrase": base64.b64encode(self.password.encode('utf-8')).decode('utf-8')
                }
        }
        response_token = self.make_rest_call('POST', '/esa/api/v2.0/login', json_data=data)
        jwt_token = response_token.get('data').get('jwtToken')
        return jwt_token

    def make_rest_call(self, method, endpoint, params=None, data=None, json_data=None, headers={}):
        if "login" in endpoint:
            headers = ({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
        else:
            headers.update({
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f"Basic {self.jwt_token}"
            })
        service_endpoint = self.base_url + endpoint
        try:
            logger.info(f"\nmethod: {method} - url: {service_endpoint}\nparams: {params}\ndata: {data}\njson_data: {json_data}")
            response = request(method, service_endpoint, verify=self.verify_ssl, params=params, data=data,
                               json=json_data, headers=headers)
            if response.status_code in response.ok:
                if response.text != "":
                    return response.json()
                else:
                    return True
            else:
                if response.text != "":
                    err_resp = response.text
                    error_msg = 'Response [{0}:Details: {1}]'.format(response.status_code, err_resp)
                else:
                    error_msg = 'Response [{0}:Details: {1}]'.format(response.status_code, response.content)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            raise ConnectorError(str(err))


def build_params(params):
    new_params = {}
    for k, v in params.items():
        if v is False or v == 0 or v:
            new_params[k] = v
    return new_params


def _check_health(config):
    ob = CiscoESA(config)
    endpoint = "/esa/api/v2.0/health"
    response = ob.make_rest_call("GET", endpoint)
    return True


def search_quarantine_messages(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    orderBy = params.get("orderBy")
    orderDir = params.get("orderDir")
    envelopeRecipientFilterOperator = params.get("envelopeRecipientFilterOperator")
    filterOperator = params.get("filterOperator")
    if orderBy:
        params.update(orderBy=ORDER_BY_MAPPING.get(orderBy))
    if orderDir:
        params.update(orderDir=SORT_MAPPING.get(orderDir))
    if envelopeRecipientFilterOperator:
        params.update(envelopeRecipientFilterOperator=FILTER_MAPPING.get(envelopeRecipientFilterOperator))
    if filterOperator:
        params.update(filterOperator=FILTER_MAPPING.get(filterOperator))
    endpoint = "/esa/api/v2.0/quarantine/messages"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def get_quarantine_message(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    endpoint = "/esa/api/v2.0/quarantine/messages/details"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def release_quarantine_message(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    mids = str(params["mids"])
    params.update(mids=mids.split(","))
    endpoint = "/esa/api/v2.0/quarantine/messages"
    response = ob.make_rest_call("POST", endpoint, json_data=params)
    return response


def delete_quarantine_message(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    mids = str(params["mids"])
    params.update(mids=mids.split(","))
    endpoint = "/esa/api/v2.0/quarantine/messages"
    response = ob.make_rest_call("DELETE", endpoint, json_data=params)
    return response


def search_safelist_or_blocklist_entries(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    safelist_or_blocklist = params.pop('safelist_or_blocklist').lower()
    viewBy = params.get("viewBy")
    orderBy = params.get("orderBy")
    orderDir = params.get("orderDir")
    if viewBy:
        params.update(viewBy=viewBy.lower())
    if orderBy:
        params.update(orderBy=orderBy.lower())
    if orderDir:
        params.update(orderDir=SORT_MAPPING.get(orderDir))
    endpoint = f"/esa/api/v2.0/quarantine/{safelist_or_blocklist}"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def edit_safelist_or_blocklist_entries(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    safelist_or_blocklist = params.pop('safelist_or_blocklist').lower()
    params.update(action=params["action"].lower())
    viewBy = params.get("viewBy")
    recipientAddresses = params.get("recipientAddresses")
    recipientList = params.get("recipientList")
    senderAddresses = params.get("senderAddresses")
    senderList = params.get("senderList")
    if viewBy:
        params.update(viewBy=viewBy.lower())
    if recipientAddresses:
        params.update(recipientAddresses=recipientAddresses.split(","))
    if recipientList:
        params.update(recipientList=recipientList.split(","))
    if senderAddresses:
        params.update(senderAddresses=senderAddresses.split(","))
    if senderList:
        params.update(senderList=senderList.split(","))
    endpoint = f"/esa/api/v2.0/quarantine/{safelist_or_blocklist}"
    response = ob.make_rest_call("POST", endpoint, json_data=params)
    return response


def delete_safelist_or_blocklist_entries(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    safelist_or_blocklist = params.pop('safelist_or_blocklist').lower()
    viewBy = params.get("viewBy")
    recipientList = params.get("recipientList")
    senderList = params.get("senderList")
    if viewBy:
        params.update(viewBy=viewBy.lower())
    if recipientList:
        params.update(recipientList=recipientList.split(","))
    if senderList:
        params.update(senderList=senderList.split(","))
    endpoint = f"/esa/api/v2.0/quarantine/{safelist_or_blocklist}"
    response = ob.make_rest_call("DELETE", endpoint, json_data=params)
    return response


def get_message_dlp_details(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    endpoint = f"/esa/api/v2.0/message-tracking/dlp-details"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def get_message_amp_details(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    endpoint = f"/esa/api/v2.0/message-tracking/amp-details"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def get_message_url_details(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    endpoint = f"/esa/api/v2.0/message-tracking/url-details"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


def get_report(config, params):
    ob = CiscoESA(config)
    params = build_params(params)
    reportType = params.pop("reportType")
    orderDir = params.get("orderDir")
    filterOperator = params.get("filterOperator")
    if reportType in REPORT_TYPE_MAPPING:
        reportType = REPORT_TYPE_MAPPING.get(reportType)
    if orderDir:
        params.update(orderDir=SORT_MAPPING.get(orderDir))
    if filterOperator:
        params.update(filterOperator=FILTER_MAPPING.get(filterOperator))
    endpoint = f"/esa/api/v2.0/reporting/{reportType}"
    response = ob.make_rest_call("GET", endpoint, params=params)
    return response


operations = {
    "search_quarantine_messages": search_quarantine_messages,
    "get_quarantine_message": get_quarantine_message,
    "release_quarantine_message": release_quarantine_message,
    "delete_quarantine_message": delete_quarantine_message,
    "search_safelist_or_blocklist_entries": search_safelist_or_blocklist_entries,
    "edit_safelist_or_blocklist_entries": edit_safelist_or_blocklist_entries,
    "delete_safelist_or_blocklist_entries": delete_safelist_or_blocklist_entries,
    "get_message_dlp_details": get_message_dlp_details,
    "get_message_amp_details": get_message_amp_details,
    "get_message_url_details": get_message_url_details,
    "get_report": get_report
}
