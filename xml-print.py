#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog, messagebox
from lxml import etree
import webbrowser
import os
import re

# Funkcja do wyboru pliku
def select_file(file_type, extension):
    file_path = filedialog.askopenfilename(filetypes=[(file_type, extension)])
    return file_path if file_path else None

# Tworzenie okna dialogowego
root = tk.Tk()
root.withdraw()  # Ukrycie głównego okna

xml_file = select_file("XML files", "*.xml")
if xml_file:
    xsd_file = os.path.splitext(xml_file)[0] + ".xsd"
    if not os.path.exists(xsd_file):
        xsd_file = select_file("XSD files", "*.xsd")

    if xsd_file:
        xml_tree = etree.parse(xml_file)
        xsd_tree = etree.parse(xsd_file)
        xmlschema = etree.XMLSchema(xsd_tree)

        if xmlschema.validate(xml_tree):
            messagebox.showinfo("Walidacja XML", "Plik XML jest poprawny względem XSD.")
        else:
            messagebox.showerror("Błąd walidacji", f"Plik XML nie przeszedł walidacji!\n{xmlschema.error_log}")
            exit()

    xslt_file = os.path.splitext(xml_file)[0] + ".xslt"
    if not os.path.exists(xslt_file):
        xslt_file = select_file("XSLT files", "*.xslt")

if xml_file and xslt_file:
    xml_tree = etree.parse(xml_file)
    xslt_tree = etree.parse(xslt_file)
    transform = etree.XSLT(xslt_tree)
    result_tree = transform(xml_tree)

    output_file = os.path.splitext(xml_file)[0] + ".html"
    if os.path.exists(output_file):
        base_name, ext = os.path.splitext(output_file)
        counter = 1
        while os.path.exists(f"{base_name}({counter}){ext}"):
            counter += 1
        new_output_file = f"{base_name}({counter}){ext}"
        choice = messagebox.askyesno("Plik istnieje", f"Plik '{os.path.basename(output_file)}' już istnieje. Czy chcesz go nadpisać? Jeśli nie, zostanie zapisany jako '{os.path.basename(new_output_file)}'.")
        if not choice:
            output_file = new_output_file
    
    with open(output_file, "wb") as f:
        f.write(etree.tostring(result_tree, pretty_print=True))
    print(f"Plik zapisany jako: {output_file}")
    webbrowser.open(output_file)  # Otwórz plik w domyślnej przeglądarce
else:
    print("Nie wybrano plików.")
