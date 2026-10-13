(() => {
  const form = document.getElementById('create-form');
  if (!form) return;
  const radios = [...form.querySelectorAll('input[name="kind"]')];
  const purpose = document.getElementById('purpose-field');
  const purposeInput = form.querySelector('[name="team_purpose"]');
  const due = form.querySelector('[name="due_date"]');
  function update() {
    const task = radios.some(input => input.checked && input.value === 'gorev');
    radios.forEach(input => input.closest('.type-option').classList.toggle('selected', input.checked));
    purpose.hidden = !task;
    purposeInput.required = task;
    due.required = task;
    document.getElementById('due-hint').textContent = task ? '· Zorunlu' : '· İsteğe bağlı';
  }
  radios.forEach(input => input.addEventListener('change', update));
  update();
})();
