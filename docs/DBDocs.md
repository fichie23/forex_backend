# Database Documentation

## Short Description

In this API, i only generate two models or tables to meet all the requirements. 
- Table `forex_currency` 
Where the currency stored, there are two main fields in this table,
  - `base` as a base currency which will be converted in the forex
  - `target` as a target currency which is a result of the base currency convert/exchange using certain rate. And this two fields will be used as foreign key in the second table with one-to-many relationship
  
- Table `forex_exchangeratehistory`
This table used for track daily exchange rate for certain currency (data from the first table)
There are three main fields here
  - date, when the exchange rate submitted
  - rate, a value of exchange from certain currency to be converted into target currency, this rate will stored daily as well
  - currency, a combination base - target currency which used here as foreign key to stored its daily exchange rate

### SQL Script
This sql script unnecessarily to be run manually since i used Django ORM to generate or mapping from models into table automatically
```
CREATE TABLE `forex_currency` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`base`	varchar ( 3 ) NOT NULL,
	`target`	varchar ( 3 ) NOT NULL
);


CREATE TABLE `forex_exchangeratehistory` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	date NOT NULL,
	`rate`	real NOT NULL,
	`currency_id`	integer NOT NULL,
	FOREIGN KEY(`currency_id`) REFERENCES `forex_currency`(`id`)
);
```
