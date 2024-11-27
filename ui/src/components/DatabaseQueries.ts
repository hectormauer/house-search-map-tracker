import sqlite3 from 'sqlite3'

const dbFilePath = './house-db.sqlite'; // Path where the DB file will be stored

export class DatabaseQueries {
    private db: sqlite3.Database;
  
    constructor() {
      this.db = new sqlite3.Database(dbFilePath, (err) => {
        if (err) {
          console.error('Error opening database:', err.message);
        } else {
          console.log('Connected to the SQLite database.');
          this.createTable();
        }
      });
    }
  
    // Create a table if it does not exist
    private createTable() {
      const createTableQuery = `
        CREATE TABLE IF NOT EXISTS houses (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          price REAL NOT NULL,
          url TEXT NOT NULL
        );
      `;
      this.db.run(createTableQuery, (err) => {
        if (err) {
          console.error('Error creating table:', err.message);
        } else {
          console.log('Houses table created or already exists.');
        }
      });
    }
  
    // Insert a new house entry
    public insertHouse(name: string, price: number, url: string): Promise<void> {
      return new Promise((resolve, reject) => {
        const query = `INSERT INTO houses (name, price, url) VALUES (?, ?, ?)`;
        this.db.run(query, [name, price, url], function (err) {
          if (err) {
            console.error('Error inserting house:', err.message);
            reject(err);
          } else {
            console.log(`Inserted house with id: ${this.lastID}`);
            resolve();
          }
        });
      });
    }
  
    // Fetch all houses
    public getHouses(): Promise<any[]> {
      return new Promise((resolve, reject) => {
        const query = `SELECT * FROM houses`;
        this.db.all(query, [], (err, rows) => {
          if (err) {
            console.error('Error fetching houses:', err.message);
            reject(err);
          } else {
            resolve(rows);
          }
        });
      });
    }
  
    // Close the database connection
    public close(): void {
      this.db.close((err) => {
        if (err) {
          console.error('Error closing database:', err.message);
        } else {
          console.log('Database connection closed.');
        }
      });
    }
  }