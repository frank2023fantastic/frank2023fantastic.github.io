<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $author = $_POST['author'];
    $title = $_POST['title'];
    $content = $_POST['content'];
    
    $post = "Author: " . $author . "\nTitle: " . $title . "\nContent: " . $content . "\n\n";

    $file = 'blog_posts.txt';
    file_put_contents($file, $post, FILE_APPEND);
    
    echo "Blog post submitted successfully!";
} else {
    echo "Invalid request!";
}
?>