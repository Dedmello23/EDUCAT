const API_URL = "http://localhost:5000";

// User Sign-Up
async function handleSignUp() {
    const username = document.getElementById("signupUsername").value;
    const password = document.getElementById("signupPassword").value;

    const res = await fetch('${API_URL}/auth/signup', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    const data = await res.json();
    alert(data.message);
    if (res.ok) window.location.href = "index.html";
}

// User Login
async function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch('${API_URL}/auth/login', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    const data = await res.json();
    alert(data.message);
    if (res.ok) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", username);
        window.location.href = "subjects.html";
    }
}


async function submitAttendance() {
    const subject = document.getElementById("subject").value;
    const hours = parseFloat(document.getElementById("hours").value);
    const totalHours = parseFloat(document.getElementById("totalHours").value);
    function calculateAttendance() {
        
        const hoursConducted = parseFloat(document.getElementById('hours').value);
        const totalHours = parseFloat(document.getElementById('totalHours').value);
    
        
        fetch('http://127.0.0.1:5000/calculate_attendance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                hours_conducted: hoursConducted,
                total_hours: totalHours,
            }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);  
                } else {
                    
                    document.getElementById('attendance').value = data.attendance + '%';
                }
            })
            .catch(error => console.error('Error:', error));
    }
    const username = localStorage.getItem("username");

    const res = await fetch('${API_URL}/attendance/add', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, subject, hours, totalHours }),
    });

    alert((await res.json()).message);
    if (res.ok) window.location.reload();
}

// Fetch Attendance Data
async function fetchAttendance() {
    const username = localStorage.getItem("username");
    const res = await fetch('${API_URL}/attendance/${username}');
    displayAttendance(await res.json());
}

function displayAttendance(attendance) {
    const list = document.getElementById("attendanceList");
    list.innerHTML = "";
    attendance.forEach(item => {
        list.innerHTML += <li>${item.subject}: ${item.hours}/${item.totalHours} hours</li>;
    });
}

// Update Cat Mood
async function updateCatMood() {
    const username = localStorage.getItem("username");
    const res = await fetch('${API_URL}/attendance/${username}');
    const attendance = await res.json();
    
    let avgAttendance = attendance.reduce((sum, item) => sum + (item.hours / item.totalHours) * 100, 0) / attendance.length;
    
    document.getElementById("cat").style.backgroundColor = avgAttendance >= 75 ? "green" : avgAttendance >= 50 ? "yellow" : "red";
}

// Logout
function logoutUser() {
    localStorage.clear();
    window.location.href = "index.html";
}