$(document).ready(function () {
  const form = document.getElementById("calculadoraForm");
  form.addEventListener("submit", handleSubmit);

  function handleSubmit(event) {
    event.preventDefault();

    const gender = getSelectedValue("gender");
    const age = getInputNumberValue("age");
    const weight = getInputNumberValue("weight");
    const height = getInputNumberValue("height");
    const activity_level = getSelectedValue("activity_level");

    const tmb = Math.round(
      gender === "female"
        ? 655 + 9.6 * weight + 1.8 * height - 4.7 * age
        : 66 + 13.7 * weight + 5 * height - 6.8 * age
    );

    const maintenance = Math.round(tmb * Number(activity_level));
    const loseWeight = maintenance - 450;
    const gainWeight = maintenance + 450;

    const layout = `

    <p style="color: #707070; margin-top: -25px; font-weight: 600">
    Aqui está o resultado:
    </p>

    <div class="result-content" style="background-color: #1a1a1a; padding: 10px; border-radius: 10px; animation: slide-left 1.3s ease-in-out;">
              <ul style="list-style: none; font-size: 15px;">
               
                <li>
                  Para manter o seu peso você precisa consumir em média
                  <strong style="color: #83a92f;">${maintenance} calorias</strong>.
                </li>
                <li>
                  Para perder peso você precisa consumir em média
                  <strong style="color: #83a92f;">${loseWeight} calorias</strong>.
                </li>
                
              </ul>
        </div>
    `;
    // <li>
    //               Seu metabolismo basal é de <strong style="color: #83a92f;">${tmb} calorias</strong>.
    //             </li>

    // <li>
    //               Para ganhar peso você precisa consumir em média
    //               <strong style="color: #83a92f;">${gainWeight} calorias</strong>.
    //             </li>

    const result = document.getElementById("result");

    result.innerHTML = layout;
  }

  function getSelectedValue(id) {
    const select = document.getElementById(id);
    return select.options[select.selectedIndex].value;
  }

  function getInputNumberValue(id) {
    return Number(document.getElementById(id).value);
  }
});
