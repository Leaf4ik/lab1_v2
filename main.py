import parsing

if __name__ == "__main__":
    urlKafedra = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"
    domTegKafedra = "ul"
    fileKafedra = "kafedraInfo.txt"
    parsing.parsing(urlKafedra, domTegKafedra, fileKafedra)
