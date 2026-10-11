package com.josephcolbert.apitesting.config;

public final class TestConfig {
    public static final String BASE_URL = value("TODO_LY_BASE_URL", "https://todo.ly");
    public static final String TEST_PASSWORD = value("TODO_LY_TEST_PASSWORD", "ApiTesting#2026");

    private TestConfig() {
    }

    private static String value(String name, String defaultValue) {
        String value = System.getenv(name);
        return value == null || value.isBlank() ? defaultValue : value;
    }
}

