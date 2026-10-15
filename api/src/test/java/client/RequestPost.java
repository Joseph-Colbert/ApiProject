package client;

import io.restassured.response.Response;

public class RequestPost implements IRequest {
    @Override
    public Response send(RequestInfo info) {
        return info.request().body(info.getBody()).when().post(info.getUrl());
    }
}

