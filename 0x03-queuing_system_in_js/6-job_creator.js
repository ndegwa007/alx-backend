#!/usr/bin/node
// use kue to create a job Queue

const kue = require('kue');
const push_notification_code = kue.createQueue();

const obj = { phoneNumber: '+254', message: 'call me' };

const job = push_notification_code.create('push_notification_code', obj);

job.save((err) => {
  if (!err) { console.log(`Notification job created: ${job.id}`); }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => { console.log('Notification job failed'); });
