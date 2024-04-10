# Lambda API Proxy

This project serves as a backend proxy for API requests. Its primary purpose is to receive incoming API requests, retrieve the associated API key, forward the request to the target API, and return the response back to the caller. The project utilizes the Singleton design pattern to efficiently manage and store secrets across simultaneous invocations of the AWS Lambda function.

## Features

- Receives incoming API requests and extracts relevant information such as HTTP method, body, query parameters, path parameters, and headers.
- Retrieves the associated API key from AWS Secrets Manager based on the requested path.
- Forwards the API request to the target API using the retrieved API key.
- Returns the API response back to the caller.
- Utilizes the Singleton design pattern to efficiently manage secrets across multiple Lambda invocations.

## Architecture

The project follows a modular architecture to ensure maintainability and extensibility. Here's an overview of the main components:

- `lambda_function.py`: The entry point of the Lambda function. It receives the incoming event and context, invokes the `main` function from `main.py`, and returns the response.
- `main.py`: Contains the core logic of the Lambda function. It parses the incoming event, extracts relevant information, and generates the appropriate response based on the requested path.
- `models/models.py`: Defines the `Secrets` class, which is implemented as a Singleton. It handles the loading and retrieval of secrets from AWS Secrets Manager.
- `services/api_requester.py`: Provides a utility function to make API requests using the `requests` library.
- `utils/constants.py`: Defines constant values used throughout the project, such as the Firebase API key name.

## Setup and Deployment

To set up and deploy this project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the AWS credentials and region in your local environment or AWS CLI.
4. Update the `secrets_arn` environment variable in `models.py` with the ARN of your AWS Secrets Manager secret.
5. Deploy the Lambda function using AWS CLI or any preferred deployment method.
6. Configure the necessary API Gateway routes to trigger the Lambda function based on the desired paths.

## Usage

Once the Lambda function is deployed and the API Gateway is configured, you can make API requests to the defined paths. The Lambda function will handle the request, retrieve the associated API key, forward the request to the target API, and return the response back to the caller.

Example paths:
- `/dev/get-firebase-key`: Retrieves the Firebase API key.
- `/dev/get-other-service-key`: Placeholder for retrieving other service keys (not implemented yet).

## Future Enhancements

- Implement additional paths and logic for retrieving API keys of other services.
- Add error handling and logging to improve visibility and debugging.
- Implement caching mechanisms to reduce the overhead of retrieving secrets from AWS Secrets Manager.
- Enhance security by implementing authentication and authorization mechanisms.
- Optimize performance by leveraging async programming techniques.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
