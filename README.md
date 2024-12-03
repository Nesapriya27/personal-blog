# Personal blog

This is a personal blog project created using HTML, CSS, and JavaScript. The blog allows users to view, create, and manage blog posts. The project was set up and deployed step-by-step, starting from initializing the project to uploading it to GitHub.

## Features
- User authentication (Login/Sign up)
- Blog post creation, editing, and management
- Categories for organizing posts
- Search functionality
- Responsive design

## Steps Taken

 1. **Project Setup**
   - Created a folder for the project named `personal-blog` on the local machine.
   - Developed the frontend of the blog using HTML, CSS, and JavaScript.
   - Ensured the blog was responsive and user-friendly across different devices.

 2. **Version Control with Git**
   - Initialized a Git repository in the `personal-blog` folder.
   - Added all project files to the repository using `git add .`.
   - Committed the initial project files with a message `git commit -m "Initial commit"`.
   
3. **Repository Creation on GitHub**
   - Created a repository on GitHub named `personal-blog` to host the project.
   - Added the remote GitHub repository URL using `git remote add origin https://github.com/Nesapriya27/personal-blog.git`.
   - Pushed the local repository to GitHub using `git push -u origin main`.

4. **Fixing Authentication Issues**
   - Configured Git with the correct username and email for commits using:
     ```bash
     git config --global user.name "Nesapriya27"
     git config --global user.email "priyanesan27@gmail..com"
     ```

 5. **Resolving Push Issues**
   - Encountered a push rejection error because the GitHub repository had existing files (like a README).
   - Pulled the changes from the remote repository using:
     ```bash
     git pull origin main --rebase
     ```
   - Rebased the local branch to integrate the changes from GitHub.
   - Added the changes and committed the updates.

 6. **Final Push to GitHub**
   - After resolving conflicts and completing the rebase, added the changes (`git add .`), and pushed the changes to GitHub using `git push origin main`.

 7. **Deployment**
   - Successfully uploaded the project files to GitHub and the blog is now visible in the repository.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nesapriya27/personal-blog.git
   ```

2. Navigate to the project directory:
   ```bash
   cd personal-blog
   ```

3. Install necessary dependencies (if applicable):
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm start
   ```

   Open your browser and go to `http://localhost:3000` to view the blog.

## Usage

Once the app is running, you can:
- Register a new account or log in.
- Create, edit, and delete blog posts.
- Use the search bar to search through posts.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

