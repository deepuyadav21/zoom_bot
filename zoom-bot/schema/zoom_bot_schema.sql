
-- Create the main database
CREATE DATABASE IF NOT EXISTS zoom_bot;
USE zoom_bot;

-- Table to store meeting details
CREATE TABLE IF NOT EXISTS meetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    meeting_id VARCHAR(100) NOT NULL,
    password VARCHAR(100),
    participant_name VARCHAR(100),
    datetime DATETIME NOT NULL,
    mic BOOLEAN DEFAULT TRUE,
    camera BOOLEAN DEFAULT TRUE
);

-- Table to log join attempts by the bot
CREATE TABLE IF NOT EXISTS join_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    meeting_id INT,
    status VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    message TEXT,
    FOREIGN KEY (meeting_id) REFERENCES meetings(id) ON DELETE CASCADE
);
