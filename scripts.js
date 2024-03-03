// JavaScript code for your blog website (if any)
// You can add your dynamic behavior here
const express = require('express');
const cron = require('node-cron');
const fs = require('fs');
const app = express();

let viewerCount = 0;

// Load previous count from file on server start
fs.readFile('count.txt', 'utf8', (err, data) => {
  if (!err && data) {
    viewerCount = parseInt(data);
  }
});

// Middleware to increment the viewer count
app.use((req, res, next) => {
  viewerCount++;
  next();
});

// Route to display the viewer count
app.get('/', (req, res) => {
  res.send(`Number of viewers today: ${viewerCount}`);
});

// Schedule a task to reset the count at 00:00 each day
cron.schedule('0 0 * * *', () => {
  fs.writeFile('count.txt', viewerCount.toString(), 'utf8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Viewer count has been reset and saved.');
    }
  });
  viewerCount = 0;
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});