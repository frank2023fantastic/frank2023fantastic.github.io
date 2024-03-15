const express = require('express');
const markdownIt = require('markdown-it');
const fs = require('fs');

const app = express();
const port = 9999;

const md = new markdownIt();

app.get('/', (req, res) => {
  // Read the Markdown file
  fs.readFile('text.md', 'utf8', (err, data) => {
    if (err) {
      res.send('Error reading file');
    } else {
      // Convert Markdown to HTML
      const html = md.render(data);
      res.send(html);
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});