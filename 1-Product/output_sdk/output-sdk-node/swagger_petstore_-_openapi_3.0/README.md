# node SDK for Swagger Petstore - OpenAPI 3.0

## Description
This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:
- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

## Endpoints Overview
- `POST /pet`: Add a new pet to the store
- `PUT /pet`: Update an existing pet
- `GET /pet/findByStatus`: Finds Pets by status
- `GET /pet/findByTags`: Finds Pets by tags
- `GET /pet/{petId}`: Find pet by ID
- `POST /pet/{petId}`: Updates a pet in the store with form data
- `DELETE /pet/{petId}`: Deletes a pet
- `POST /pet/{petId}/uploadImage`: uploads an image
- `GET /store/inventory`: Returns pet inventories by status
- `POST /store/order`: Place an order for a pet
- `GET /store/order/{orderId}`: Find purchase order by ID
- `DELETE /store/order/{orderId}`: Delete purchase order by ID
- `POST /user`: Create user
- `POST /user/createWithList`: Creates list of users with given input array
- `GET /user/login`: Logs user into the system
- `GET /user/logout`: Logs out current logged in user session
- `GET /user/{username}`: Get user by user name
- `PUT /user/{username}`: Update user
- `DELETE /user/{username}`: Delete user