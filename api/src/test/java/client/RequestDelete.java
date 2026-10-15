package client;

import io.restassured.response.Response;

public class RequestDelete implements IRequest {
    @Override
    public Response send(RequestInfo info) {
        return info.request().when().delete(info.getUrl());
    }
}

