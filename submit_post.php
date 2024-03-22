<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $author = $_POST['author'];
    $title = $_POST['title'];
    $content = $_POST['content'];

    // Create a new blog post entry
    $post = "Author: " . $author . "\nTitle: " . $title . "\nContent: " . $content . "\n\n";

    // Save the blog post to a text file
    $file = 'blog_posts.txt';
    file_put_contents($file, $post, FILE_APPEND | LOCK_EX);

    echo "Blog post submitted successfully!";
} else {
    echo "Invalid request!";
}
?>