CREATE DATABASE HotelManagementSystem;
USE HotelManagementSystem;

CREATE TABLE Menu (
    item VARCHAR(50) PRIMARY KEY,
    price INT
);

INSERT INTO Menu (item, price) VALUES
('pizza', 250),
('burger', 120),
('pasta', 180),
('sandwich', 90),
('coffee', 80),
('tea', 50),
('fries', 100);

CREATE TABLE Bills (
    bill_id INT IDENTITY(1,1) PRIMARY KEY,
    item VARCHAR(50),
    quantity INT,
    amount INT,
    bill_date DATETIME DEFAULT GETDATE()
);

SELECT * FROM Menu;
SELECT * FROM Bills;