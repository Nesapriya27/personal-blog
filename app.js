// Array to store blog posts (in-memory for now)
let posts = [
    {
        title: "My First Blog Post",
        content: "This is the content of my first blog post. Here, I'll talk about various topics that interest me, such as web development, coding, and personal experiences. Stay tuned for more updates!"
    },
    {
        title: "My Second Blog Post",
        content: "In this post, I will share insights on how to learn web development, my journey, and tips for beginners. It's an exciting world with endless possibilities!"
    }
];

// Function to display posts
function displayPosts() {
    const postList = document.getElementById("post-list");
    postList.innerHTML = ''; // Clear current posts

    posts.forEach(post => {
        const postElement = document.createElement("div");
        postElement.classList.add("post");

        const postTitle = document.createElement("h2");
        postTitle.textContent = post.title;

        const postContent = document.createElement("p");
        postContent.textContent = post.content;

        postElement.appendChild(postTitle);
        postElement.appendChild(postContent);
        postList.appendChild(postElement);
    });
}

// Handle form submission to add a new post
document.getElementById("postForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page reload on form submission

    const title = document.getElementById("postTitle").value;
    const content = document.getElementById("postContent").value;

    // Add the new post to the posts array
    posts.push({
        title: title,
        content: content
    });

    // Clear form fields
    document.getElementById("postTitle").value = '';
    document.getElementById("postContent").value = '';

    // Display the updated posts
    displayPosts();

    // Show a response message
    const responseMessage = document.getElementById("responseMessage");
    responseMessage.textContent = "Your post has been submitted successfully!";
    responseMessage.classList.remove("hidden");

    // Hide the response message after 3 seconds
    setTimeout(function() {
        responseMessage.classList.add("hidden");
    }, 3000);
});

// Initial call to display posts
displayPosts();
