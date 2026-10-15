package client;

public class FactoryRequest {
    public static IRequest make(String method) {
        return switch (method.toUpperCase()) {
            case "GET" -> new RequestGet();
            case "POST" -> new RequestPost();
            case "PUT" -> new RequestPut();
            case "DELETE" -> new RequestDelete();
            default -> throw new IllegalArgumentException("Invalid HTTP method: " + method);
        };
    }
}

