SELECT Customers.CustomerID, Customers.CompanyName,
Customers.City,
Customers.Country,
Orders.OrderID,
Orders.OrderDate,
Products.ProductName,
[Order Details].Quantity,
[Order Details].UnitPrice,
[Order Details].Quantity * [Order Details].UnitPrice AS TotalPrice

FROM Customers
	INNER JOIN Orders ON Orders.CustomerID = Customers.CustomerID
	INNER JOIN [Order Details] ON [Order Details].OrderID = Orders.OrderID
	INNER JOIN Products ON Products.ProductID = [Order Details].ProductID