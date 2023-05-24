import { createClient, print } from 'redis';

const client = createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

client.hset('HolbertonSchools', 'Portland', 50, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Seattle', 80, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'New York', 20, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Bogota', 20, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Cali', 40, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hset('HolbertonSchools', 'Paris', 2, (err, reply) => {
    print(`Reply: ${reply}`);
});

client.hgetall('HolbertonSchools', (err, reply) => {
    console.log(reply)
})