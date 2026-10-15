package client;

import io.restassured.response.Response;

public class RequestGet implements IRequest {
    @Override
    public Response send(RequestInfo info) {
        return info.request().when().get(info.getUrl());
    }
}

