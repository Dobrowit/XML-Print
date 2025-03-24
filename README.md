# XML-Print
Visualizes an XML file

XSLT is used for visualization.

Additionally, validation is performed if an XSD file is available.

---

Apka zamienia plik XML na HTML i otwiera w domyślnej przeglądarce WWW plik wynikowy. Do wizualizacji potrzebny jest plik XSLT. Przy okazji jeśli dostępny jest plik XSD przeprowadzana jest walidacja dokumentu.

Narzędzie przydatne w urzędach jeśli otrzyma się korespondencję w formacie XML i nie wiadomo co z tym zrobić. Do wizualizacji niezbędny jest schemat XSLT czyli trzeba mieć przynajmniej dwa pliki lub w nagłówku dokumentu XML musi być podany adres schematu.

Do działania niezbędny jest intermpreter Python i biblioteka lxml.

Interpreter można pobrać ze strony ```https://www.python.org/```, natomiast bibliotekę zainstalować można globalnie za pomocą polecenia:

```pip install lxml```
