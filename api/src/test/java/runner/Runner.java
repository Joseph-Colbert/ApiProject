package runner;

import io.cucumber.java.After;
import io.cucumber.java.Before;

public class Runner {
    @Before
    public void beforeCucumber() {
        System.out.println("Before Cucumber");
    }

    @After
    public void afterCucumber() {
        System.out.println("After Cucumber");
    }
}

