class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = {"com", "bg", "org", "net"}

email = input()

while not email == "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    email_parts = email.split("@")
    name = email_parts[0]
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name = email_parts[-1]
    domain = domain_name.split(".")[-1]
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
