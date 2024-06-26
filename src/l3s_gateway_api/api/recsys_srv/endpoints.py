## import libraries
from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse
from http import HTTPStatus
import requests, json
import os, socket
import dataclasses, json
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

### import exceptions
from werkzeug.exceptions import BadRequest
from requests.exceptions import InvalidURL

from swagger_client import l3s_recsys_client
from swagger_client.l3s_recsys_client.rest import ApiException
from swagger_client.l3s_recsys_client.models.test import Test as TestDto
from swagger_client.l3s_recsys_client.models.dto_random_response import DtoRandomResponse
from swagger_client.l3s_recsys_client.models.dto_jobs_search_response import DtoJobsSearchResponse

## Configuration L3S Recsys
l3s_recsys_config = l3s_recsys_client.Configuration()
# l3s_recsys_config.host = "https://staging.sse.uni-hildesheim.de:9042/l3s-recsys/"

l3s_recsys_config.host = os.getenv('L3S_RECSYS_HOST')
print("*"*80)
print('l3s-recsys-service-host:', l3s_recsys_config.host)
print("*"*80)

client_l3s_recsys = l3s_recsys_client.ApiClient(configuration=l3s_recsys_config)
recsys_test_api = l3s_recsys_client.TestsApi(api_client=client_l3s_recsys)
recsys_random_api = l3s_recsys_client.RandomRecommendationApi(api_client=client_l3s_recsys)
recsys_trends_api = l3s_recsys_client.TrendsApi(api_client=client_l3s_recsys)

ns_recsys_srv = Namespace("Recsys Service", validate=True, description="downstream endpoints for recsys services")


from .dto import dto_recommendation_object, dto_recsys_connection_response
ns_recsys_srv.models[dto_recommendation_object.name] = dto_recommendation_object
ns_recsys_srv.models[dto_recsys_connection_response.name] = dto_recsys_connection_response


## Test
@ns_recsys_srv.route('/connection', endpoint="recsys_service_connection")
class RecommendationService(Resource):
    @ns_recsys_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_recsys_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_recsys_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_recsys_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_recsys_srv.marshal_with(dto_recsys_connection_response)
    def get(self):
        # url = os.getenv('L3S_SEARCH_HOST')+'/'
        url = l3s_recsys_config.host + '/'
        print(url)
        
        result = {}
        try:
            response = requests.head(url)
            if response.status_code == 200:
                result.update({"host_url": url, "status": 'success'})
                return result, HTTPStatus.OK
            else:
                result.update({"host_url": url, "status": 'failed'})
                return result, HTTPStatus.INTERNAL_SERVER_ERROR
        except requests.ConnectionError as e:
            result = {"host_url": url}
            result.update({"status": e.args[0]})
            return result, HTTPStatus.NOT_FOUND
        except InvalidURL as e:
            result = {"host_url": url}
            result.update({"status": e.args[0]})
            return result, HTTPStatus.BAD_REQUEST



## Random API
get_n_random_rec_parser = reqparse.RequestParser()
get_n_random_rec_parser.add_argument('num_of_recs', type=int, location='args', default=10)

@ns_recsys_srv.route('/random-recs/get-n-paths')
class GetNRandomRecommendation(Resource):
    @ns_recsys_srv.expect(get_n_random_rec_parser)
    def get(self):
        args=get_n_random_rec_parser.parse_args()
        
        request_data = dict(args)
        try:
        # Get list of exposure types
            print(recsys_random_api.api_client.configuration.host)
            api_response = recsys_random_api.get_get_random_paths(num_of_recs=request_data["num_of_recs"])
            d = DtoRandomResponse(message=api_response.message, type=api_response.type, results=api_response.results)
            
            response = jsonify(d.to_dict())
            
            response.status_code = 200
            return response
        
        except ApiException as e:
            return ("Exception when calling Api-> %s\n" % e)

@ns_recsys_srv.route('/random-recs/get-n-skills')
class GetNRandomSkills(Resource):
    @ns_recsys_srv.expect(get_n_random_rec_parser)
    def get(self):
        args=get_n_random_rec_parser.parse_args()
        
        request_data = dict(args)
        try:
        # Get list of exposure types
            print(recsys_random_api.api_client.configuration.host)
            api_response = recsys_random_api.get_get_random_skill(num_of_recs=request_data["num_of_recs"])
            d = DtoRandomResponse(message=api_response.message, type=api_response.type, results=api_response.results)
            
            response = jsonify(d.to_dict())
            
            response.status_code = 200
            return response
        
        except ApiException as e:
            return ("Exception when calling Api-> %s\n" % e)


