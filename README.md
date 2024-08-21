# Deployment-Webhook
>The deployment webhook is designed to automate the deployment process for the various microservices of the TESODEV Order Application. It is built using Flask and Docker, and it listens for incoming POST requests to trigger the deployment of specific services.

## How It Works

### 1. Webhook Endpoint
* The webhook is exposed at the /webhook route. When a POST request is sent to this endpoint, it includes a payload containing details about the repository that triggered the webhook.

### 2. Service Mapping
* The webhook has a predefined mapping of repositories to their corresponding services. Currently, the supported services are: 
```customer-service```
```order-service```
```gateway```
```rabbitmq-consumer```

### 3. Service Validation
* The webhook checks if the repository from the payload is listed in the predefined services. If it is not, the webhook returns an "Unauthorized" response.

### 4. Docker Operations
* ```Login```: The webhook uses the GitHub Container Registry (ghcr.io) for pulling Docker images. It logs in using credentials stored in environment variables (username and pat).

* ```Container Management```: If a container for the requested service is already running, it stops and removes the existing container.

* ```Image Pulling```: The webhook pulls the latest image for the service from the registry.

* ```Container Deployment```: A new container is started with the pulled image, and it is configured with the appropriate settings (e.g., ports, restart policy).

* ```Image Pruning```: After deployment, the webhook cleans up unused Docker images to save space.

### 5. Response
* Upon successful deployment, the webhook responds with "Success". If there are any issues during the process, relevant error messages are printed to the server's standard error stream.

# Setting up the Deployment Webhook
* Important Webhook Notes
    * Chnage the pywin package in requirements.txt to this
    ```
    pywin32;sys_platform == 'win32'
    ```
    * Install flask async
    ```
    pip install flask[async]
    ```
    * Customize webhook for the project
* Generate PAT in github

* Deploy Webhook
    ```
    docker login ghcr.io -u USERNAME -p <YOUR_PAT>
    
    docker run -d -p 5000:5000  --name=webhook --restart always -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/tesodev-order-application/deployment-webhook:main
    ```
* Removing and Reinstalling Guide
    * Remove Webhook Container
    ```
    docker ps -a
    docker stop <CONTAİNER_ID>
    docker rm <CONTAİNER_ID>
    ```

     * Remove Webhook Image
    ```
    docker images
    docker rmi <IMAGE_ID> 
    ```
* Removing old PAT Guide
    * Open docker login registery and delete old logins
    ```
    sudo nano ~/.docker/config.json
    ```
    ```
    https://www.redswitches.com/blog/fix-temporary-failure-in-name-resolution/#:~:text=Resolving%20the%20Temporary%20failure%20in,can%20ensure%20seamless%20internet%20connectivity.
    ```