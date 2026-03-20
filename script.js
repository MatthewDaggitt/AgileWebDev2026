let buttonePressed = 0;

function buttonClicked() {
    buttonePressed++;
    console.log("Button has been pressed " + buttonePressed + " times.");
}
function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
    
    }

console.log(factorial(5));





function showAlert(msg) {
    alert(msg);
}
function myFunction() {
    let message = prompt("Enter your message:");
    showAlert(message);
}

function sum(){
    let num1 = parseInt(prompt("Enter the first number:"));
    let num2 = parseInt(prompt("Enter the second number:"));
    let result = num1 + num2;
    console.log("The sum is: " + result);
    console.log(typeof num1);
    console.log(typeof num2);
    
    // alert("The sum is: " + result);
}
//sum

function changeHeading() {
    let headings = document.getElementsByTagName("h1");
    
    for (let i = 0; i < headings.length; i++) {
        let message = prompt("Enter the new heading text:");
        headings[i].innerText = message;
    }
}
