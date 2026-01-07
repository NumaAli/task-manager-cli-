//  Delete Task Feature 
let tasks = [
  { id: 1, name: 'Sample Task 1' },
  { id: 2, name: 'Sample Task 2' }
];

function deleteTask(id) {
  tasks = tasks.filter(task => task.id !== id);
  console.log("✅ Task deleted successfully!");
}

// CLI input example
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Enter task ID to delete: ', id => {
  deleteTask(Number(id));
  readline.close();
  c
  onsole.log("Current tasks:", tasks);
});
