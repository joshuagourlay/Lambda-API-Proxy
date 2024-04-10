# backend-proxy-for-apis
This is a project I am using to act as a backend proxy to my API requests. Its intended goal is to receive incoming API requests, fetch the associated API key, then forward the request before returning the response back to the caller. It uses the singleton design pattern to keep the secrets between simultaneous invocations of the lambda.
