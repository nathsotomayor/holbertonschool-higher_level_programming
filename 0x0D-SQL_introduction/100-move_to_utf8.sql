-- Converts database and table to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table COLLATE utf8mb4_general_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;