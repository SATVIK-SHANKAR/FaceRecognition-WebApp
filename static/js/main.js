// function register() {
//     const name = document.getElementById('nameInput').value.trim();
//     if (!name) {
//         showResult('Please enter a name', 'error');
//         return;
//     }

//     fetch('/register', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//         },
//         body: `name=${encodeURIComponent(name)}`
//     })
//         .then(response => response.json())
//         .then(data => {
//             showResult(data.message, data.status);
//         })
//         .catch(error => {
//             showResult('Registration failed', 'error');
//         });
// }

// function recognize() {
//     fetch('/recognize', {
//         method: 'POST'
//     })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 showResult(`Welcome, ${data.name}!`, 'success');
//             } else {
//                 showResult(data.message, 'error');
//             }
//         })
//         .catch(error => {
//             showResult('Recognition failed', 'error');
//         });
// }

// function showResult(message, status) {
//     const resultDiv = document.getElementById('result');
//     resultDiv.textContent = message;
//     resultDiv.className = `result ${status}`;
// }



let isRegistering = false;

function register() {
    const name = document.getElementById('nameInput').value.trim();
    if (!name) {
        showResult('Please enter a name', 'error');
        return;
    }

    if (isRegistering) {
        return;
    }

    isRegistering = true;
    const registerBtn = document.getElementById('registerBtn');
    registerBtn.disabled = true;
    showResult('Please look at the camera. Capturing face data...', 'success');

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `name=${encodeURIComponent(name)}`
    })
        .then(response => response.json())
        .then(data => {
            showResult(data.message, data.status);
            if (data.status === 'success') {
                document.getElementById('nameInput').value = '';
            }
        })
        .catch(error => {
            showResult('Registration failed. Please try again.', 'error');
        })
        .finally(() => {
            isRegistering = false;
            registerBtn.disabled = false;
        });
}

function recognize() {
    const recognizeBtn = document.getElementById('recognizeBtn');
    recognizeBtn.disabled = true;
    showResult('Recognizing face...', 'success');

    fetch('/recognize', {
        method: 'POST'
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showResult(`Welcome, ${data.name}!`, 'success');
            } else {
                showResult(data.message, 'error');
            }
        })
        .catch(error => {
            showResult('Recognition failed. Please try again.', 'error');
        })
        .finally(() => {
            recognizeBtn.disabled = false;
        });
}

function showResult(message, status) {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = message;
    resultDiv.className = `result ${status}`;
}





