package com.josephcolbert.apitesting.steps;

import com.josephcolbert.apitesting.client.TodoLyClient;
import com.josephcolbert.apitesting.config.TestConfig;
import com.josephcolbert.apitesting.context.ScenarioContext;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import java.time.Instant;
import java.util.Map;
import java.util.UUID;

import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.blankOrNullString;

public final class ProjectCrudSteps {
    private final TodoLyClient client = new TodoLyClient();
    private final ScenarioContext context = new ScenarioContext();

    @Given("un usuario nuevo registrado en Todo.ly")
    public void createUser() {
        String unique = Instant.now().toEpochMilli() + "-" + UUID.randomUUID().toString().substring(0, 8);
        context.email("apitesting+" + unique + "@example.com");
        context.password(TestConfig.TEST_PASSWORD);

        context.response(client.createUser(Map.of(
                "Email", context.email(),
                "FullName", "API Testing Candidate",
                "Password", context.password()
        )));

        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("Email", equalTo(context.email()));
    }

    @And("obtengo el token de autenticacion del usuario")
    public void getAuthenticationToken() {
        context.response(client.getToken(context.email(), context.password()));
        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("TokenString", not(blankOrNullString()));
        context.token(context.response().jsonPath().getString("TokenString"));
    }

    @When("creo un proyecto llamado {string} usando el token")
    public void createProject(String name) {
        context.response(client.createProject(context.token(), Map.of("Content", name)));
        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("Content", equalTo(name))
                .body("Deleted", equalTo(false));
        context.projectId(context.response().jsonPath().getInt("Id"));
    }

    @Then("puedo consultar el proyecto {string} usando el token")
    public void getProject(String name) {
        context.response(client.getProject(context.token(), context.projectId()));
        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("Id", equalTo(context.projectId()))
                .body("Content", equalTo(name));
    }

    @When("actualizo el proyecto a {string} usando el token")
    public void updateProject(String name) {
        context.response(client.updateProject(
                context.token(),
                context.projectId(),
                Map.of("Content", name)
        ));
        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("Id", equalTo(context.projectId()))
                .body("Content", equalTo(name));
    }

    @Then("elimino el proyecto usando el token")
    public void deleteProject() {
        context.response(client.deleteProject(context.token(), context.projectId()));
        context.response().then()
                .log().ifValidationFails()
                .statusCode(200)
                .body("Id", equalTo(context.projectId()))
                .body("Deleted", equalTo(true));
    }
}

