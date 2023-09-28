#!/usr/bin/node
// subscriber

const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server', err));
const channel_name = 'holberton school channel';
client.subscribe(channel_name);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER' && channel === channel_name) {
    client.unsubscribe(channel);
    client.quit();
  }
});
