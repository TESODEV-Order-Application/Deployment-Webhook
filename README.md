# Deployment-Webhook
The webhook repository for the TESODEV Order Application Project
> Ubuntu 22.04

## 1. Setting up the Deployment Webhook
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