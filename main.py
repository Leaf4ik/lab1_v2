import parsing
import toolsParsing as tools

if __name__ == "__main__":
    parsing.parsing(tools.urlKafedra, tools.domTegKafedra, tools.fileKafedra)
    parsing.parsing(tools.urlFakultets, tools.domTegFakultets, tools.fileFakultets)
    parsing.parsing(tools.urlStaff, tools.domTegStaff, tools.fileStaff)