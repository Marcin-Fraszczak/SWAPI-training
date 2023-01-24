const df = document.querySelector(".dataframe");


if (df) {
    let show = 10;
    let more = 10;

    function showRows() {
        let columns = visibleCols();
        headers.forEach((header, index) => {
            header.style.background = "white";
            header.style.display = columns[index];
        });
        rows.forEach(row => {
            const th = row.querySelector("th");
            if (Number(th.textContent) <= show) {
                row.style.display = "";
                const tds = row.querySelectorAll("td");
                tds.forEach((td, index) => {
                    td.style.display = columns[index];
                });
            } else {
                row.style.display = "none";
            }
        });
        updateRowButtons(showLessButton, showMoreButton);
    }

    function showMore(more) {
        if ((more < 0 && show > 10) || (more > 0 && show < rows.length)) {
            show += more;
            showRows();
        }
    }

    function updateRowButtons(showLessButton, showMoreButton) {
        if (show <= 10) {
            showLessButton.classList.add("disabled");
        } else {
            showLessButton.classList.remove("disabled");
        }
        if (show >= rows.length) {
            showMoreButton.classList.add("disabled");
        } else {
            showMoreButton.classList.remove("disabled");
        }
    }

    function updateColButtons(e) {
        if (e.target.tagName === "A" && [...e.target.classList].includes("btn-light")) {
            e.target.classList.remove("btn-light");
            e.target.classList.add("btn-warning");
            showRows();
        } else if (e.target.tagName === "A") {
            e.target.classList.remove("btn-warning");
            e.target.classList.add("btn-light");
            showRows();
        }
    }

    function visibleCols() {
        let columns = [];
        const colButtons = colButtonsContainer.querySelectorAll("a");
        colButtons.forEach(button => {
            if ([...button.classList].includes("btn-warning")) {
                columns.push("");
            } else {
                columns.push("none");
            }
        });
        return columns;
    }

    df.classList.add("table", "table-striped", "text-center");

    const headers = [...df.querySelector("thead").querySelectorAll("th")];
    headers.shift();
    const rows = df.querySelectorAll("tbody > tr");
    const showMoreButton = document.querySelector("#show-more");
    const showLessButton = document.querySelector("#show-less");
    const colButtonsContainer = document.querySelector("#columns-buttons");
    showLessButton.addEventListener("click", e => showMore(-more));
    showMoreButton.addEventListener("click", e => showMore(more));
    colButtonsContainer.addEventListener("click", e => updateColButtons(e));
    showRows();

}