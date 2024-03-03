const express = require('express');
const app = express();

let viewerCount = 0;

// Middleware to increment the viewer count
app.use('/incrementCount', (req, res, next) => {
  viewerCount++;
  next();
});

// Route to send the viewer count
app.get('/getCount', (req, res) => {
  res.json({ count: viewerCount });
});

// Serve the HTML file
app.use(express.static('public'));

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});