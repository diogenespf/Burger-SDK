"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from apitizing_burgers import utils
from apitizing_burgers._hooks import HookContext
from apitizing_burgers.models import components, errors, operations
from typing import List, Optional

class Burger:
    r"""Operations related to burgers
    https://en.wikipedia.org/wiki/Hamburger - Burger external docs
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def list_burgers(self, retries: Optional[utils.RetryConfig] = None) -> operations.ListBurgersResponse:
        r"""List Burgers
        List all burgers
        """
        hook_ctx = HookContext(operation_id='listBurgers', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/burger/'
        
        headers = {}
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5XX'
        ]))
        
        
        res = operations.ListBurgersResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[List[components.BurgerOutput]])
                res.response_listburgers = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def create_burger(self, request: components.BurgerCreate, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBurgerResponse:
        r"""Create Burger
        Create a burger
        """
        hook_ctx = HookContext(operation_id='createBurger', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/burger/'
        
        headers = {}
        
        req_content_type, data, form = utils.serialize_request_body(request, components.BurgerCreate, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('POST', url, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['422','4XX','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5XX'
        ]))
        
        
        res = operations.CreateBurgerResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.BurgerOutput])
                res.burger_output = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def read_burger(self, burger_id: int, retries: Optional[utils.RetryConfig] = None) -> operations.ReadBurgerResponse:
        r"""Read Burger
        Read a burger
        """
        hook_ctx = HookContext(operation_id='readBurger', oauth2_scopes=[], security_source=None)
        request = operations.ReadBurgerRequest(
            burger_id=burger_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ReadBurgerRequest, base_url, '/burger/{burger_id}', request)
        
        headers = {}
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('GET', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['404','422','4XX','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5XX'
        ]))
        
        
        res = operations.ReadBurgerResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.BurgerOutput])
                res.burger_output = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ResponseMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def update_burger(self, burger_id: int, burger_update: components.BurgerUpdate, retries: Optional[utils.RetryConfig] = None) -> operations.UpdateBurgerResponse:
        r"""Update Burger
        Update a burger
        """
        hook_ctx = HookContext(operation_id='updateBurger', oauth2_scopes=[], security_source=None)
        request = operations.UpdateBurgerRequest(
            burger_id=burger_id,
            burger_update=burger_update,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateBurgerRequest, base_url, '/burger/{burger_id}', request)
        
        headers = {}
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.UpdateBurgerRequest, "burger_update", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('PUT', url, data=data, files=form, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['404','422','4XX','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5XX'
        ]))
        
        
        res = operations.UpdateBurgerResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.BurgerOutput])
                res.burger_output = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ResponseMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def delete_burger(self, burger_id: int, retries: Optional[utils.RetryConfig] = None) -> operations.DeleteBurgerResponse:
        r"""Delete Burger
        Delete a burger
        """
        hook_ctx = HookContext(operation_id='deleteBurger', oauth2_scopes=[], security_source=None)
        request = operations.DeleteBurgerRequest(
            burger_id=burger_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteBurgerRequest, base_url, '/burger/{burger_id}', request)
        
        headers = {}
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    hook_ctx, 
                    requests_http.Request('DELETE', url, headers=headers).prepare(),
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
                raise e

            if utils.match_status_codes(['404','422','4XX','5XX'], http_res.status_code):
                http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
                if e:
                    raise e
            else:
                result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
                if isinstance(result, Exception):
                    raise result
                http_res = result

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5XX'
        ]))
        
        
        res = operations.DeleteBurgerResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[errors.ResponseMessage])
                res.response_message = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.ResponseMessage)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    