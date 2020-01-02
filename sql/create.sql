CREATE TABLE ubsuser (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    tnumber VARCHAR NOT NULL
);


CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    status VARCHAR NOT NULL,
    version VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    ubsuser_id INTEGER REFERENCES ubsuser
);

INSERT INTO ubsuser (name, tnumber) VALUES ('Alice', 't12345');
INSERT INTO ubsuser (name, tnumber) VALUES ('Bob', 't11111');
INSERT INTO ubsuser (name, tnumber) VALUES ('Charlie', 't111444');

INSERT INTO tickets (status, version, description, ubsuser_id) VALUES ('Open', '1.0', 'New Inc Ticket', 1);
INSERT INTO tickets (status, version, description, ubsuser_id) VALUES ('Open', '1.0', '2nd Inc Ticket', 3);

select * from tickets join ubsuser on tickets.ubsuser_id = ubsuser.id;
