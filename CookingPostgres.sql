DROP TABLE IF EXISTS liquid;
CREATE TABLE liquid (
id SERIAL NOT NULL, unit VARCHAR(255) NOT NULL, ml DECIMAL(6,2) NOT NULL, PRIMARY KEY (id)
);
INSERT INTO liquid (unit, ml)
VALUES ('Teaspoons', 5);
INSERT INTO liquid (unit, ml)
VALUES ('Dessertspoons', 10);
INSERT INTO liquid (unit, ml)
VALUES ('Tablespoons', 15);
INSERT INTO liquid (unit, ml)
VALUES ('Milliliters', 1);
INSERT INTO liquid (unit, ml)
VALUES ('Liters', 1000);
INSERT INTO liquid (unit, ml)
VALUES ('Grams', 1);
INSERT INTO liquid (unit, ml)
VALUES ('US Cups', 240);
INSERT INTO liquid (unit, ml)
VALUES ('US Fluid Ounces', 30);
INSERT INTO liquid (unit, ml)
VALUES ('US Pints', 480);
INSERT INTO liquid (unit, ml)
VALUES ('US Quarts', 960);
INSERT INTO liquid (unit, ml)
VALUES ('US Gallons', 3840);

DROP TABLE IF EXISTS flour;
CREATE TABLE flour (
id SERIAL NOT NULL, unit VARCHAR(255) NOT NULL, g DECIMAL(6,2) NOT NULL, PRIMARY KEY (id)
);
INSERT INTO flour (unit, g)
VALUES ('Teaspoons', 2.65);
INSERT INTO flour (unit, g)
VALUES ('Dessertspoons', 5.30);
INSERT INTO flour (unit, g)
VALUES ('Tablespoons', 7.95);
INSERT INTO flour (unit, g)
VALUES ('US Cups', 127.2);
INSERT INTO flour (unit, g)
VALUES ('Grams', 1);
INSERT INTO flour (unit, g)
VALUES ('Kilograms', 1000);
INSERT INTO flour (unit, g)
VALUES ('Ounces', 28);
INSERT INTO flour (unit, g)
VALUES ('Pounds', 448);

DROP TABLE IF EXISTS butter;
CREATE TABLE butter (
id SERIAL NOT NULL, unit VARCHAR(255) NOT NULL, g DECIMAL(6,2) NOT NULL, PRIMARY KEY (id)
);
INSERT INTO butter (unit, g)
VALUES ('Teaspoons', 4.8);
INSERT INTO butter (unit, g)
VALUES ('Dessertspoons', 9.6);
INSERT INTO butter (unit, g)
VALUES ('Tablespoons', 14.4);
INSERT INTO butter (unit, g)
VALUES ('US Cups', 230.4);
INSERT INTO butter (unit, g)
VALUES ('Grams', 1);
INSERT INTO butter (unit, g)
VALUES ('Kilograms', 1000);
INSERT INTO butter (unit, g)
VALUES ('Ounces', 28);
INSERT INTO butter (unit, g)
VALUES ('Pounds', 448);

DROP TABLE IF EXISTS temp;
CREATE TABLE temp (
id SERIAL NOT NULL, unit VARCHAR(255) NOT NULL, c DECIMAL(6,2) NOT NULL, PRIMARY KEY (id)
);
INSERT INTO temp (unit, c)
VALUES ('Celsius', 1);
INSERT INTO temp (unit, c)
VALUES ('Fahrenheit', 1.8);

CREATE UNIQUE INDEX liquid_index ON liquid (unit);
CREATE UNIQUE INDEX flour_index ON flour (unit);
CREATE UNIQUE INDEX butter_index ON butter (unit);
CREATE UNIQUE INDEX temp_index ON temp (unit);