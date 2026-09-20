-- MySQL-first logical schema. The local SQLite engine uses the same explicit types.
CREATE TABLE schema_migration (
  version INT NOT NULL PRIMARY KEY,
  applied_at DATETIME(3) NOT NULL
);

CREATE TABLE execution (
  execution_id CHAR(36) NOT NULL PRIMARY KEY,
  source_platform VARCHAR(64) NOT NULL,
  source_execution_id VARCHAR(255) NOT NULL,
  assistant_id VARCHAR(128) NOT NULL,
  assistant_name VARCHAR(255) NOT NULL,
  status VARCHAR(32) NOT NULL,
  collection_mode VARCHAR(32) NOT NULL,
  coverage VARCHAR(16) NOT NULL,
  trace_integrity VARCHAR(16) NOT NULL,
  started_at DATETIME(3) NOT NULL,
  ended_at DATETIME(3),
  UNIQUE(source_platform, source_execution_id)
);
