import parsing
urlKafedra = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"
domTegKafedra = "ul"
fileKafedra = "kafedraInfo.txt"

urlFakultets = "https://omgtu.ru/general_information/faculties/"
domTegFakultets = "li"
fileFakultets = "FakultetsInfo.txt"

urlStaff = "https://omgtu.ru/ecab/persons/index.php?b=10"
domTegStaff = "a"
fileStaff = "staffInfo.txt"


if __name__ == "__main__":
    parsing.Parsing(urlKafedra, domTegKafedra, fileKafedra)
    parsing.Parsing(urlFakultets, domTegFakultets, fileFakultets)
    parsing.Parsing(urlStaff, domTegStaff, fileStaff)