package com.josephcolbert.apitesting.client;

import com.josephcolbert.apitesting.config.TestConfig;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

import java.util.Map;

import static io.restassured.RestAssured.given;

public final class TodoLyClient {
    private RequestSpecification request() {
        return given()
                .baseUri(TestConfig.BASE_URL)
                .accept(ContentType.JSON)
                .contentType(ContentType.JSON)
                .log().method()
                .log().uri();
    }

    public Response createUser(Map<String, Object> body) {
        return request()
                .body(body)
                .when()
                .post("/api/user.json");
    }

    public Response getToken(String email, String password) {
        return request()
                .auth().preemptive().basic(email, password)
                .when()
                .get("/api/authentication/token.json");
    }

    public Response createProject(String token, Map<String, Object> body) {
        return tokenRequest(token)
                .body(body)
                .when()
                .post("/api/projects.json");
    }

    public Response getProject(String token, int projectId) {
        return tokenRequest(token)
                .when()
                .get("/api/projects/{id}.json", projectId);
    }

    public Response updateProject(String token, int projectId, Map<String, Object> body) {
        return tokenRequest(token)
                .body(body)
                .when()
                .put("/api/projects/{id}.json", projectId);
    }

    public Response deleteProject(String token, int projectId) {
        return tokenRequest(token)
                .when()
                .delete("/api/projects/{id}.json", projectId);
    }

    private RequestSpecification tokenRequest(String token) {
        return request().header("Token", token);
    }
}

