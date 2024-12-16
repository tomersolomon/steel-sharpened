# __init__.py
__version__ = "0.1.0"

# API Client
class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def call_api(self, path, method, params=None):
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}  # Adjust as needed

        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=params, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=params, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Handle response based on content type (add more as needed)
        if response.headers["Content-Type"] == "application/json":
            return response.json()
        else:
            return response.text()

# API Endpoints

class Addpet:
    def __init__(self, api_client):
        self.api_client = api_client

    def addPet(self, params=None):
        """
        Add a new pet to the store

        Add a new pet to the store
        """
        return self.api_client.call_api("/pet", "POST", params)


class Updatepet:
    def __init__(self, api_client):
        self.api_client = api_client

    def updatePet(self, params=None):
        """
        Update an existing pet

        Update an existing pet by Id
        """
        return self.api_client.call_api("/pet", "PUT", params)


class Findpetsbystatus:
    def __init__(self, api_client):
        self.api_client = api_client

    def findPetsByStatus(self, params=None):
        """
        Finds Pets by status

        Multiple status values can be provided with comma separated strings
        """
        return self.api_client.call_api("/pet/findByStatus", "GET", params)


class Findpetsbytags:
    def __init__(self, api_client):
        self.api_client = api_client

    def findPetsByTags(self, params=None):
        """
        Finds Pets by tags

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
        """
        return self.api_client.call_api("/pet/findByTags", "GET", params)


class Getpetbyid:
    def __init__(self, api_client):
        self.api_client = api_client

    def getPetById(self, params=None):
        """
        Find pet by ID

        Returns a single pet
        """
        return self.api_client.call_api("/pet/{petId}", "GET", params)


class Updatepetwithform:
    def __init__(self, api_client):
        self.api_client = api_client

    def updatePetWithForm(self, params=None):
        """
        Updates a pet in the store with form data

        """
        return self.api_client.call_api("/pet/{petId}", "POST", params)


class Deletepet:
    def __init__(self, api_client):
        self.api_client = api_client

    def deletePet(self, params=None):
        """
        Deletes a pet

        """
        return self.api_client.call_api("/pet/{petId}", "DELETE", params)


class Uploadfile:
    def __init__(self, api_client):
        self.api_client = api_client

    def uploadFile(self, params=None):
        """
        uploads an image

        """
        return self.api_client.call_api("/pet/{petId}/uploadImage", "POST", params)


class Getinventory:
    def __init__(self, api_client):
        self.api_client = api_client

    def getInventory(self, params=None):
        """
        Returns pet inventories by status

        Returns a map of status codes to quantities
        """
        return self.api_client.call_api("/store/inventory", "GET", params)


class Placeorder:
    def __init__(self, api_client):
        self.api_client = api_client

    def placeOrder(self, params=None):
        """
        Place an order for a pet

        Place a new order in the store
        """
        return self.api_client.call_api("/store/order", "POST", params)


class Getorderbyid:
    def __init__(self, api_client):
        self.api_client = api_client

    def getOrderById(self, params=None):
        """
        Find purchase order by ID

        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.
        """
        return self.api_client.call_api("/store/order/{orderId}", "GET", params)


class Deleteorder:
    def __init__(self, api_client):
        self.api_client = api_client

    def deleteOrder(self, params=None):
        """
        Delete purchase order by ID

        For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors
        """
        return self.api_client.call_api("/store/order/{orderId}", "DELETE", params)


class Createuser:
    def __init__(self, api_client):
        self.api_client = api_client

    def createUser(self, params=None):
        """
        Create user

        This can only be done by the logged in user.
        """
        return self.api_client.call_api("/user", "POST", params)


class Createuserswithlistinput:
    def __init__(self, api_client):
        self.api_client = api_client

    def createUsersWithListInput(self, params=None):
        """
        Creates list of users with given input array

        Creates list of users with given input array
        """
        return self.api_client.call_api("/user/createWithList", "POST", params)


class Loginuser:
    def __init__(self, api_client):
        self.api_client = api_client

    def loginUser(self, params=None):
        """
        Logs user into the system

        """
        return self.api_client.call_api("/user/login", "GET", params)


class Logoutuser:
    def __init__(self, api_client):
        self.api_client = api_client

    def logoutUser(self, params=None):
        """
        Logs out current logged in user session

        """
        return self.api_client.call_api("/user/logout", "GET", params)


class Getuserbyname:
    def __init__(self, api_client):
        self.api_client = api_client

    def getUserByName(self, params=None):
        """
        Get user by user name

        """
        return self.api_client.call_api("/user/{username}", "GET", params)


class Updateuser:
    def __init__(self, api_client):
        self.api_client = api_client

    def updateUser(self, params=None):
        """
        Update user

        This can only be done by the logged in user.
        """
        return self.api_client.call_api("/user/{username}", "PUT", params)


class Deleteuser:
    def __init__(self, api_client):
        self.api_client = api_client

    def deleteUser(self, params=None):
        """
        Delete user

        This can only be done by the logged in user.
        """
        return self.api_client.call_api("/user/{username}", "DELETE", params)

