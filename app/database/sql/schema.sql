CREATE TABLE incidents (

    incident_id TEXT PRIMARY KEY,

    title TEXT,

    category TEXT,

    priority TEXT,

    status TEXT,

    root_cause TEXT,

    resolution TEXT,

    created_at TEXT

);

CREATE TABLE servers(

    server_id TEXT PRIMARY KEY,

    hostname TEXT,

    region TEXT,

    service TEXT,

    status TEXT,

    owner TEXT

);

CREATE TABLE applications(

    app_id TEXT PRIMARY KEY,

    application_name TEXT,

    server_id TEXT,

    environment TEXT,

    owner TEXT,

    FOREIGN KEY(server_id)
    REFERENCES servers(server_id)
);