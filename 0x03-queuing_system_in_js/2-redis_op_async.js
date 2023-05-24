import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool(schoolName, value) {
    const reply = await setAsync(schoolName, value);
    print(`Reply: ${reply}`);
}

async function displaySchoolValue(schoolName) {
    const reply = await getAsync(schoolName);
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
