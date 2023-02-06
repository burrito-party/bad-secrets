LOGIN_URLS = {
    "DefNotRealAPI": "https://sch-def-not-real-api.com",
    "Customer": "https://no-way-this-is-customer-url.com",
}

PWD_RULE_TYPE = {
    "DefNotRealAPI": {
        "VERSION": "1.0.2",
        "idp": {
            "SHOPPER": "12345678",
            "USER": "testuser",
            "PW": "1q2w3e4r5t",
            "REDIRECT_REQUEST": "/api/idp/login",
        },
        "pass": {
            "SHOPPER": "98765432",
            "PASS_GUID": "b9d8b262-c122-4dd9-a6e4-0e50584b8b3e",
            "USER": "cust1@fake-not-real-ui.com",
            "PW": "qwertymydog0000",
            "REDIRECT_REQUEST": "users.somefakesitenotrealyes.com",
        }
    },
    "Customer": {
        "VERSION": "1.0.0",
        "idp": {
            "SHOPPER": "13579753",
            "USER": "cust_user",
            "PW": "EQpdFQ9KE!",
            "REDIRECT_REQUEST": "/api/idp/login",
            "SUCCESS_REDIRECT": "cust.notrealbutlooksprettypeace.com/?plid=33333"
        },
        "pass": {
            "SHOPPER": "24680864",
            "PASS_ID": "90f1b8d9-cb9f-4b92-8b79-210d3f4fc99e",
            "USER": "work@fake-cust-prod-joy.com",
            "PW": "GfpbDfPZCfpZDA3",
            "REDIRECT_REQUEST": "custs.somefakesitenotrealno.com",
        }
    }
}
