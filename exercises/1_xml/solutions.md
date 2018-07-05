# Assignment 1: Data Modeling

## Exercise 1

See `purchaseOrder.xml`.

Das XML-Dokument erfüllt die Anforderungen:

a) Es ist kompatibel mit XML-1.0-Parsern, da diese erwarten, dass die Version 1.0 oder nicht angegeben ist.
Es ist auch kompatibel mit XML-1.1-Parsern, da diese erwarten, dass die Version angegeben ist und selbst kompatibel zu XML-1.0 sein müssen.

b) Um ein Element einem Namensraum zuzuordnen, kann man entweder einen Standardnamensraum angeben,

    <purchaseOrder
        xmlns="http://www.altova.com/IPO"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        orderDate="1999-12-01">

        <shipTo export-code="1" xsi:type="ipo:EU-Address">

        <!-- ... -->

oder dem Element ein Präfix voranstellen, das zuvor als Namensraum deklariert wurde:

    <ipo:purchaseOrder
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:ipo="http://www.altova.com/IPO"
        orderDate="1999-12-01">

        <ipo:shipTo export-code="1" xsi:type="ipo:EU-Address">

        <!-- ... -->

c) Die Daten orderDate, type, export-code und partNum werden als Attribute repräsentiert.

d) Die Attribute orderDate, export-code und partNum haben kein Präfix. Da Attribute nur durch ein Präfix einem Namensraum zugeordnet werden können, sind sie nicht namensraumeingeschränkt und liegen damit im Null-Namensraum.

e) Das Attribut type wird mit dem Präfix `xsi` verwendet, das als der Namensraum http://www.w3.org/2001/XMLSchema-instance deklariert ist. Dadurch liegt es in diesem Namensraum.

Bonus questions:

a) Um auch die Attribute orderDate, export-code und partNum dem gleichen Namensraum wie die Elemente zuzuordnen, müssen sie mit einem Präfix verwendet werden.

    <ipo:purchaseOrder
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:ipo="http://www.altova.com/IPO"
        ipo:orderDate="1999-12-01">

        <ipo:shipTo ipo:export-code="1" xsi:type="ipo:EU-Address">

        <!-- ... -->

b) Nein, das Dokument ist nicht wohlgeformt bezüglich XML 1.0 und 1.1.
Ein XML-Dokument ohne Angabe der Version oder mit Version 1.0 ist nicht wohlgeformt bezüglich XML 1.1 und ein XML-Dokument mit Version 1.1 ist nicht wohlgeformt bezüglich XML 1.0.

c) Die klassische Betrachtungsweise geht davon aus, dass eine URI entweder ein URL oder ein URN ist.
Sowohl für URLs als auch für URNs gibt es dabei verschiedene Schemata, deren Verwendung durch ein Präfix angegeben wird, wie zum Beispiel http oder isbn.
Die aktuelle Betrachtungsweise nimmt keine klare Unterteilung von URIs mehr
vor.
Schemata werden nur noch für URIs verwendet und als Namensräume bezeichnet.
URNs mit dem Präfix urn sind ein möglicher Namensraum.
URLs werden nur noch als informelle Bezeichnung für solche Ressourcen verwendet,
deren Namensraum ihre primäre Zugriffsmethode angibt.

## Exercise 2

See `book.dtd`.
