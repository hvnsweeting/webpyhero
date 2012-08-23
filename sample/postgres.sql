DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id serial primary key,
    task text,
    startdate text,
    enddate text,
    priority integer
);