@ns_recsys_srv.route('/random-recs/get-n-tasks')
class GetNRandomTasks(Resource):
    @ns_recsys_srv.expect(get_n_random_rec_parser)
    def get(self):
        args=get_n_random_rec_parser.parse_args()
        
        request_data = dict(args)
        try:
        # Get list of exposure types
            print(recsys_random_api.api_client.configuration.host)
            api_response = recsys_random_api.get_get_random_tasks(num_of_recs=request_data["num_of_recs"])
            d = DtoRandomResponse(message=api_response.message, type=api_response.type, results=api_response.results)
            
            response = jsonify(d.to_dict())
            
            response.status_code = 200
            return response
        
        except ApiException as e:
            return ("Exception when calling Api-> %s\n" % e)



## Trends
trends_search_jobs_parser = reqparse.RequestParser()
trends_search_jobs_parser.add_argument('loc', required=True, type=str, location='args', default='berlin')
trends_search_jobs_parser.add_argument('job_name', required=True, type=str, location='args', default='machine learning')
trends_search_jobs_parser.add_argument('radius', type=int, location='args', default=5)
@ns_recsys_srv.route('/trends/search-jobs')
class TrendsSearchJobs(Resource):
    @ns_recsys_srv.expect(trends_search_jobs_parser)
    def get(self):
        args=get_n_random_rec_parser.parse_args()
        
        request_data = dict(args)
        try:
        # Get list of exposure types
            print(recsys_random_api.api_client.configuration.host)
            api_response = recsys_trends_api.get_search_jobs(loc=args['loc'], job_name=args['job_name'], radius=args['radius'])
            d = DtoJobsSearchResponse(job_offers=api_response.job_offsers)
            
            response = jsonify(d.to_dict())
            
            response.status_code = 200
            return response
        
        except ApiException as e:
            return ("Exception when calling Api-> %s\n" % e)



# from .dto import dto_get_recommendation_reponse
# ns_recsys_srv.models[dto_get_recommendation_reponse.name] = dto_get_recommendation_reponse
# parser_owners = reqparse.RequestParser()
# parser_owners.add_argument("owners", action='split', type=str, location='args')

# @ns_recsys_srv.route("/<string:user_id>/trends", endpoint="get_user_trends")
# class RecUserTrends(Resource):
#     @ns_recsys_srv.expect(parser_owners)
#     @ns_recsys_srv.marshal_with(dto_get_recommendation_reponse)
#     @ns_recsys_srv.response(int(HTTPStatus.OK), "request for getting trends processed successfully")
#     @ns_recsys_srv.response(int(HTTPStatus.BAD_REQUEST), "invalid user id")
#     @ns_recsys_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     def get(self, user_id):
#         """in progress"""
#         args=parser_owners.parse_args()
#         request_data = dict(args)
#         owners = request_data.get("owners")
#         #logic: send request to aimeta-service
#         print(owners)
#         results = {}
#         response = {"results": results}
#         return response, HTTPStatus.OK
    

##
# @ns_recsys_srv.route("/<string:user_id>/interests", endpoint="get_rec_interests")
# class RecUserInterests(Resource):
#     @ns_recsys_srv.expect(parser_owners)
#     @ns_recsys_srv.marshal_with(dto_get_recommendation_reponse)
#     def get(self, user_id):
#         """in progress"""
#         args=parser_owners.parse_args()
#         request_data = dict(args)
#         owners = request_data.get("owners")
#         print(owners)
        
#         return {"results": []}
    

# @ns_recsys_srv.route("/<string:user_id>/learning-goal")
# class RecUserLearningGoal(Resource):
#     @ns_recsys_srv.expect(parser_owners)
#     @ns_recsys_srv.marshal_with(dto_get_recommendation_reponse)
#     def get(self, user_id):
#         """in progress"""
#         args=parser_owners.parse_args()
#         request_data = dict(args)
#         owners = request_data.get("owners")
#         print(owners)
        
#         return {"results": []}
    

# @ns_recsys_srv.route("/<string:user_id>/company")
# class RecUserComany(Resource):
#     @ns_recsys_srv.expect(parser_owners)
#     @ns_recsys_srv.marshal_with(dto_get_recommendation_reponse)
#     def get(self, user_id):
#         """in progress"""
#         args=parser_owners.parse_args()
#         request_data = dict(args)
#         owners = request_data.get("owners")
#         print(owners)
        
#         return {"results": []}
    

# @ns_recsys_srv.route("/<string:user_id>/sibblings")
# class RecUserSibblings(Resource):
#     @ns_recsys_srv.expect(parser_owners)
#     @ns_recsys_srv.marshal_with(dto_get_recommendation_reponse)
#     def get(self, user_id):
#         """in progress"""
#         args=parser_owners.parse_args()
#         request_data = dict(args)
#         owners = request_data.get("owners")
#         print(owners)
        
#         return {"results": []}