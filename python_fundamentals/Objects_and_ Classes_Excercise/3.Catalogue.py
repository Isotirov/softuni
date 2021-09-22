class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.sorted_list = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        self.sorted_list = [el for el in self.products if el[0] == first_letter]
        return self.sorted_list

    def __repr__(self):
        self.products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(self.products)
        return result
