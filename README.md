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

## APIs

- URL: /doc<br>
  Method: GET<br>
  Description: open API docs of project

- URL: /get-all-products<br>
  Method: GET<br>
  Description: get all products from postgres database

- URL: /get-product<br>
  Method: GET<br>
  Description: get product from cache or postgres database using product id

- URL: /fetch-users<br>
  Method: POST<br>
  Body: {"count": <integerValue>}
  Description: create celery tasks to fetch and store users in mongodb and postgresdb

- URL: postgres/get-users<br>
  Method: GET<br>
  Description: get all users from postgres database

- URL: mongo/get-users<br>
  Method: GET<br>
  Description: get all users from mongo database

