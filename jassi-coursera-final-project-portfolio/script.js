const form = document.getElementById('recommendation-form');
const list = document.getElementById('recommendation-list');
const popup = document.getElementById('popup');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const text = document.getElementById('recommendation-text').value;
  const name = document.getElementById('recommender-name').value;

  const newRec = document.createElement('li');
  newRec.innerHTML = `<q>${text}</q> – ${name}`;
  list.appendChild(newRec);

  popup.style.display = 'block';
  setTimeout(() => popup.style.display = 'none', 3000);

  form.reset();
});
