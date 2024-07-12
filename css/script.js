document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Perform simple validation
    if(username === '' || password === '') {
        alert('Please fill in both fields');
        return;
    }
    
    // Normally, here you would send a request to your server to authenticate the user
    // For demonstration, we'll just log the credentials to the console
    console.log(`Username: ${username}, Password: ${password}`);
    
    // Simulate successful login
    alert('Login successful');
    // Redirect to the inventory management dashboard (replace 'dashboard.html' with the actual path)
    window.location.href = 'https://demo-git.partkeepr.org/';
});
