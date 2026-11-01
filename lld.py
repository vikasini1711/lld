class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def login(self):
        print(self.name, "logged in")


class Company:
    def __init__(self, company_id, name):
        self.company_id = company_id
        self.name = name

    def display(self):
        print("Company:", self.name)


class Contact:
    def __init__(self, contact_id, name, email):
        self.contact_id = contact_id
        self.name = name
        self.email = email

    def display(self):
        print("Contact:", self.name, "|", self.email)


class Deal:
    def __init__(self, deal_id, title, value):
        self.deal_id = deal_id
        self.title = title
        self.value = value
        self.status = "OPEN"

    def update_status(self, status):
        self.status = status

    def display(self):
        print(self.title, "|", self.value, "|", self.status)


class CRMService:
    def __init__(self):
        self.companies = []
        self.contacts = []
        self.deals = []

    def add_company(self, company):
        self.companies.append(company)

    def add_contact(self, contact):
        self.contacts.append(contact)

    def add_deal(self, deal):
        self.deals.append(deal)

    def display_deals(self):
        for deal in self.deals:
            deal.display()


class AIAssistant:
    def process_prompt(self, prompt):
        print("AI received:", prompt)
        print("Please specify the CRM action.")


# Main program
user = User(1, "priya", "ADMIN")
crm = CRMService()

user.login()

company = Company(101, "ABC Technologies")
contact = Contact(201, "Priya", "priya@example.com")
deal = Deal(301, "Software Project", 150000)

crm.add_company(company)
crm.add_contact(contact)
crm.add_deal(deal)

company.display()
contact.display()
crm.display_deals()

deal.update_status("CLOSED")

print("After updating deal:")
deal.display()

ai = AIAssistant()
ai.process_prompt("Show me all deals")
