async function processXML() {
  const xmlInput = document.getElementById('xmlInput').value;
  const output = document.getElementById('output');

  try {
    const response = await fetch('/process-xml', {
      method: 'POST',
      headers: { 'Content-Type': 'application/xml' },
      body: xmlInput
    });

    const result = await response.json();

    if (response.ok) {
      output.textContent = JSON.stringify(result, null, 2);
    } else {
      output.textContent = 'Error: ' + result.error;
    }
  } catch (error) {
    output.textContent = 'Error: ' + error.message;
  }
}
