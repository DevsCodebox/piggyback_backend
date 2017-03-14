from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from connections import Connections

class AddNewSSID(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(AddNewSSID, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        ssid = data.get('ssid')
        ssid_strength = data.get('ssid_strength')
        response = {}
        if Connections.add_new_ssid(ssid, ssid_strength):
            response['response'] = "SSID updated"
        else:
            response['response'] = "SSID Failed to Create"
        return jsonify(response)