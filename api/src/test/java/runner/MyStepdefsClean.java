package runner;

import client.FactoryRequest;
import client.RequestInfo;
import config.Configuration;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.response.Response;

import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.blankOrNullString;

public class MyStepdefsClean {
    private Response response;
    private final Map<String, String> variables = new HashMap<>();

    @Given("un usuario nuevo registrado en Todo.ly")
    public void createUser() {
        String email = "apitesting+" + Instant.now().toEpochMilli() + "-"
                + UUID.randomUUID().toString().substring(0, 8) + "@example.com";
        variables.put("EMAIL", email);
        variables.put("PASSWORD", Configuration.TEST_PASSWORD);

        response = FactoryRequest.make("POST").send(new RequestInfo(
                Configuration.BASE_URL + "/api/user.json",
                "{\"Email\":\"" + email + "\",\"FullName\":\"API Testing Candidate\",\"Password\":\""
                        + Configuration.TEST_PASSWORD + "\"}"
        ));
        response.then().statusCode(200).body("Email", equalTo(email));
    }

    @And("obtengo el token de autenticacion del usuario")
    public void getToken() {
        response = FactoryRequest.make("GET").send(RequestInfo.withBasicAuth(
                Configuration.BASE_URL + "/api/authentication/token.json",
                "",
                variables.get("EMAIL"),
                variables.get("PASSWORD")
        ));
        response.then().statusCode(200).body("TokenString", not(blankOrNullString()));
        variables.put("TOKEN", response.jsonPath().getString("TokenString"));
    }

    @When("creo un proyecto llamado {string} usando el token")
    public void createProject(String name) {
        sendTokenRequest("POST", "/api/projects.json", "{\"Content\":\"" + name + "\"}");
        response.then().statusCode(200).body("Content", equalTo(name));
        variables.put("ID_PROJECT", response.jsonPath().getString("Id"));
    }

    @Then("puedo consultar el proyecto {string} usando el token")
    public void getProject(String name) {
        sendTokenRequest("GET", "/api/projects/ID_PROJECT.json", "");
        response.then().statusCode(200).body("Content", equalTo(name));
    }

    @When("actualizo el proyecto a {string} usando el token")
    public void updateProject(String name) {
        sendTokenRequest("PUT", "/api/projects/ID_PROJECT.json", "{\"Content\":\"" + name + "\"}");
        response.then().statusCode(200).body("Content", equalTo(name));
    }

    @Then("elimino el proyecto usando el token")
    public void deleteProject() {
        sendTokenRequest("DELETE", "/api/projects/ID_PROJECT.json", "");
        response.then().statusCode(200).body("Deleted", equalTo(true));
    }

    private void sendTokenRequest(String method, String path, String body) {
        String url = Configuration.BASE_URL + replaceVariables(path);
        response = FactoryRequest.make(method).send(RequestInfo.withToken(
                url,
                body,
                variables.get("TOKEN")
        ));
    }

    private String replaceVariables(String value) {
        for (Map.Entry<String, String> entry : variables.entrySet()) {
            value = value.replace(entry.getKey(), entry.getValue());
        }
        return value;
    }
}

