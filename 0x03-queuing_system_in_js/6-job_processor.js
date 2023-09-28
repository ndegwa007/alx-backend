#!/usr/bin/node
// process a job using kue

const kue = require('kue');

const Kue = kue.createQueue();

function sendNotification (phoneNumber, message) {
  console.log(`sending notification to ${phoneNumber}, with message: ${message}`);
}

Kue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
});
