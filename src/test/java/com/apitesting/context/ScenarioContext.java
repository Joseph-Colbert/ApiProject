package com.josephcolbert.apitesting.context;

import io.restassured.response.Response;

public final class ScenarioContext {
    private String email;
    private String password;
    private String token;
    private int projectId;
    private Response response;

    public String email() {
        return email;
    }

    public void email(String email) {
        this.email = email;
    }

    public String password() {
        return password;
    }

    public void password(String password) {
        this.password = password;
    }

    public String token() {
        return token;
    }

    public void token(String token) {
        this.token = token;
    }

    public int projectId() {
        return projectId;
    }

    public void projectId(int projectId) {
        this.projectId = projectId;
    }

    public Response response() {
        return response;
    }

    public void response(Response response) {
        this.response = response;
    }
}

