# coding: utf-8

"""
    L3S Recommendation Service for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 0.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from l3s_recsys_client.api_client import ApiClient


class RandomRecommendationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_get_random_paths(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_paths  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_paths(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_get_random_paths_with_http_info(num_of_recs, **kwargs)  # noqa: E501
        else:
            (data) = self.get_get_random_paths_with_http_info(num_of_recs, **kwargs)  # noqa: E501
            return data

    def get_get_random_paths_with_http_info(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_paths  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_paths_with_http_info(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['num_of_recs', 'orga_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_random_paths" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'num_of_recs' is set
        if ('num_of_recs' not in params or
                params['num_of_recs'] is None):
            raise ValueError("Missing the required parameter `num_of_recs` when calling `get_get_random_paths`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num_of_recs' in params:
            query_params.append(('num_of_recs', params['num_of_recs']))  # noqa: E501
        if 'orga_ids' in params:
            query_params.append(('orga_ids', params['orga_ids']))  # noqa: E501
            collection_formats['orga_ids'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/random/get-random-paths', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoRandomResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_get_random_skill(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_skill(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_get_random_skill_with_http_info(num_of_recs, **kwargs)  # noqa: E501
        else:
            (data) = self.get_get_random_skill_with_http_info(num_of_recs, **kwargs)  # noqa: E501
            return data

    def get_get_random_skill_with_http_info(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_skill_with_http_info(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['num_of_recs', 'orga_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_random_skill" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'num_of_recs' is set
        if ('num_of_recs' not in params or
                params['num_of_recs'] is None):
            raise ValueError("Missing the required parameter `num_of_recs` when calling `get_get_random_skill`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num_of_recs' in params:
            query_params.append(('num_of_recs', params['num_of_recs']))  # noqa: E501
        if 'orga_ids' in params:
            query_params.append(('orga_ids', params['orga_ids']))  # noqa: E501
            collection_formats['orga_ids'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/random/get-random-skill', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoRandomResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_get_random_tasks(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_tasks(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_get_random_tasks_with_http_info(num_of_recs, **kwargs)  # noqa: E501
        else:
            (data) = self.get_get_random_tasks_with_http_info(num_of_recs, **kwargs)  # noqa: E501
            return data

    def get_get_random_tasks_with_http_info(self, num_of_recs, **kwargs):  # noqa: E501
        """get_get_random_tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_random_tasks_with_http_info(num_of_recs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int num_of_recs: (required)
        :param list[str] orga_ids:
        :return: DtoRandomResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['num_of_recs', 'orga_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_random_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'num_of_recs' is set
        if ('num_of_recs' not in params or
                params['num_of_recs'] is None):
            raise ValueError("Missing the required parameter `num_of_recs` when calling `get_get_random_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num_of_recs' in params:
            query_params.append(('num_of_recs', params['num_of_recs']))  # noqa: E501
        if 'orga_ids' in params:
            query_params.append(('orga_ids', params['orga_ids']))  # noqa: E501
            collection_formats['orga_ids'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/random/get-random-tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoRandomResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
