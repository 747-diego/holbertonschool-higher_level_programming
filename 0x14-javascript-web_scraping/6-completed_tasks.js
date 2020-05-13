#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const GettingRequest = require('request');
const content = process.argv;

GettingRequest(content[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const TasksCompleted = {};
  const body = JSON.parse(body);
  for (const tasks of body) {
    if (tasks.completed === true) {
      let TaskByUserID = TasksCompleted[tasks.userId];
      if (TaskByUserID) {
        TaskByUserID++;
      } else {
        TaskByUserID = 1;
      }
    }
  }
  console.log(TasksCompleted);
});
