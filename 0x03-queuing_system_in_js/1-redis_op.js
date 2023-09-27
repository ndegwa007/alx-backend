#!/usr/bin/node
// start a node_redis client

import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server', err));
client.on('connect', () => {
  console.log('Redis client is connected to the server');
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
