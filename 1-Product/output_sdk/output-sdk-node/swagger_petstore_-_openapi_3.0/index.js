// index.js

const axios = require('axios');

class ApiClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.apiKey = 'special-key'; // API key, replace with your authentication mechanism if needed
    }

    async callApi(path, method, params = {}) {
        const url = `${this.baseURL}${path}`;
        const headers = {
            'Content-Type': 'application/json',
            'api_key': this.apiKey, // Include API key in headers (adjust header name as needed)
        };

        try {
            let response;
            if (method === 'GET') {
                response = await axios.get(url, { params, headers });
            } else if (method === 'POST') {
                response = await axios.post(url, params, { headers });
            } else if (method === 'PUT') {
                response = await axios.put(url, params, { headers });
            } else if (method === 'DELETE') {
                response = await axios.delete(url, { headers });
            } else {
                throw new Error(`Unsupported HTTP method: ${method}`);
            }

            return response.data;
        } catch (error) {
            if (error.response) {
                throw new Error(`Request failed with status code ${error.response.status}`);
            } else if (error.request) {
                throw new Error('Request made but no response received');
            } else {
                throw new Error('Error setting up request');
            }
        }
    }
}


exports.Addpet = class Addpet {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async addPet(params = {}) {
        /**
         * Add a new pet to the store
         * Add a new pet to the store
         */
        return await this.apiClient.callApi("/pet", "POST", params);
    }
};

exports.Updatepet = class Updatepet {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async updatePet(params = {}) {
        /**
         * Update an existing pet
         * Update an existing pet by Id
         */
        return await this.apiClient.callApi("/pet", "PUT", params);
    }
};

exports.Findpetsbystatus = class Findpetsbystatus {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async findPetsByStatus(params = {}) {
        /**
         * Finds Pets by status
         * Multiple status values can be provided with comma separated strings
         */
        return await this.apiClient.callApi("/pet/findByStatus", "GET", params);
    }
};

exports.Findpetsbytags = class Findpetsbytags {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async findPetsByTags(params = {}) {
        /**
         * Finds Pets by tags
         * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
         */
        return await this.apiClient.callApi("/pet/findByTags", "GET", params);
    }
};

exports.Getpetbyid = class Getpetbyid {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async getPetById(params = {}) {
        /**
         * Find pet by ID
         * Returns a single pet
         */
        return await this.apiClient.callApi("/pet/{petId}", "GET", params);
    }
};

exports.Updatepetwithform = class Updatepetwithform {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async updatePetWithForm(params = {}) {
        /**
         * Updates a pet in the store with form data
         */
        return await this.apiClient.callApi("/pet/{petId}", "POST", params);
    }
};

exports.Deletepet = class Deletepet {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async deletePet(params = {}) {
        /**
         * Deletes a pet
         */
        return await this.apiClient.callApi("/pet/{petId}", "DELETE", params);
    }
};

exports.Uploadfile = class Uploadfile {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async uploadFile(params = {}) {
        /**
         * uploads an image
         */
        return await this.apiClient.callApi("/pet/{petId}/uploadImage", "POST", params);
    }
};

exports.Getinventory = class Getinventory {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async getInventory(params = {}) {
        /**
         * Returns pet inventories by status
         * Returns a map of status codes to quantities
         */
        return await this.apiClient.callApi("/store/inventory", "GET", params);
    }
};

exports.Placeorder = class Placeorder {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async placeOrder(params = {}) {
        /**
         * Place an order for a pet
         * Place a new order in the store
         */
        return await this.apiClient.callApi("/store/order", "POST", params);
    }
};

exports.Getorderbyid = class Getorderbyid {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async getOrderById(params = {}) {
        /**
         * Find purchase order by ID
         * For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.
         */
        return await this.apiClient.callApi("/store/order/{orderId}", "GET", params);
    }
};

exports.Deleteorder = class Deleteorder {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async deleteOrder(params = {}) {
        /**
         * Delete purchase order by ID
         * For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors
         */
        return await this.apiClient.callApi("/store/order/{orderId}", "DELETE", params);
    }
};

exports.Createuser = class Createuser {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async createUser(params = {}) {
        /**
         * Create user
         * This can only be done by the logged in user.
         */
        return await this.apiClient.callApi("/user", "POST", params);
    }
};

exports.Createuserswithlistinput = class Createuserswithlistinput {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async createUsersWithListInput(params = {}) {
        /**
         * Creates list of users with given input array
         * Creates list of users with given input array
         */
        return await this.apiClient.callApi("/user/createWithList", "POST", params);
    }
};

exports.Loginuser = class Loginuser {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async loginUser(params = {}) {
        /**
         * Logs user into the system
         */
        return await this.apiClient.callApi("/user/login", "GET", params);
    }
};

exports.Logoutuser = class Logoutuser {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async logoutUser(params = {}) {
        /**
         * Logs out current logged in user session
         */
        return await this.apiClient.callApi("/user/logout", "GET", params);
    }
};

exports.Getuserbyname = class Getuserbyname {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async getUserByName(params = {}) {
        /**
         * Get user by user name
         */
        return await this.apiClient.callApi("/user/{username}", "GET", params);
    }
};

exports.Updateuser = class Updateuser {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async updateUser(params = {}) {
        /**
         * Update user
         * This can only be done by the logged in user.
         */
        return await this.apiClient.callApi("/user/{username}", "PUT", params);
    }
};

exports.Deleteuser = class Deleteuser {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async deleteUser(params = {}) {
        /**
         * Delete user
         * This can only be done by the logged in user.
         */
        return await this.apiClient.callApi("/user/{username}", "DELETE", params);
    }
};
