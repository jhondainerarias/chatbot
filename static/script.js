async function enviarMensaje() {
  const input = document.getElementById("mensaje");
  const chatBox = document.getElementById("chat-box");
  const mensaje = input.value.trim();

  if (mensaje === "") return;

  // Mostrar mensaje del usuario
  chatBox.innerHTML += `<div class="message user"><div class="bubble">${mensaje}</div></div>`;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Enviar al servidor Flask
  const respuesta = await fetch("/enviar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensaje }),
  });

  const data = await respuesta.json();

  // Mostrar respuesta del bot
  chatBox.innerHTML += `
    <div class="message bot">
      <img src="/static/jhon.jpg" class="bot-avatar" alt="bot" />
      <div class="bubble">${data.respuesta}</div>
    </div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}

function enviarTexto(texto) {
  document.getElementById("mensaje").value = texto;
  enviarMensaje();
}
// 🧠 Función para efecto de escritura animada
function escribirTexto(elemento, texto, velocidad = 25) {
  let i = 0;
  const intervalo = setInterval(() => {
    elemento.innerHTML += texto.charAt(i);
    i++;
    if (i >= texto.length) clearInterval(intervalo);
  }, velocidad);
}

// 💬 Enviar mensaje al servidor
async function enviarMensaje() {
  const input = document.getElementById("mensaje");
  const chatBox = document.getElementById("chat-box");
  const mensaje = input.value.trim();

  if (mensaje === "") return;

  // Mostrar mensaje del usuario
  chatBox.innerHTML += `
    <div class="message user">
      <div class="bubble">${mensaje}</div>
    </div>`;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Mostrar mensaje temporal de "escribiendo..."
  const botMsg = document.createElement("div");
  botMsg.classList.add("message", "bot");
  botMsg.innerHTML = `
    <img src="/static/jhon.jpg" class="bot-avatar" alt="bot" />
    <div class="bubble typing">Escribiendo<span class="dots">...</span></div>`;
  chatBox.appendChild(botMsg);
  chatBox.scrollTop = chatBox.scrollHeight;

  // Enviar mensaje al backend
  const respuesta = await fetch("/enviar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensaje }),
  });

  const data = await respuesta.json();

  // Reemplazar el texto "Escribiendo..." con la respuesta real
  const bubble = botMsg.querySelector(".bubble");
  bubble.classList.remove("typing");
  bubble.innerHTML = ""; // limpiar burbuja
  escribirTexto(bubble, data.respuesta, 20);

  chatBox.scrollTop = chatBox.scrollHeight;
}

// Enviar texto con botones rápidos
function enviarTexto(texto) {
  document.getElementById("mensaje").value = texto;
  enviarMensaje();
}
