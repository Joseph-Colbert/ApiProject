package config;

public final class Configuration {
    public static final String BASE_URL = value("TODO_LY_BASE_URL", "https://todo.ly");
    public static final String TEST_PASSWORD = value("TODO_LY_TEST_PASSWORD", "ApiTesting#2026");

    private Configuration() {
    }

    private static String value(String name, String fallback) {
        String value = System.getenv(name);
        return value == null || value.isBlank() ? fallback : value;
    }
}

