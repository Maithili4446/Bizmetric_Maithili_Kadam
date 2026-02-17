
import pyodbc



class Hotel:


    def __init__(self, server, database):

        connection_string = (

            "DRIVER={ODBC Driver 17 for SQL Server};"

            f"SERVER={server};"

            f"DATABASE={database};"

            "Trusted_Connection=yes;"

            "TrustServerCertificate=yes;"

        )


        self.conn = pyodbc.connect(connection_string)

        self.cursor = self.conn.cursor()

        self.menu = self.load_menu()

        self.order = {}



    def load_menu(self):

        self.cursor.execute("select item, price from dbo.Menu")

        return {row[0]: row[1] for row in self.cursor.fetchall()}



    def display_menu(self):

        print("\n------ MENU ------")

        for item, price in self.menu.items():

            print(f"{item:<15}{price}")



    def take_order(self):

        while True:

            item = input("\nEnter item name: ").lower()

            if item in self.menu:

                qty = int(input("Enter quantity: "))

                self.order[item] = self.order.get(item, 0) + qty

            else:

                print("Item not available")



            choice = input("Add more items? (yes/no): ").lower()

            if choice != "yes":

                break



    def generate_bill(self):

        print("\n--------- BILL ---------")

        total = 0


