#!/usr/bin/node
// subscriber

const Redis = require('ioredis');
const client = new Redis();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server', err));
const channel_name = 'holberton school channel';
const listener = (message, channel) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
  if (message === null) { return; }
  console.log(channel, message);
};
client.subscribe(channel_name, listener);
