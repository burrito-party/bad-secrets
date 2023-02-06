from .config import LOGIN_URLS, PWD_RULE_TYPE

def main():
    salt = "7d78c211b3ce9ff86d50217b49c42cf9"

    if salt+PWD_RULE_TYPE["Customer"]["idp"]["PW"] == "WHAT":
        print("you get the idea...")

    print("Done... Thank you." + LOGIN_URLS["DefNotRealAPI"])


if __name__ == "__main__":
    main()
