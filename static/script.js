document.getElementById("search-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const keyword = document.getElementById("keyword").value;

    fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keyword }),
    })
        .then((response) => response.json())
        .then((data) => {
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = data.length
                ? data.map((subsidy) =>
                      `<div class="result-item">
                           <h4>${subsidy.name}</h4>
                           <p><strong>Category:</strong> ${subsidy.category}</p>
                           <p><strong>Eligibility:</strong> ${subsidy.eligibility}</p>
                           ${
                               subsidy.official_link
                                   ? `<a href="${subsidy.official_link}" target="_blank">Visit Official Website</a>`
                                   : ""
                           }
                       </div>`
                  ).join("")
                : "<p>No subsidies match your keyword.</p>";
        });
});
