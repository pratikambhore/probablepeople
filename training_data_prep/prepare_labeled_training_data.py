import xml.etree.ElementTree as xml
from xml.etree import ElementTree
import random

# Labeled output filepath
labeled_output_filename = 'labeled.xml'

root = xml.Element('NameCollection')

# Unlabeled input CSV filepath
unlabeled_fname_input_csv_filename = ''
unlabeled_lname_input_csv_filename = ''

# Generate labeled firstnames list
unlabeled_fname_file = open(unlabeled_fname_input_csv_filename, 'r')
unlabeled_fname_lines = unlabeled_fname_file.readlines()
unlabeled_fname_list = list(zip(unlabeled_fname_lines, ['GivenName']*len(unlabeled_fname_lines)))

# Generate labeled lastnames list
unlabeled_lname_file = open(unlabeled_lname_input_csv_filename, 'r')
unlabeled_lname_lines = unlabeled_lname_file.readlines()
unlabeled_lname_list = list(zip(unlabeled_lname_lines, ['Surname']*len(unlabeled_lname_lines)))

unlabeled_names_list = unlabeled_fname_list + unlabeled_lname_list
random.shuffle(unlabeled_names_list)

# Generate the XML Tree
for item in names_list:
    nameelement = xml.Element('Name')
    elmnt = xml.SubElement(nameelement, item[1])
    elmnt.text = item[0]
    root.append(nameelement)

tree = xml.ElementTree(root)

# Store the XML tree in output file
tree.write(labeled_output_filename)
