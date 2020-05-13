#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const GettingRequest = require('request');
const content = process.argv[2];

GettingRequest(content, function (err, _resp, body) {
  if (err) {
    console.log(err);
  }

  const TasksCompleted = {};
  for (const tasks of JSON.parse(body)) {
    if (tasks.completed === true) {
      if (TasksCompleted[tasks.userId]) {
        TasksCompleted[tasks.userId] = TasksCompleted[tasks.userId] + 1;
      } else {
        TasksCompleted[tasks.userId] = 1;
      }
    }
  }

  console.log(TasksCompleted);
});
