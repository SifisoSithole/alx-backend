import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const PORT = 1245;

const reserveSeat = async (number) => {
  const setAsync = promisify(client.SET).bind(client);
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.GET).bind(client);
  return await getAsync('available_seats');
};

app.get('/available_seats', async (_, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: Number.parseInt(numberOfAvailableSeats || 0) });
});

app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation is blocked' });
    return;
  }

  try {
    const job = queue.create('reserve_seat');

    job.on('failed', (err) => {
      console.log('Seat reservation job', job.id, 'failed:', err.message || err.toString());
    });

    job.on('complete', () => {
      console.log('Seat reservation job', job.id, 'completed');
    });

    job.save();
    res.json({ status: 'Reservation in process' });
  } catch {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (_job, done) => {
    const availableSeats = Number.parseInt(await getCurrentAvailableSeats() || 0);
    reservationEnabled = availableSeats > 1 ? reservationEnabled : false;

    if (availableSeats >= 1) {
      await reserveSeat(availableSeats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

const resetAvailableSeats = async (initialSeatsCount) => {
  const setAsync = promisify(client.SET).bind(client);
  await setAsync('available_seats', Number.parseInt(initialSeatsCount));
};

app.listen(PORT, () => {
  resetAvailableSeats(process.env.INITIAL_SEATS_COUNT || INITIAL_SEATS_COUNT)
    .then(() => {
      reservationEnabled = true;
      console.log(`API available on localhost port ${PORT}`);
    });
});

export default app;
