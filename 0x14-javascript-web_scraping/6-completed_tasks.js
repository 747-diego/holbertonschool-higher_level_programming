#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const GettingRequest = require('request');
const content = process.argv;

GettingRequest(content[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const TasksCompleted = {};
  for (const tasks of JSON.parse(body)) {
    if (tasks.completed === true) {
      const Id = tasks.userId;
      if (TasksCompleted) {
        TasksCompleted[Id] = TasksCompleted[Id] + 1;
      } else {
        TasksCompleted[Id] = 1;
      }
    }
  }

  console.log(TasksCompleted);
});
