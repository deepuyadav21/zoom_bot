
USE zoom_bot;

-- Add new columns for extended metadata
ALTER TABLE meetings
ADD COLUMN notes TEXT AFTER participant_name,
ADD COLUMN join_attempts INT DEFAULT 0 AFTER camera,
ADD COLUMN join_source VARCHAR(20) DEFAULT 'manual' AFTER join_attempts,
ADD COLUMN scheduled_time DATETIME AFTER datetime;
