CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    city VARCHAR(100) NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    aadhar_number VARCHAR(20) UNIQUE NOT NULL
);


CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    customer_id INT NOT NULL,
    customer_phone_number VARCHAR(20) NOT NULL,
    account_type ENUM('Savings', 'Current') NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    date_opened VARCHAR(20) NOT NULL,
    status ENUM('Active', 'Inactive', 'Closed') NOT NULL,

    -- Savings Account Specific Fields
    interest_rate DECIMAL(5,2) DEFAULT NULL,
    minimum_balance DECIMAL(15,2) DEFAULT NULL,

    -- Current Account Specific Fields
    overdraft_limit DECIMAL(15,2) DEFAULT NULL,
    monthly_fee DECIMAL(15,2) DEFAULT NULL,

    -- Foreign Key Constraint
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);