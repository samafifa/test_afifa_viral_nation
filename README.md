## Instruction to Setup and Run django project

### Requirements
- Docker

To setup Docker please follow the instructions on the following links

- https://learn.microsoft.com/en-us/windows/wsl/install-manual
- https://docs.docker.com/desktop/install/windows-install/

Run Project
- Open cmd or powershell or bash in test_afifa folder which contains Dockerfile and docker-compose file
- Run the following command to build the required project docker containers<br>
`docker-compose build`
- Run the following command to run the project<br>
`docker-compose up`
- The APIs will be accessible on http://localhost:8000
- To stop/exit the project run the following command<br>
`docker-compose down`