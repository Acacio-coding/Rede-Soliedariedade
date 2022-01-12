const userCounter = document.querySelector("#user-counter")
const entityCounter = document.querySelector("#entity-counter");
const familyCounter = document.querySelector("#family-counter");
const donationCounter = document.querySelector("#donation-counter");

const count = (value, end, tag) => {
  tag.innerHTML = value;

  if (value < end)
    setTimeout(() => count(value + 1, end, tag), 10);
}

window.onload = () => {
  const start = 0;

  const users = {
    counter: userCounter,
    end: 100,
  }

  const entities = {
    counter: entityCounter,
    end: 100,
  }

  const families = {
    counter: familyCounter,
    end: 100, 
  }

  const donations = {
    counter: donationCounter,
    end: 100,
  }

  count(start, users.end, users.counter);
  count(start, entities.end, entities.counter);
  count(start, families.end, families.counter);
  count(start, donations.end, donations.counter);
}

