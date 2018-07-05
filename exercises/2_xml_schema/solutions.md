# Assignment 2: XML Schema

## Exercise 1

See `purchaseOrder.xsd` and `address.xsd`.

Um ein XML-Dokument mit einem Schema zu verknüpfen,
verwendet man das Attribut `xsi:schemaLocation` im Wurzelelement des Dokuments:

    <?xml version="1.0" ?>
    <ipo:purchaseOrder
        xmlns:ipo="http://www.altova.com/IPO"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema−instance"
        xsi:schemaLocation="http://www.example.org/ipo.xsd"
        orderDate="1999−12−01">

## Exercise 2

See `book.xsd`.
