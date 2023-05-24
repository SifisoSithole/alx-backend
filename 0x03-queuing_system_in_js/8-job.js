export default function createPushNotificationsJobs(jobs, queue) {
    if (Object.getPrototypeOf(jobs) !== Array.prototype) throw Error('Jobs is not an array');

    jobs.forEach((task) => {
        let job = queue.create('push_notification_code_3', task).save(
            (err) => {
                if (!err) console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', () => console.log(`Notification job ${job.id} completed`));
        job.on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`));
        job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
}