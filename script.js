const form = document.getElementById("frm1");

form.addEventListener("submit", function (event) {
  event.preventDefault();
  const groupMembers = parseInt(document.getElementById("groupMembers").value);
  const student1 = document.getElementById("student1").value.trim();
  const student2 = document.getElementById("student2").value.trim();
  const student3 = document.getElementById("student3").value.trim();
  const student4 = document.getElementById("student4").value.trim();

  // Validate group members
  if (isNaN(groupMembers) || groupMembers < 1 || groupMembers > 4) {
    alert("Number of members must be between 1 and 4.");
    return;
  }

  // Collect student IDs
  const students = [student1, student2, student3, student4];
  const filledStudents = students.filter(s => s !== "");

  // Check if number of filled students matches group members
  if (filledStudents.length !== groupMembers) {
    alert(`Number of entered student fields (${filledStudents.length}) does not match the number of members (${groupMembers}).`);
    return;
  }

  // Validate each student ID
  const studentSet = new Set();
  for (let i = 0; i < filledStudents.length; i++) {
    const student = filledStudents[i];
    if (!/^\d{8}$/.test(student)) {
      alert(`Student ${i+1} ID must be an 8-digit number.`);
      return;
    }
    if (studentSet.has(student)) {
      alert("Duplicate student IDs are not allowed.");
      return;
    }
    studentSet.add(student);
  }

  // If all validations pass
  alert("Form submitted successfully!");
  // Here you can proceed with actual submission, e.g., form.submit();
});
