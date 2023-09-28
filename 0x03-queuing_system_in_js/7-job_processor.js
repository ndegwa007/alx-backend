#!/usr/bin/node
// process a series of jobs

const blacklist = ['4153518780', '4153518781'];
const kue = require('kue');
const Kue = kue.createQueue();

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

Kue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
