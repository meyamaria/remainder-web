document.addEventListener('DOMContentLoaded', () => {
  if (!("Notification" in window)) return;

  if (Notification.permission === "default") {
    Notification.requestPermission();
  }

  if (!Array.isArray(userData) || userData.length === 0) return;

  const latestUser = userData[userData.length - 1];
  const sleepTimeStr = latestUser.sleep_time;
  const wakeTimeStr = latestUser.wake_time;

  function parseTimeToDate(timeStr) {
    const [time, modifier] = timeStr.split(" ");
    let [hours, minutes] = time.split(":").map(Number);
    if (modifier === 'PM' && hours !== 12) hours += 12;
    if (modifier === 'AM' && hours === 12) hours = 0;
    const now = new Date();
    now.setHours(hours, minutes, 0, 0);
    return now;
  }

  function scheduleNotification(time, title, body) {
    const now = new Date();
    const delay = time.getTime() - now.getTime();
    if (delay > 0) {
      setTimeout(() => {
        if (Notification.permission === "granted") {
          new Notification(title, { body });
        }
      }, delay);
    }
  }

  const sleepTime = parseTimeToDate(sleepTimeStr);
  const wakeTime = parseTimeToDate(wakeTimeStr);
  const exerciseTime = new Date(wakeTime.getTime() + 30 * 60 * 1000);

  scheduleNotification(sleepTime, "😴 Time to Sleep", "Prepare to go to bed.");
  scheduleNotification(wakeTime, "🌞 Wake Up!", "Good morning! Drink some water.");
  scheduleNotification(exerciseTime, "🏃 Exercise Time", "Time for some light exercise.");
});
