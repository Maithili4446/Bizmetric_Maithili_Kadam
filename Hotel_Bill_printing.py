import pyodbc
from datetime import datetime
import os   # <-- added for folder handling

class Hotel:

    def __init__(self):

        server = r"GANESH\SQLEXPRESS"
        database = "HotelManagementSystem"

        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()
        self.menu = self.get_menu()
        self.order = {}

        # --------- Create Folder bill_generator ----------
        self.folder = "bill_generator"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        # --------- Generate Menu Card File ----------
        self.generate_menu_card()

    # ---------------- MENU FROM DATABASE ----------------
    def get_menu(self):
        self.cursor.execute("select item,price from Menu")
        return dict(self.cursor.fetchall())

    # ---------------- SHOW MENU ----------------
    def show_menu(self):
        print("---- MENU ----")
        for item, price in self.menu.items():
            print(f"{item:<15}{price}")

    # ---------------- MENU CARD FILE ----------------
    def generate_menu_card(self):
        filepath = os.path.join(self.folder, "menucard.txt")

        with open(filepath, "w") as f:
            f.write("----------- HOTEL MENU CARD -----------\n")
            for item, price in self.menu.items():
                f.write(f"{item:<15}{price}\n")

    # ---------------- TAKE ORDER ----------------
    def take_order(self):
        while True:
            item = input("Enter item name: ").lower()
            if item in self.menu:
                qty = int(input("Enter quantity: "))
                self.order[item] = self.order.get(item, 0) + qty
            else:
                print("Item not available")

            ch = input("Do you want to order more? ").lower()
            if ch != "yes":
                break

    # ---------------- GENERATE BILL ----------------
    def generate_bill(self):

        print("\n----------- BILL -----------")
        total = 0
        lines = []

        lines.append("----------- HOTEL BILL -----------")
        lines.append(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        lines.append("----------------------------------")

        for item, qty in self.order.items():
            amount = self.menu[item] * qty
            total += amount

            print(f"{item:<15}{qty:<5}{amount}")
            lines.append(f"{item:<15}{qty:<5}{amount}")

            self.cursor.execute(
                "insert into Bills(item,quantity,amount) values(?,?,?)",
                item, qty, amount
            )

        self.conn.commit()

        print("----------------------------------")
        print(f"Total Amount = {total}")

        lines.append("----------------------------------")
        lines.append(f"Total Amount = {total}")
        lines.append("----------------------------------")

        # -------- Save bill inside bill_generator folder --------
        filename = datetime.now().strftime("bill_%Y%m%d_%H%M%S.txt")
        filepath = os.path.join(self.folder, filename)

        with open(filepath, "w") as f:
            for line in lines:
                f.write(line + "\n")

        print(f"\nBill saved in folder → {self.folder}")

    # ---------------- CLOSE CONNECTION ----------------
    def close(self):
        self.conn.close()


# ---------------- RUN PROGRAM ----------------
h = Hotel()
h.show_menu()
h.take_order()
h.generate_bill()
h.close()




