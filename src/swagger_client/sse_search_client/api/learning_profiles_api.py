# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sse_search_client.api_client import ApiClient


class LearningProfilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def learning_profile_controller_add_learning_profile(self, body, **kwargs):  # noqa: E501
        """learning_profile_controller_add_learning_profile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_add_learning_profile(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LearningProfileCreationDto body: (required)
        :return: LearningProfileCreationDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.learning_profile_controller_add_learning_profile_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.learning_profile_controller_add_learning_profile_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def learning_profile_controller_add_learning_profile_with_http_info(self, body, **kwargs):  # noqa: E501
        """learning_profile_controller_add_learning_profile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_add_learning_profile_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LearningProfileCreationDto body: (required)
        :return: LearningProfileCreationDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method learning_profile_controller_add_learning_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `learning_profile_controller_add_learning_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/learning-profiles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LearningProfileCreationDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def learning_profile_controller_del_learning_profile_by_id(self, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_del_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_del_learning_profile_by_id(learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.learning_profile_controller_del_learning_profile_by_id_with_http_info(learning_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.learning_profile_controller_del_learning_profile_by_id_with_http_info(learning_profile_id, **kwargs)  # noqa: E501
            return data

    def learning_profile_controller_del_learning_profile_by_id_with_http_info(self, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_del_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_del_learning_profile_by_id_with_http_info(learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learning_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method learning_profile_controller_del_learning_profile_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learning_profile_id' is set
        if ('learning_profile_id' not in params or
                params['learning_profile_id'] is None):
            raise ValueError("Missing the required parameter `learning_profile_id` when calling `learning_profile_controller_del_learning_profile_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learning_profile_id' in params:
            path_params['learning_profile_id'] = params['learning_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/learning-profiles/{learning_profile_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def learning_profile_controller_get_learning_profile_by_id(self, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_get_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_get_learning_profile_by_id(learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.learning_profile_controller_get_learning_profile_by_id_with_http_info(learning_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.learning_profile_controller_get_learning_profile_by_id_with_http_info(learning_profile_id, **kwargs)  # noqa: E501
            return data

    def learning_profile_controller_get_learning_profile_by_id_with_http_info(self, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_get_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_get_learning_profile_by_id_with_http_info(learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_profile_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learning_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method learning_profile_controller_get_learning_profile_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learning_profile_id' is set
        if ('learning_profile_id' not in params or
                params['learning_profile_id'] is None):
            raise ValueError("Missing the required parameter `learning_profile_id` when calling `learning_profile_controller_get_learning_profile_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learning_profile_id' in params:
            path_params['learning_profile_id'] = params['learning_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/learning-profiles/{learning_profile_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def learning_profile_controller_patch_learning_profile_by_id(self, body, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_patch_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_patch_learning_profile_by_id(body, learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LearningProfileDto body: (required)
        :param str learning_profile_id: (required)
        :return: LearningProfileCreationDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.learning_profile_controller_patch_learning_profile_by_id_with_http_info(body, learning_profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.learning_profile_controller_patch_learning_profile_by_id_with_http_info(body, learning_profile_id, **kwargs)  # noqa: E501
            return data

    def learning_profile_controller_patch_learning_profile_by_id_with_http_info(self, body, learning_profile_id, **kwargs):  # noqa: E501
        """learning_profile_controller_patch_learning_profile_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.learning_profile_controller_patch_learning_profile_by_id_with_http_info(body, learning_profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LearningProfileDto body: (required)
        :param str learning_profile_id: (required)
        :return: LearningProfileCreationDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'learning_profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method learning_profile_controller_patch_learning_profile_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `learning_profile_controller_patch_learning_profile_by_id`")  # noqa: E501
        # verify the required parameter 'learning_profile_id' is set
        if ('learning_profile_id' not in params or
                params['learning_profile_id'] is None):
            raise ValueError("Missing the required parameter `learning_profile_id` when calling `learning_profile_controller_patch_learning_profile_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learning_profile_id' in params:
            path_params['learning_profile_id'] = params['learning_profile_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/learning-profiles/{learning_profile_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LearningProfileCreationDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)